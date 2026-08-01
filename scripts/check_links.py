#!/usr/bin/env python3
"""vault/ 안의 상대 링크가 실제 파일을 가리키는지 검사한다.

CLAUDE.md 5절의 "링크: 상대 링크 깨짐 0" 게이트를 자동으로 확인하는 스크립트다.
문서를 옮기거나 이름을 바꾼 뒤, 그리고 main 에 올리기 전에 돌린다.

    python3 scripts/check_links.py            # vault 전체 검사
    python3 scripts/check_links.py --json     # 결과를 JSON 으로 출력

깨진 링크가 하나라도 있으면 종료코드 1 을 돌려준다.

검사 대상은 상대 경로 링크뿐이다. http/https/mailto/앵커 링크는 건너뛴다.
링크 대상이 폴더면 그 안의 index.md 가 있는지 본다. 마크다운은 링크 주소 안의
괄호를 균형쌍까지 허용하므로(예: `모놀리식 아키텍처(Monolithic Architecture)`)
단순 정규식 대신 괄호 깊이를 세어 파싱한다.
"""
import argparse
import json
import os
import re
import sys
from urllib.parse import unquote

DEFAULT_ROOT = "vault"
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "#")


def parse_links(text):
    """마크다운 인라인 링크를 (위치, 라벨, 주소) 로 뽑는다. 괄호 균형을 지킨다."""
    out = []
    i, n = 0, len(text)
    while i < n:
        if text[i] != "[" or (i > 0 and text[i - 1] == "!"):
            i += 1
            continue
        depth, j = 0, i
        while j < n:
            if text[j] == "[":
                depth += 1
            elif text[j] == "]":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= n or j + 1 >= n or text[j + 1] != "(":
            i += 1
            continue
        depth, k = 0, j + 1
        while k < n:
            if text[k] == "(":
                depth += 1
            elif text[k] == ")":
                depth -= 1
                if depth == 0:
                    break
            elif text[k] == "\n":
                break
            k += 1
        if k >= n or text[k] != ")":
            i += 1
            continue
        out.append((i, text[i + 1 : j], text[j + 2 : k]))
        i = k + 1
    return out


def strip_code(text):
    """코드펜스와 인라인 코드를 지운다. 줄 번호는 유지한다."""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def check(root):
    broken = []
    total = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as f:
                body = strip_code(f.read())
            for start, label, raw in parse_links(body):
                total += 1
                dest = raw.split(' "')[0].strip().strip("<>")
                if not dest or dest.startswith(SKIP_SCHEMES):
                    continue
                target = unquote(dest.split("#")[0]).strip()
                if not target:
                    continue
                resolved = os.path.normpath(os.path.join(dirpath, target))
                if os.path.exists(resolved):
                    continue
                if os.path.exists(os.path.join(resolved, "index.md")):
                    continue
                if not target.endswith(".md") and os.path.exists(resolved + ".md"):
                    continue
                broken.append({
                    "file": path,
                    "line": body[:start].count("\n") + 1,
                    "label": label,
                    "target": dest,
                })
    return total, broken


def main():
    ap = argparse.ArgumentParser(description="vault 상대 링크 검사")
    ap.add_argument("root", nargs="?", default=DEFAULT_ROOT, help="검사할 폴더 (기본 vault)")
    ap.add_argument("--json", action="store_true", help="결과를 JSON 으로 출력한다")
    args = ap.parse_args()

    if not os.path.isdir(args.root):
        print(f"폴더를 찾을 수 없다: {args.root}", file=sys.stderr)
        return 2

    total, broken = check(args.root)
    if args.json:
        json.dump(broken, sys.stdout, ensure_ascii=False, indent=1)
        print()
    else:
        for b in broken:
            print(f"{b['file']}:{b['line']}  [{b['label']}]({b['target']})")
        print(f"\n링크 {total}개 검사, 깨짐 {len(broken)}건")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
