---
title: "3. 서버 앱 골격과 공통 모듈"
source_kind: page
source_path: manual-local/lecture/fullstack-study/11-practice-code/03-server-skeleton
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 3. 서버 앱 골격과 공통 모듈
이 페이지는 05장 1절에서 설명한 FastAPI 앱 골격의 실제 코드를 담습니다. 진입점, 앱 생성, 라우터 등록, 설정 로딩, 인증과 데이터베이스 공통 모듈까지가 여기에 있습니다.

05장은 진입점이 단순해야 하는 이유와 공통 모듈을 어디에 둘지를 설명만 하고 코드를 싣지 않습니다. 그 설명이 실제로 어떤 파일 배치로 떨어졌는지를 이 페이지에서 확인합니다. `main.py`는 앱을 띄우는 일만 하고, `api/app.py`가 앱 객체를 만들며, `api/router.py`가 엔드포인트를 모읍니다. `shared/` 아래에는 설정과 무관하게 여러 컨텍스트가 함께 쓰는 인증, 데이터베이스, 모델 정의가 들어갑니다.

# 파일

## `server/main.py`

```python
from api.app import app

__all__ = ["app"]

__all__ = ["app"]
```

## `server/config.py`

```python
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.local", ".env.example"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Lecture Commerce API"
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./data/lecture.db"
    jwt_secret_key: str = "lecture-dev-secret"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 720
    bootstrap_admin_email: str = "admin@lecture.test"
    bootstrap_admin_password: str = "Admin1234!"
    bootstrap_admin_name: str = "Lecture Admin"
    cors_origins: list[str] = Field(
        default_factory=lambda: [
            "http://127.0.0.1:5173",
            "http://localhost:5173",
            "http://127.0.0.1:5174",
            "http://localhost:5174",
        ],
    )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.cors_origins = [origin.rstrip("/") for origin in settings.cors_origins]
    settings.bootstrap_admin_email = settings.bootstrap_admin_email.strip().lower()
    return settings
```

## `server/api/__init__.py`

```python
"""Template server API package."""
```

## `server/api/app.py`

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from config import get_settings
from shared.database import Base, get_session_factory
from shared.service import seed_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    from shared import models as shared_models

    session_factory = get_session_factory()
    _ = shared_models.User
    Base.metadata.create_all(bind=session_factory.kw["bind"])

    session = session_factory()
    try:
        seed_database(session)
    finally:
        session.close()

    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="0.2.0", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": "lecture-commerce",
            "persistence": "sqlalchemy",
        }

    app.include_router(api_router, prefix=settings.api_prefix)
    return app


app = create_app()
```

## `server/api/router.py`

```python
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from shared.auth import get_admin_user, get_current_user
from shared.database import get_db
from shared.models import User
from shared.service import (
    add_cart_item,
    admin_payment_attempts_payload,
    admin_dashboard_payload,
    admin_orders_payload,
    admin_products_payload,
    authenticate_user,
    build_session_response,
    buyer_orders_payload,
    cart_payload,
    catalog_payload,
    confirm_payment,
    create_order_from_cart,
    get_product_by_slug,
    orders_summary_payload,
    register_user,
    remove_cart_item,
    serialize_product,
    update_cart_item,
)


api_router = APIRouter()


class CartItemPayload(BaseModel):
    product_id: str = Field(min_length=1)
    quantity: int = Field(ge=1, le=20)


class CartQuantityPayload(BaseModel):
    quantity: int = Field(ge=1, le=20)


class RegisterPayload(BaseModel):
    email: str = Field(min_length=3, max_length=255)
    full_name: str = Field(min_length=2, max_length=120)
    password: str = Field(min_length=8, max_length=128)


class LoginPayload(BaseModel):
    email: str = Field(min_length=3, max_length=255)
    password: str = Field(min_length=8, max_length=128)


class OrderCreatePayload(BaseModel):
    notes: str | None = Field(default=None, max_length=300)


class PaymentConfirmPayload(BaseModel):
    order_id: str = Field(min_length=1)
    success: bool = True
    provider_reference: str | None = Field(default=None, max_length=120)


@api_router.get("/system/info")
def system_info() -> dict[str, str]:
    return {
        "service": "lecture-commerce",
        "status": "ready",
        "mode": "persistent",
    }


@api_router.get("/catalog/products")
def list_products(db: Session = Depends(get_db)) -> dict[str, object]:
    return catalog_payload(db)


@api_router.get("/catalog/products/{slug}")
def product_detail(slug: str, db: Session = Depends(get_db)) -> dict[str, object]:
    product = get_product_by_slug(db, slug)
    if product is None:
        raise HTTPException(status_code=404, detail="product_not_found")
    return serialize_product(product)


@api_router.post("/auth/register", status_code=status.HTTP_201_CREATED)
def register(payload: RegisterPayload, db: Session = Depends(get_db)) -> dict[str, object]:
    try:
        user = register_user(
            db,
            email=str(payload.email),
            full_name=payload.full_name,
            password=payload.password,
        )
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc

    return build_session_response(user)


@api_router.post("/auth/login")
def login(payload: LoginPayload, db: Session = Depends(get_db)) -> dict[str, object]:
    user = authenticate_user(db, email=str(payload.email), password=payload.password)
    if user is None:
        raise HTTPException(status_code=401, detail="invalid_credentials")

    return build_session_response(user)


@api_router.post("/admin/session")
def admin_session(payload: LoginPayload, db: Session = Depends(get_db)) -> dict[str, object]:
    user = authenticate_user(db, email=str(payload.email), password=payload.password)
    if user is None:
        raise HTTPException(status_code=401, detail="invalid_credentials")
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="admin_access_required")
    return build_session_response(user)


@api_router.get("/cart")
def get_cart(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return cart_payload(db, current_user)


@api_router.post("/cart/items")
def create_cart_item(
    payload: CartItemPayload,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    try:
        return add_cart_item(db, current_user, product_id=payload.product_id, quantity=payload.quantity)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@api_router.patch("/cart/items/{product_id}")
def update_cart_item_quantity(
    product_id: str,
    payload: CartQuantityPayload,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    try:
        return update_cart_item(db, current_user, product_id=product_id, quantity=payload.quantity)
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@api_router.delete("/cart/items/{product_id}")
def delete_cart_item(
    product_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return remove_cart_item(db, current_user, product_id=product_id)


@api_router.get("/orders/summary")
def orders_summary(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return orders_summary_payload(db, current_user)


@api_router.get("/orders")
def list_orders(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return buyer_orders_payload(db, current_user)


@api_router.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(
    payload: OrderCreatePayload,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    try:
        return create_order_from_cart(db, current_user, notes=payload.notes)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@api_router.post("/payments/confirm")
@api_router.post("/payments/mock/confirm")
def confirm_mock_payment(
    payload: PaymentConfirmPayload,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    try:
        return confirm_payment(
            db,
            current_user,
            order_id=payload.order_id,
            success=payload.success,
            provider_reference=payload.provider_reference,
        )
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@api_router.get("/admin/dashboard")
def admin_dashboard(
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return admin_dashboard_payload(db)


@api_router.get("/admin/products")
def admin_products(
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return {"items": admin_products_payload(db)}


@api_router.get("/admin/orders")
def admin_orders(
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return {"items": admin_orders_payload(db)}


@api_router.get("/admin/payment-attempts")
def admin_payment_attempts(
    _: User = Depends(get_admin_user),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    return {"items": admin_payment_attempts_payload(db)}
```

## `server/shared/__init__.py`

```python
from .store import get_store

__all__ = ["get_store"]
```

## `server/shared/auth.py`

```python
from __future__ import annotations

import hashlib
import hmac
import secrets
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from config import get_settings
from shared.database import get_db
from shared.models import User, UserRole


bearer_scheme = HTTPBearer(auto_error=False)


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    derived = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 120_000)
    return f"{salt}${derived.hex()}"


def verify_password(password: str, password_hash: str) -> bool:
    try:
        salt, expected_hash = password_hash.split("$", maxsplit=1)
    except ValueError:
        return False

    derived = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 120_000)
    return hmac.compare_digest(expected_hash, derived.hex())


def create_access_token(user: User) -> str:
    settings = get_settings()
    issued_at = datetime.now(timezone.utc)
    payload = {
        "sub": user.id,
        "email": user.email,
        "role": user.role,
        "iat": int(issued_at.timestamp()),
        "exp": int((issued_at + timedelta(minutes=settings.jwt_expire_minutes)).timestamp()),
    }
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def _decode_token(token: str) -> dict[str, object]:
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except jwt.PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid_token",
        ) from exc
    return payload


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="authentication_required")

    payload = _decode_token(credentials.credentials)
    user_id = payload.get("sub")
    if not isinstance(user_id, str):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid_token")

    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="user_not_found")
    return user


def get_admin_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != UserRole.ADMIN.value:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="admin_access_required")
    return current_user
```

## `server/shared/database.py`

```python
from __future__ import annotations

from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.pool import StaticPool

from config import get_settings


class Base(DeclarativeBase):
    pass


_engine = None
_session_factory: sessionmaker[Session] | None = None


def _ensure_sqlite_directory(database_url: str) -> None:
    if not database_url.startswith("sqlite:///"):
        return

    sqlite_path = database_url.removeprefix("sqlite:///")
    if sqlite_path == ":memory:":
        return

    file_path = Path(sqlite_path)
    if not file_path.is_absolute():
        file_path = Path.cwd() / file_path
    file_path.parent.mkdir(parents=True, exist_ok=True)


def get_engine():
    global _engine

    if _engine is not None:
        return _engine

    settings = get_settings()
    database_url = settings.database_url
    _ensure_sqlite_directory(database_url)

    engine_kwargs: dict[str, object] = {}
    if database_url.startswith("sqlite"):
        engine_kwargs["connect_args"] = {"check_same_thread": False}
        if database_url.endswith(":memory:"):
            engine_kwargs["poolclass"] = StaticPool

    _engine = create_engine(database_url, **engine_kwargs)
    return _engine


def get_session_factory() -> sessionmaker[Session]:
    global _session_factory

    if _session_factory is None:
        _session_factory = sessionmaker(
            bind=get_engine(),
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
    return _session_factory


def get_db() -> Generator[Session, None, None]:
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()


def dispose_engine() -> None:
    global _engine, _session_factory

    if _engine is not None:
        _engine.dispose()

    _engine = None
    _session_factory = None
```

## `server/shared/models.py`

```python
from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from uuid import uuid4

from sqlalchemy import JSON, DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.database import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class UserRole(StrEnum):
    CUSTOMER = "customer"
    ADMIN = "admin"


class OrderStatus(StrEnum):
    PENDING_PAYMENT = "pending_payment"
    PAID = "paid"
    PAYMENT_FAILED = "payment_failed"


class PaymentAttemptStatus(StrEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    FAILED = "failed"


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String(120))
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), default=UserRole.CUSTOMER.value)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    cart_items: Mapped[list["CartItem"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    orders: Mapped[list["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(160))
    category: Mapped[str] = mapped_column(String(80))
    price: Mapped[int] = mapped_column(Integer)
    compare_at_price: Mapped[int | None] = mapped_column(Integer, nullable=True)
    inventory: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column()
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)
    summary: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    cart_items: Mapped[list["CartItem"]] = relationship(back_populates="product")


class CartItem(Base):
    __tablename__ = "cart_items"
    __table_args__ = (UniqueConstraint("user_id", "product_id", name="uq_cart_items_user_product"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), index=True)
    quantity: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    user: Mapped[User] = relationship(back_populates="cart_items")
    product: Mapped[Product] = relationship(back_populates="cart_items")


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    customer_name: Mapped[str] = mapped_column(String(120))
    customer_email: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(32), default=OrderStatus.PENDING_PAYMENT.value)
    payment_status: Mapped[str] = mapped_column(String(32), default=PaymentAttemptStatus.PENDING.value)
    channel: Mapped[str] = mapped_column(String(32), default="Storefront")
    subtotal: Mapped[int] = mapped_column(Integer)
    shipping_fee: Mapped[int] = mapped_column(Integer)
    total_amount: Mapped[int] = mapped_column(Integer)
    item_count: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    order_lines: Mapped[list[dict[str, object]]] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    user: Mapped[User] = relationship(back_populates="orders")
    payment_attempts: Mapped[list["PaymentAttempt"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
        order_by="PaymentAttempt.created_at",
    )


class PaymentAttempt(Base):
    __tablename__ = "payment_attempts"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), index=True)
    provider: Mapped[str] = mapped_column(String(40), default="mock")
    status: Mapped[str] = mapped_column(String(32), default=PaymentAttemptStatus.PENDING.value)
    amount: Mapped[int] = mapped_column(Integer)
    provider_reference: Mapped[str | None] = mapped_column(String(120), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    confirmed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    order: Mapped[Order] = relationship(back_populates="payment_attempts")
```
