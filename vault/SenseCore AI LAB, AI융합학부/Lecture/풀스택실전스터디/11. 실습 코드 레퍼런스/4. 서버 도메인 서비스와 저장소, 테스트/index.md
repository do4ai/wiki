---
title: "4. 서버 도메인 서비스와 저장소, 테스트"
source_kind: page
source_path: manual-local/lecture/fullstack-study/11-practice-code/04-server-domain
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 4. 서버 도메인 서비스와 저장소, 테스트
이 페이지는 06장부터 08장까지 구현한 백엔드 기능의 본체를 담습니다. 카탈로그, 인증, 장바구니, 주문, 결제, 운영자 기능이 서비스 계층과 저장소 계층에 어떻게 나뉘어 들어갔는지 확인하는 자리입니다.

`shared/service.py`가 애플리케이션 서비스 역할을 맡아 유스케이스를 담고, `shared/store.py`가 저장소 접근을 맡습니다. `contexts/` 아래 네 패키지는 02장에서 자른 바운디드 컨텍스트의 자리를 코드에 미리 만들어 둔 것입니다. `tests/test_api.py`는 09장의 회귀 검증 바닥에 해당하며, 주요 흐름이 깨지지 않았는지를 API 수준에서 확인합니다.

# 파일

## `server/shared/service.py`

```python
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from config import get_settings
from shared.auth import create_access_token, hash_password, verify_password
from shared.models import (
    CartItem,
    Order,
    OrderStatus,
    PaymentAttempt,
    PaymentAttemptStatus,
    Product,
    User,
    UserRole,
)


FREE_SHIPPING_THRESHOLD = 150_000
STANDARD_SHIPPING_FEE = 3_500


def _seed_products() -> list[dict[str, object]]:
    return [
        {
            "id": "prod_studio_jacket",
            "slug": "studio-jacket",
            "title": "Studio Field Jacket",
            "category": "Outerwear",
            "price": 129000,
            "compare_at_price": 149000,
            "inventory": 12,
            "rating": 4.8,
            "tags": ["Best seller", "Lecture pick"],
            "summary": "도심형 편집숍 무드로 만든 대표 상품 카드 예시.",
        },
        {
            "id": "prod_canvas_bag",
            "slug": "canvas-market-bag",
            "title": "Canvas Market Bag",
            "category": "Accessories",
            "price": 49000,
            "compare_at_price": None,
            "inventory": 8,
            "rating": 4.6,
            "tags": ["Low stock", "Bundle"],
            "summary": "장바구니와 재고 상태를 설명하기 좋은 액세서리 상품.",
        },
        {
            "id": "prod_glass_set",
            "slug": "amber-glass-set",
            "title": "Amber Glass Set",
            "category": "Home",
            "price": 36000,
            "compare_at_price": 42000,
            "inventory": 24,
            "rating": 4.9,
            "tags": ["Home edit", "Giftable"],
            "summary": "프로모션 가격과 compare-at-price를 보여주기 위한 샘플.",
        },
        {
            "id": "prod_desk_lamp",
            "slug": "mono-desk-lamp",
            "title": "Mono Desk Lamp",
            "category": "Lighting",
            "price": 89000,
            "compare_at_price": 109000,
            "inventory": 5,
            "rating": 4.7,
            "tags": ["Almost gone", "Visual focus"],
            "summary": "상세 카드와 admin low-stock 상태를 연결하기 위한 샘플.",
        },
    ]


def seed_database(db: Session) -> None:
    if db.scalar(select(func.count()).select_from(Product)) == 0:
        db.add_all(Product(**payload) for payload in _seed_products())

    settings = get_settings()
    admin_user = db.scalar(select(User).where(User.email == settings.bootstrap_admin_email.lower()))
    if admin_user is None:
        db.add(
            User(
                email=settings.bootstrap_admin_email.lower(),
                full_name=settings.bootstrap_admin_name,
                password_hash=hash_password(settings.bootstrap_admin_password),
                role=UserRole.ADMIN.value,
            )
        )

    db.commit()


def register_user(db: Session, *, email: str, full_name: str, password: str) -> User:
    normalized_email = email.strip().lower()
    existing_user = db.scalar(select(User).where(User.email == normalized_email))
    if existing_user is not None:
        raise ValueError("email_already_registered")

    user = User(
        email=normalized_email,
        full_name=full_name.strip(),
        password_hash=hash_password(password),
        role=UserRole.CUSTOMER.value,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, *, email: str, password: str) -> User | None:
    user = db.scalar(select(User).where(User.email == email.strip().lower()))
    if user is None or not verify_password(password, user.password_hash):
        return None
    return user


def get_product_by_slug(db: Session, slug: str) -> Product | None:
    return db.scalar(select(Product).where(Product.slug == slug))


def get_product_by_id(db: Session, product_id: str) -> Product | None:
    return db.get(Product, product_id)


def serialize_user(user: User) -> dict[str, object]:
    return {
        "id": user.id,
        "email": user.email,
        "name": user.full_name,
        "full_name": user.full_name,
        "segment": None,
        "role": user.role,
        "created_at": user.created_at.isoformat(),
    }


def serialize_product(product: Product) -> dict[str, object]:
    return {
        "id": product.id,
        "slug": product.slug,
        "title": product.title,
        "category": product.category,
        "price": product.price,
        "compare_at_price": product.compare_at_price,
        "inventory": product.inventory,
        "rating": product.rating,
        "tags": product.tags,
        "summary": product.summary,
    }


def catalog_payload(db: Session) -> dict[str, object]:
    products = db.scalars(select(Product).order_by(Product.created_at.asc())).all()
    return {
        "brand": {
            "name": "Edition Lecture",
            "headline": "실전 풀스택 스터디용 이커머스 레퍼런스",
            "subhead": "storefront, admin, api 경계를 한 번에 설명하기 위한 샘플 데이터",
        },
        "collections": [
            "Spring edit",
            "Desk objects",
            "Low stock watchlist",
        ],
        "selling_points": [
            "React storefront",
            "FastAPI backend",
            "Admin operations",
        ],
        "items": [serialize_product(product) for product in products],
    }


def _shipping_fee(subtotal: int) -> int:
    if subtotal == 0 or subtotal >= FREE_SHIPPING_THRESHOLD:
        return 0
    return STANDARD_SHIPPING_FEE


def cart_payload(db: Session, user: User) -> dict[str, object]:
    cart_items = db.scalars(
        select(CartItem)
        .options(selectinload(CartItem.product))
        .where(CartItem.user_id == user.id)
        .order_by(CartItem.created_at.asc())
    ).all()

    items: list[dict[str, object]] = []
    subtotal = 0
    item_count = 0

    for cart_item in cart_items:
        product = cart_item.product
        line_total = product.price * cart_item.quantity
        subtotal += line_total
        item_count += cart_item.quantity
        items.append(
            {
                "product_id": product.id,
                "slug": product.slug,
                "title": product.title,
                "quantity": cart_item.quantity,
                "unit_price": product.price,
                "line_total": line_total,
                "inventory": product.inventory,
            }
        )

    shipping_fee = _shipping_fee(subtotal)
    return {
        "items": items,
        "item_count": item_count,
        "subtotal": subtotal,
        "shipping_fee": shipping_fee,
        "total": subtotal + shipping_fee,
        "shipping_policy": f"{FREE_SHIPPING_THRESHOLD}원 이상 무료배송",
    }


def add_cart_item(db: Session, user: User, *, product_id: str, quantity: int) -> dict[str, object]:
    product = get_product_by_id(db, product_id)
    if product is None:
        raise LookupError("product_not_found")
    if product.inventory < quantity:
        raise ValueError("insufficient_inventory")

    cart_item = db.scalar(
        select(CartItem).where(CartItem.user_id == user.id, CartItem.product_id == product_id)
    )
    if cart_item is None:
        cart_item = CartItem(user_id=user.id, product_id=product_id, quantity=quantity)
        db.add(cart_item)
    else:
        if product.inventory < cart_item.quantity + quantity:
            raise ValueError("insufficient_inventory")
        cart_item.quantity += quantity

    db.commit()
    return cart_payload(db, user)


def update_cart_item(db: Session, user: User, *, product_id: str, quantity: int) -> dict[str, object]:
    product = get_product_by_id(db, product_id)
    if product is None:
        raise LookupError("product_not_found")

    cart_item = db.scalar(
        select(CartItem).where(CartItem.user_id == user.id, CartItem.product_id == product_id)
    )
    if cart_item is None:
        raise LookupError("cart_item_not_found")
    if product.inventory < quantity:
        raise ValueError("insufficient_inventory")

    cart_item.quantity = quantity
    db.commit()
    return cart_payload(db, user)


def remove_cart_item(db: Session, user: User, *, product_id: str) -> dict[str, object]:
    cart_item = db.scalar(
        select(CartItem).where(CartItem.user_id == user.id, CartItem.product_id == product_id)
    )
    if cart_item is not None:
        db.delete(cart_item)
        db.commit()
    return cart_payload(db, user)


def serialize_payment_attempt(payment_attempt: PaymentAttempt) -> dict[str, object]:
    return {
        "id": payment_attempt.id,
        "order_id": payment_attempt.order_id,
        "provider": payment_attempt.provider,
        "status": payment_attempt.status,
        "amount": payment_attempt.amount,
        "reference": payment_attempt.provider_reference,
        "provider_reference": payment_attempt.provider_reference,
        "attempted_at": payment_attempt.created_at.isoformat(),
        "created_at": payment_attempt.created_at.isoformat(),
        "confirmed_at": payment_attempt.confirmed_at.isoformat() if payment_attempt.confirmed_at else None,
    }


def _serialize_order(order: Order) -> dict[str, object]:
    latest_payment_attempt = order.payment_attempts[-1] if order.payment_attempts else None
    return {
        "id": order.id,
        "customer": order.customer_name,
        "customer_email": order.customer_email,
        "channel": order.channel,
        "status": order.status,
        "payment_status": order.payment_status,
        "total_amount": order.total_amount,
        "subtotal": order.subtotal,
        "shipping_fee": order.shipping_fee,
        "item_count": order.item_count,
        "note": order.notes,
        "notes": order.notes,
        "items": order.order_lines,
        "created_at": order.created_at.isoformat(),
        "payment_attempt": serialize_payment_attempt(latest_payment_attempt)
        if latest_payment_attempt is not None
        else None,
        "latest_payment_attempt": serialize_payment_attempt(latest_payment_attempt)
        if latest_payment_attempt is not None
        else None,
    }


def get_order_for_user(db: Session, user: User, order_id: str) -> Order | None:
    return db.scalar(
        select(Order)
        .options(selectinload(Order.payment_attempts))
        .where(Order.id == order_id, Order.user_id == user.id)
    )


def create_order_from_cart(db: Session, user: User, *, notes: str | None = None) -> dict[str, object]:
    cart_items = db.scalars(
        select(CartItem)
        .options(selectinload(CartItem.product))
        .where(CartItem.user_id == user.id)
        .order_by(CartItem.created_at.asc())
    ).all()
    if not cart_items:
        raise ValueError("cart_empty")

    subtotal = 0
    item_count = 0
    order_lines: list[dict[str, object]] = []

    for cart_item in cart_items:
        product = cart_item.product
        if product.inventory < cart_item.quantity:
            raise ValueError(f"insufficient_inventory:{product.id}")

        line_total = product.price * cart_item.quantity
        subtotal += line_total
        item_count += cart_item.quantity
        product.inventory -= cart_item.quantity
        order_lines.append(
            {
                "product_id": product.id,
                "slug": product.slug,
                "title": product.title,
                "quantity": cart_item.quantity,
                "unit_price": product.price,
                "line_total": line_total,
            }
        )

    shipping_fee = _shipping_fee(subtotal)
    order = Order(
        user_id=user.id,
        customer_name=user.full_name,
        customer_email=user.email,
        status=OrderStatus.PENDING_PAYMENT.value,
        payment_status=PaymentAttemptStatus.PENDING.value,
        subtotal=subtotal,
        shipping_fee=shipping_fee,
        total_amount=subtotal + shipping_fee,
        item_count=item_count,
        notes=notes,
        order_lines=order_lines,
    )
    db.add(order)
    db.flush()

    payment_attempt = PaymentAttempt(
        order_id=order.id,
        provider="mock",
        status=PaymentAttemptStatus.PENDING.value,
        amount=order.total_amount,
    )
    db.add(payment_attempt)

    for cart_item in cart_items:
        db.delete(cart_item)

    db.commit()
    db.refresh(payment_attempt)

    loaded_order = get_order_for_user(db, user, order.id)
    assert loaded_order is not None
    return {
        "order": _serialize_order(loaded_order),
        "payment_attempt": serialize_payment_attempt(payment_attempt),
    }


def confirm_payment(
    db: Session,
    user: User,
    *,
    order_id: str,
    success: bool,
    provider_reference: str | None = None,
) -> dict[str, object]:
    order = get_order_for_user(db, user, order_id)
    if order is None:
        raise LookupError("order_not_found")

    payment_attempt = db.scalar(
        select(PaymentAttempt)
        .where(PaymentAttempt.order_id == order_id)
        .order_by(PaymentAttempt.created_at.desc())
    )
    if payment_attempt is None:
        raise LookupError("payment_attempt_not_found")

    payment_attempt.provider_reference = provider_reference or f"mock-{order_id[:8]}"
    payment_attempt.confirmed_at = datetime.now(timezone.utc)

    if success:
        payment_attempt.status = PaymentAttemptStatus.CONFIRMED.value
        order.payment_status = PaymentAttemptStatus.CONFIRMED.value
        order.status = OrderStatus.PAID.value
    else:
        payment_attempt.status = PaymentAttemptStatus.FAILED.value
        order.payment_status = PaymentAttemptStatus.FAILED.value
        order.status = OrderStatus.PAYMENT_FAILED.value

    db.commit()
    db.refresh(payment_attempt)

    refreshed_order = get_order_for_user(db, user, order_id)
    assert refreshed_order is not None
    return {
        "order": _serialize_order(refreshed_order),
        "payment_attempt": serialize_payment_attempt(payment_attempt),
    }


def orders_summary_payload(db: Session, user: User) -> dict[str, object]:
    orders = db.scalars(
        select(Order)
        .options(selectinload(Order.payment_attempts))
        .where(Order.user_id == user.id)
        .order_by(Order.created_at.desc())
        .limit(5)
    ).all()
    return {
        "stages": [
            {"label": "Cart", "value": "review"},
            {"label": "Payment", "value": "confirm"},
            {"label": "Fulfillment", "value": "track"},
        ],
        "recent_orders": [_serialize_order(order) for order in orders],
        "policy_notes": [
            "재고 5개 이하 상품은 admin에서 low stock으로 강조",
            "결제는 mock confirm endpoint로 마무리되는 강의용 흐름",
        ],
    }


def buyer_orders_payload(db: Session, user: User) -> dict[str, object]:
    orders = db.scalars(
        select(Order)
        .options(selectinload(Order.payment_attempts))
        .where(Order.user_id == user.id)
        .order_by(Order.created_at.desc())
    ).all()
    return {"items": [_serialize_order(order) for order in orders]}


def admin_dashboard_payload(db: Session) -> dict[str, object]:
    orders = db.scalars(
        select(Order)
        .options(selectinload(Order.payment_attempts))
        .order_by(Order.created_at.desc())
    ).all()
    products = db.scalars(select(Product)).all()

    gross_revenue = sum(order.total_amount for order in orders if order.status == OrderStatus.PAID.value)
    total_orders = len(orders)
    low_stock = len([product for product in products if product.inventory <= 8])
    average_order_value = int(gross_revenue / total_orders) if total_orders else 0

    highlight_order = (
        _serialize_order(orders[0])
        if orders
        else {
            "id": "awaiting-first-order",
            "customer": "No orders yet",
            "customer_email": "",
            "channel": "Storefront",
            "status": "awaiting_first_order",
            "payment_status": "pending",
            "total_amount": 0,
            "subtotal": 0,
            "shipping_fee": 0,
            "item_count": 0,
            "notes": None,
            "items": [],
            "created_at": "",
            "latest_payment_attempt": None,
        }
    )

    return {
        "metrics": [
            {"label": "Gross Revenue", "value": f"{gross_revenue:,} KRW", "delta": "live"},
            {"label": "Orders", "value": str(total_orders), "delta": "live"},
            {"label": "Low Stock SKU", "value": str(low_stock), "delta": "watch"},
            {"label": "AOV", "value": f"{average_order_value:,} KRW", "delta": "calc"},
        ],
        "highlight_order": highlight_order,
        "watchlist": [product.title for product in products if product.inventory <= 8],
    }


def admin_products_payload(db: Session) -> list[dict[str, object]]:
    products = db.scalars(select(Product).order_by(Product.created_at.asc())).all()
    return [
        {
            **serialize_product(product),
            "stock_state": "low" if product.inventory <= 8 else "stable",
        }
        for product in products
    ]


def admin_orders_payload(db: Session) -> list[dict[str, object]]:
    orders = db.scalars(
        select(Order)
        .options(selectinload(Order.payment_attempts))
        .order_by(Order.created_at.desc())
    ).all()
    return [_serialize_order(order) for order in orders]


def admin_payment_attempts_payload(db: Session) -> list[dict[str, object]]:
    attempts = db.scalars(
        select(PaymentAttempt)
        .options(selectinload(PaymentAttempt.order))
        .order_by(PaymentAttempt.created_at.desc())
    ).all()

    items: list[dict[str, object]] = []
    for attempt in attempts:
        failure_reason = None
        retryable = False
        if attempt.status == PaymentAttemptStatus.FAILED.value:
            failure_reason = "mock_payment_failed"
            retryable = True

        items.append(
            {
                **serialize_payment_attempt(attempt),
                "customer": attempt.order.customer_name,
                "failure_reason": failure_reason,
                "retryable": retryable,
            }
        )

    return items


def build_session_response(user: User) -> dict[str, object]:
    settings = get_settings()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_expire_minutes)
    token = create_access_token(user)
    operator = {
        "email": user.email,
        "name": user.full_name,
        "role": user.role,
        "scopes": (
            ["dashboard:read", "products:read", "orders:read", "payments:read"]
            if user.role == UserRole.ADMIN.value
            else ["catalog:read", "cart:write", "orders:write"]
        ),
    }
    buyer = {
        "id": user.id,
        "email": user.email,
        "name": user.full_name,
        "segment": None,
    }
    return {
        "access_token": token,
        "token": token,
        "token_type": "bearer",
        "expires_at": expires_at.isoformat(),
        "user": serialize_user(user),
        "buyer": buyer,
        "operator": operator,
    }
```

## `server/shared/store.py`

```python
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass


def _seed_products() -> list[dict[str, object]]:
    return [
        {
            "id": "prod_studio_jacket",
            "slug": "studio-jacket",
            "title": "Studio Field Jacket",
            "category": "Outerwear",
            "price": 129000,
            "compare_at_price": 149000,
            "inventory": 12,
            "rating": 4.8,
            "tags": ["Best seller", "Lecture pick"],
            "summary": "도심형 편집숍 무드로 만든 대표 상품 카드 예시.",
        },
        {
            "id": "prod_canvas_bag",
            "slug": "canvas-market-bag",
            "title": "Canvas Market Bag",
            "category": "Accessories",
            "price": 49000,
            "compare_at_price": None,
            "inventory": 8,
            "rating": 4.6,
            "tags": ["Low stock", "Bundle"],
            "summary": "장바구니와 재고 상태를 설명하기 좋은 액세서리 상품.",
        },
        {
            "id": "prod_glass_set",
            "slug": "amber-glass-set",
            "title": "Amber Glass Set",
            "category": "Home",
            "price": 36000,
            "compare_at_price": 42000,
            "inventory": 24,
            "rating": 4.9,
            "tags": ["Home edit", "Giftable"],
            "summary": "프로모션 가격과 compare-at-price를 보여주기 위한 샘플.",
        },
        {
            "id": "prod_desk_lamp",
            "slug": "mono-desk-lamp",
            "title": "Mono Desk Lamp",
            "category": "Lighting",
            "price": 89000,
            "compare_at_price": 109000,
            "inventory": 5,
            "rating": 4.7,
            "tags": ["Almost gone", "Visual focus"],
            "summary": "상세 카드와 admin low-stock 상태를 연결하기 위한 샘플.",
        },
    ]


def _seed_orders() -> list[dict[str, object]]:
    return [
        {
            "id": "ORD-240421-01",
            "customer": "Kim Hana",
            "channel": "Storefront",
            "status": "ready_to_ship",
            "total_amount": 178000,
            "item_count": 2,
        },
        {
            "id": "ORD-240421-02",
            "customer": "Park Jun",
            "channel": "Instagram",
            "status": "payment_pending",
            "total_amount": 49000,
            "item_count": 1,
        },
        {
            "id": "ORD-240421-03",
            "customer": "Lee Seoyeon",
            "channel": "Storefront",
            "status": "delivered",
            "total_amount": 129000,
            "item_count": 1,
        },
    ]


@dataclass
class InMemoryStore:
    products: list[dict[str, object]]
    orders: list[dict[str, object]]
    cart: dict[str, int]

    def reset(self) -> None:
        self.products = deepcopy(_seed_products())
        self.orders = deepcopy(_seed_orders())
        self.cart = {}

    def catalog_payload(self) -> dict[str, object]:
        return {
            "brand": {
                "name": "Edition Lecture",
                "headline": "실전 풀스택 스터디용 이커머스 레퍼런스",
                "subhead": "storefront, admin, api 경계를 한 번에 설명하기 위한 샘플 데이터",
            },
            "collections": [
                "Spring edit",
                "Desk objects",
                "Low stock watchlist",
            ],
            "selling_points": [
                "React storefront",
                "FastAPI backend",
                "Admin operations",
            ],
            "items": self.products,
        }

    def product_detail(self, slug: str) -> dict[str, object] | None:
        for product in self.products:
            if product["slug"] == slug:
                return product
        return None

    def cart_payload(self) -> dict[str, object]:
        items: list[dict[str, object]] = []
        subtotal = 0

        for product in self.products:
            quantity = self.cart.get(str(product["id"]), 0)
            if quantity == 0:
                continue

            line_total = int(product["price"]) * quantity
            subtotal += line_total
            items.append(
                {
                    "product_id": product["id"],
                    "title": product["title"],
                    "quantity": quantity,
                    "unit_price": product["price"],
                    "line_total": line_total,
                }
            )

        shipping_fee = 0 if subtotal >= 150000 or subtotal == 0 else 3500
        return {
            "items": items,
            "item_count": sum(self.cart.values()),
            "subtotal": subtotal,
            "shipping_fee": shipping_fee,
            "total": subtotal + shipping_fee,
            "shipping_policy": "150000원 이상 무료배송",
        }

    def add_cart_item(self, product_id: str, quantity: int) -> dict[str, object]:
        self._ensure_product(product_id)
        self.cart[product_id] = self.cart.get(product_id, 0) + quantity
        return self.cart_payload()

    def update_cart_item(self, product_id: str, quantity: int) -> dict[str, object]:
        self._ensure_product(product_id)
        self.cart[product_id] = quantity
        return self.cart_payload()

    def remove_cart_item(self, product_id: str) -> dict[str, object]:
        self.cart.pop(product_id, None)
        return self.cart_payload()

    def orders_summary_payload(self) -> dict[str, object]:
        return {
            "stages": [
                {"label": "Cart", "value": "active"},
                {"label": "Payment", "value": "next"},
                {"label": "Fulfillment", "value": "watch"},
            ],
            "recent_orders": self.orders[:2],
            "policy_notes": [
                "재고 5개 이하 상품은 admin에서 low stock으로 강조",
                "현재 버전은 주문 생성 대신 주문 요약 read model만 제공",
            ],
        }

    def admin_dashboard_payload(self) -> dict[str, object]:
        gross_revenue = sum(int(order["total_amount"]) for order in self.orders)
        total_orders = len(self.orders)
        low_stock = len([product for product in self.products if int(product["inventory"]) <= 8])
        average_order_value = int(gross_revenue / total_orders) if total_orders else 0

        return {
            "metrics": [
                {"label": "Gross Revenue", "value": f"{gross_revenue:,} KRW", "delta": "+12%"},
                {"label": "Orders", "value": str(total_orders), "delta": "+3"},
                {"label": "Low Stock SKU", "value": str(low_stock), "delta": "watch"},
                {"label": "AOV", "value": f"{average_order_value:,} KRW", "delta": "+4%"},
            ],
            "highlight_order": self.orders[0],
            "watchlist": [
                product["title"]
                for product in self.products
                if int(product["inventory"]) <= 8
            ],
        }

    def admin_products_payload(self) -> list[dict[str, object]]:
        return [
            {
                **product,
                "stock_state": "low" if int(product["inventory"]) <= 8 else "stable",
            }
            for product in self.products
        ]

    def admin_orders_payload(self) -> list[dict[str, object]]:
        return self.orders

    def _ensure_product(self, product_id: str) -> None:
        if not any(product["id"] == product_id for product in self.products):
            raise ValueError(f"unknown product: {product_id}")


_store = InMemoryStore(products=[], orders=[], cart={})
_store.reset()


def get_store() -> InMemoryStore:
    return _store
```

## `server/contexts/__init__.py`

```python
"""Domain context package for the lecture commerce API."""
```

## `server/contexts/catalog/__init__.py`

```python
"""Catalog context placeholder."""
```

## `server/contexts/cart/__init__.py`

```python
"""Cart context placeholder."""
```

## `server/contexts/orders/__init__.py`

```python
"""Orders context placeholder."""
```

## `server/contexts/admin/__init__.py`

```python
"""Admin context placeholder."""
```

## `server/tests/test_api.py`

```python
from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from config import get_settings
from shared.database import dispose_engine


@pytest.fixture()
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Generator[TestClient, None, None]:
    database_path = tmp_path / "lecture-test.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{database_path}")
    monkeypatch.setenv("JWT_SECRET_KEY", "test-secret-key")
    monkeypatch.setenv("BOOTSTRAP_ADMIN_EMAIL", "admin@lecture.test")
    monkeypatch.setenv("BOOTSTRAP_ADMIN_PASSWORD", "AdminPass123!")
    monkeypatch.setenv("BOOTSTRAP_ADMIN_NAME", "Lecture Admin")

    get_settings.cache_clear()
    dispose_engine()

    from api.app import create_app

    with TestClient(create_app()) as test_client:
        yield test_client

    dispose_engine()
    get_settings.cache_clear()


def _register_user(client: TestClient, *, email: str, full_name: str = "Kim Hana") -> dict[str, object]:
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "full_name": full_name,
            "password": "BuyerPass123!",
        },
    )
    assert response.status_code == 201
    return response.json()


def _login(client: TestClient, *, email: str, password: str) -> dict[str, object]:
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )
    assert response.status_code == 200
    return response.json()


def test_health_and_catalog_seed(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "lecture-commerce",
        "persistence": "sqlalchemy",
    }

    info_response = client.get("/api/v1/system/info")
    assert info_response.status_code == 200
    assert info_response.json()["mode"] == "persistent"

    catalog_response = client.get("/api/v1/catalog/products")
    assert catalog_response.status_code == 200
    payload = catalog_response.json()
    assert len(payload["items"]) == 4
    assert payload["items"][0]["slug"] == "studio-jacket"

    detail_response = client.get("/api/v1/catalog/products/studio-jacket")
    assert detail_response.status_code == 200
    assert detail_response.json()["id"] == "prod_studio_jacket"


def test_auth_cart_order_and_payment_flow(client: TestClient) -> None:
    registration = _register_user(client, email="buyer@lecture.test")
    login = _login(client, email="buyer@lecture.test", password="BuyerPass123!")
    token = login["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    unauthorized_cart = client.get("/api/v1/cart")
    assert unauthorized_cart.status_code == 401

    add_response = client.post(
        "/api/v1/cart/items",
        headers=headers,
        json={"product_id": "prod_studio_jacket", "quantity": 1},
    )
    assert add_response.status_code == 200
    assert add_response.json()["item_count"] == 1

    update_response = client.patch(
        "/api/v1/cart/items/prod_studio_jacket",
        headers=headers,
        json={"quantity": 2},
    )
    assert update_response.status_code == 200
    assert update_response.json()["subtotal"] == 258000
    assert update_response.json()["shipping_fee"] == 0

    order_response = client.post(
        "/api/v1/orders",
        headers=headers,
        json={"notes": "Ring the bell"},
    )
    assert order_response.status_code == 201
    order_payload = order_response.json()
    assert order_payload["order"]["status"] == "pending_payment"
    assert order_payload["payment_attempt"]["status"] == "pending"
    assert order_payload["order"]["customer_email"] == registration["user"]["email"]

    cart_response = client.get("/api/v1/cart", headers=headers)
    assert cart_response.status_code == 200
    assert cart_response.json()["item_count"] == 0

    orders_response = client.get("/api/v1/orders", headers=headers)
    assert orders_response.status_code == 200
    assert orders_response.json()["items"][0]["id"] == order_payload["order"]["id"]

    payment_response = client.post(
        "/api/v1/payments/mock/confirm",
        headers=headers,
        json={
            "order_id": order_payload["order"]["id"],
            "success": True,
            "provider_reference": "mock-paid-001",
        },
    )
    assert payment_response.status_code == 200
    assert payment_response.json()["order"]["status"] == "paid"
    assert payment_response.json()["payment_attempt"]["status"] == "confirmed"

    summary_response = client.get("/api/v1/orders/summary", headers=headers)
    assert summary_response.status_code == 200
    assert summary_response.json()["recent_orders"][0]["payment_status"] == "confirmed"


def test_admin_endpoints_require_admin_and_list_orders(client: TestClient) -> None:
    buyer = _register_user(client, email="another-buyer@lecture.test", full_name="Park Jun")
    buyer_headers = {"Authorization": f"Bearer {buyer['access_token']}"}

    client.post(
        "/api/v1/cart/items",
        headers=buyer_headers,
        json={"product_id": "prod_canvas_bag", "quantity": 1},
    )
    order_response = client.post("/api/v1/orders", headers=buyer_headers, json={})
    order_id = order_response.json()["order"]["id"]
    client.post(
        "/api/v1/payments/confirm",
        headers=buyer_headers,
        json={"order_id": order_id, "success": True},
    )

    forbidden_response = client.get("/api/v1/admin/dashboard", headers=buyer_headers)
    assert forbidden_response.status_code == 403

    admin_login = _login(client, email="admin@lecture.test", password="AdminPass123!")
    admin_headers = {"Authorization": f"Bearer {admin_login['access_token']}"}

    admin_session_response = client.post(
        "/api/v1/admin/session",
        json={"email": "admin@lecture.test", "password": "AdminPass123!"},
    )
    assert admin_session_response.status_code == 200
    assert admin_session_response.json()["operator"]["role"] == "admin"

    dashboard_response = client.get("/api/v1/admin/dashboard", headers=admin_headers)
    assert dashboard_response.status_code == 200
    assert dashboard_response.json()["metrics"][0]["label"] == "Gross Revenue"
    assert dashboard_response.json()["highlight_order"]["status"] == "paid"

    products_response = client.get("/api/v1/admin/products", headers=admin_headers)
    assert products_response.status_code == 200
    assert len(products_response.json()["items"]) == 4

    orders_response = client.get("/api/v1/admin/orders", headers=admin_headers)
    assert orders_response.status_code == 200
    assert orders_response.json()["items"][0]["id"] == order_id

    payments_response = client.get("/api/v1/admin/payment-attempts", headers=admin_headers)
    assert payments_response.status_code == 200
    assert payments_response.json()["items"][0]["order_id"] == order_id
```
