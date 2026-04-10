---
tags:
  - space-style
description: Notion-like reading and editing surface for the do4ai workspace.
priority: 50
---
```space-style
/* priority: 50 */
html {
  --editor-width: 980px !important;
  --editor-font: "Pretendard Variable", "Pretendard", "Inter", sans-serif !important;
  --ui-font: "Pretendard Variable", "Pretendard", "Inter", sans-serif !important;
  --ui-accent-color: #2f6feb;
  --top-background-color: #f7f6f3;
}

html,
body {
  background: #f7f6f3;
  color: #1f2328;
}

#sb-top {
  background: rgba(247, 246, 243, 0.92) !important;
  border-bottom: 1px solid #e7e5e4;
  backdrop-filter: blur(14px);
}

#sb-main {
  background:
    radial-gradient(circle at top, rgba(47, 111, 235, 0.05), transparent 28rem),
    linear-gradient(180deg, #f7f6f3 0%, #f2efe9 100%);
}

#sb-editor {
  padding: 2rem 0 4rem;
}

.cm-editor {
  background: #ffffff;
  border: 1px solid #e7e5e4;
  border-radius: 18px;
  box-shadow: 0 20px 50px rgba(15, 23, 42, 0.05);
  padding: 1.25rem 0;
}

.cm-scroller {
  padding: 0 1.5rem 2rem;
}

.cm-content .HyperMD-header-1,
.cm-content .sb-line-h1 {
  font-size: 2.2rem;
  font-weight: 700;
  letter-spacing: -0.03em;
}

.cm-content .HyperMD-header-2,
.cm-content .sb-line-h2 {
  margin-top: 1.8rem;
  font-size: 1.45rem;
  font-weight: 650;
}

button {
  border-radius: 10px;
}

.sb-panel,
.sb-modal,
.sb-sidebar {
  background: #fbfbfa;
}
```
