---
title: "5. Storefront 프론트 코드"
source_kind: page
source_path: manual-local/lecture/fullstack-study/11-practice-code/05-storefront
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 5. Storefront 프론트 코드
이 페이지는 구매자용 storefront 앱의 전체 코드를 담습니다. 03장 2절에서 기획한 구매자 화면과 06장, 07장에서 구현한 상품 조회, 장바구니, 주문 흐름이 실제 React 코드로 어떻게 나타났는지 확인합니다.

`src/app/App.tsx`가 화면 전환과 상태를 모두 쥐고 있고, `src/lib/api.ts`가 서버 API 호출을 한곳에 모읍니다. 05장 3절에서 맞춘 공통 API 계약이 이 파일에서 타입으로 굳어집니다. `src/styles/main.css`는 화면 기획에서 정한 레이아웃을 그대로 옮긴 스타일입니다.

# 파일

## `client/storefront/index.html`

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lecture Storefront</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
  </html>
```

## `client/storefront/package.json`

```json
{
  "name": "lecture-storefront",
  "private": true,
  "version": "0.1.0",
  "packageManager": "pnpm@10.32.1",
  "type": "module",
  "scripts": {
    "dev": "vite --host 0.0.0.0 --port 5173",
    "build": "tsc -b && vite build",
    "preview": "vite preview --host 0.0.0.0 --port 4173"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.30.1"
  },
  "devDependencies": {
    "@playwright/test": "^1.58.2",
    "@types/node": "^25.3.3",
    "@types/react": "^18.3.18",
    "@types/react-dom": "^18.3.5",
    "@vitejs/plugin-react": "^4.7.0",
    "pixelmatch": "^7.1.0",
    "pngjs": "^7.0.0",
    "typescript": "^5.8.3",
    "vite": "^5.4.19",
    "yaml": "^2.8.1"
  }
}
```

## `client/storefront/tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    },
    "strict": true,
    "moduleResolution": "Bundler",
    "noEmit": true,
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "types": ["vite/client"]
  },
  "include": ["src"]
}
```

## `client/storefront/vite.config.ts`

```ts
import path from "node:path";

import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

const rootDir = __dirname;
const resolveFromRoot = (...segments: string[]) => path.resolve(rootDir, ...segments);

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      react: resolveFromRoot("node_modules/react"),
      "react-dom": resolveFromRoot("node_modules/react-dom"),
      "react/jsx-runtime": resolveFromRoot("node_modules/react/jsx-runtime.js"),
      "react/jsx-dev-runtime": resolveFromRoot("node_modules/react/jsx-dev-runtime.js"),
    },
    dedupe: ["react", "react-dom"],
  },
  server: {
    host: "0.0.0.0",
    port: 5173,
    allowedHosts: ["localhost", "127.0.0.1"],
    proxy: {
      "/api/v1": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
    },
  },
  preview: {
    host: "0.0.0.0",
    port: 4173,
  },
});
```

## `client/storefront/src/main.tsx`

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from "./app/App";
import "./styles/main.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
);
```

## `client/storefront/src/app/App.tsx`

```tsx
import { type FormEvent, useEffect, useState } from "react";

import {
  ApiError,
  addCartItem,
  clearBuyerSession,
  confirmMockPayment,
  createOrder,
  fetchCart,
  fetchCatalog,
  fetchOrders,
  loginBuyer,
  readBuyerSession,
  registerBuyer,
  removeCartItem,
  updateCartItem,
  type BuyerOrder,
  type BuyerSession,
  type Cart,
  type CatalogResponse,
  type Product,
} from "@/lib/api";

type AuthMode = "login" | "register";

type AuthFormState = {
  name: string;
  email: string;
  password: string;
};

const currencyFormatter = new Intl.NumberFormat("ko-KR");
const dateFormatter = new Intl.DateTimeFormat("ko-KR", {
  month: "short",
  day: "numeric",
  hour: "2-digit",
  minute: "2-digit",
});

const initialAuthForm: AuthFormState = {
  name: "",
  email: "",
  password: "",
};

function formatCurrency(value: number) {
  return `${currencyFormatter.format(value)}원`;
}

function formatOrderTimestamp(value?: string | null) {
  if (!value) {
    return "방금 업데이트";
  }

  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) {
    return value;
  }

  return dateFormatter.format(parsed);
}

function messageFromError(error: unknown) {
  if (error instanceof ApiError) {
    return error.detail;
  }

  return error instanceof Error ? error.message : "unexpected_error";
}

function isPendingPayment(order: BuyerOrder) {
  const paymentStatus = order.payment_status.toLowerCase();
  const orderStatus = order.status.toLowerCase();

  return (
    paymentStatus !== "paid" &&
    paymentStatus !== "confirmed" &&
    orderStatus !== "paid" &&
    orderStatus !== "ready_to_ship"
  );
}

function getActionableOrder(orders: BuyerOrder[]) {
  return orders.find((order) => isPendingPayment(order)) ?? null;
}

export default function App() {
  const [authMode, setAuthMode] = useState<AuthMode>("login");
  const [authForm, setAuthForm] = useState<AuthFormState>(initialAuthForm);
  const [buyerSession, setBuyerSession] = useState<BuyerSession | null>(() => readBuyerSession());
  const [catalog, setCatalog] = useState<CatalogResponse | null>(null);
  const [cart, setCart] = useState<Cart | null>(null);
  const [orders, setOrders] = useState<BuyerOrder[]>([]);
  const [checkoutNote, setCheckoutNote] = useState("");
  const [statusMessage, setStatusMessage] = useState<string | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isCatalogLoading, setCatalogLoading] = useState(true);
  const [isBuyerDataLoading, setBuyerDataLoading] = useState(false);
  const [isAuthSubmitting, setAuthSubmitting] = useState(false);
  const [pendingProductId, setPendingProductId] = useState<string | null>(null);
  const [isCreatingOrder, setCreatingOrder] = useState(false);
  const [isConfirmingPayment, setConfirmingPayment] = useState(false);

  const actionableOrder = getActionableOrder(orders);
  const paidOrders = orders.filter((order) => !isPendingPayment(order)).length;
  const totalOrderVolume = orders.reduce((sum, order) => sum + order.total_amount, 0);

  useEffect(() => {
    void refreshSurface(readBuyerSession());
  }, []);

  async function refreshSurface(session: BuyerSession | null) {
    setErrorMessage(null);
    setCatalogLoading(true);
    setBuyerDataLoading(Boolean(session));

    try {
      if (!session) {
        const catalogPayload = await fetchCatalog();
        setCatalog(catalogPayload);
        setCart(null);
        setOrders([]);
        return;
      }

      const [catalogPayload, cartPayload, ordersPayload] = await Promise.all([
        fetchCatalog(),
        fetchCart(session.accessToken),
        fetchOrders(session.accessToken),
      ]);

      setCatalog(catalogPayload);
      setCart(cartPayload);
      setOrders(ordersPayload.items);
    } catch (error) {
      if (error instanceof ApiError && (error.status === 401 || error.status === 403)) {
        clearBuyerSession();
        setBuyerSession(null);
        setCart(null);
        setOrders([]);
      }

      setErrorMessage(messageFromError(error));
    } finally {
      setCatalogLoading(false);
      setBuyerDataLoading(false);
    }
  }

  function updateAuthField(field: keyof AuthFormState, value: string) {
    setAuthForm((current) => ({
      ...current,
      [field]: value,
    }));
  }

  async function handleAuthSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setErrorMessage(null);
    setStatusMessage(null);
    setAuthSubmitting(true);

    try {
      const nextSession =
        authMode === "register"
          ? await registerBuyer({
              name: authForm.name.trim(),
              email: authForm.email.trim(),
              password: authForm.password,
            })
          : await loginBuyer({
              email: authForm.email.trim(),
              password: authForm.password,
            });

      setBuyerSession(nextSession);
      setAuthForm(initialAuthForm);
      setStatusMessage(
        authMode === "register"
          ? "계정이 생성되었습니다. 장바구니와 주문 흐름을 바로 이어서 확인할 수 있습니다."
          : "로그인되었습니다. 개인 cart와 주문 read model을 불러옵니다.",
      );
      await refreshSurface(nextSession);
    } catch (error) {
      setErrorMessage(messageFromError(error));
    } finally {
      setAuthSubmitting(false);
    }
  }

  function handleLogout() {
    clearBuyerSession();
    setBuyerSession(null);
    setCart(null);
    setOrders([]);
    setCheckoutNote("");
    setStatusMessage("로그아웃되었습니다. 상품은 계속 둘러볼 수 있고 checkout은 다시 로그인 후 가능합니다.");
    setErrorMessage(null);
  }

  async function handleAddToCart(product: Product) {
    if (!buyerSession) {
      setStatusMessage("장바구니와 checkout은 로그인 후 활성화됩니다.");
      document.getElementById("buyer-auth")?.scrollIntoView({ behavior: "smooth", block: "start" });
      return;
    }

    setErrorMessage(null);
    setStatusMessage(null);
    setPendingProductId(product.id);

    try {
      const nextCart = await addCartItem(buyerSession.accessToken, product.id, 1);
      setCart(nextCart);
      setStatusMessage(`${product.title}을(를) 장바구니에 담았습니다.`);
    } catch (error) {
      setErrorMessage(messageFromError(error));
    } finally {
      setPendingProductId(null);
    }
  }

  async function handleQuantityChange(productId: string, quantity: number) {
    if (!buyerSession) {
      return;
    }

    setErrorMessage(null);
    setPendingProductId(productId);

    try {
      const nextCart =
        quantity <= 0
          ? await removeCartItem(buyerSession.accessToken, productId)
          : await updateCartItem(buyerSession.accessToken, productId, quantity);
      setCart(nextCart);
    } catch (error) {
      setErrorMessage(messageFromError(error));
    } finally {
      setPendingProductId(null);
    }
  }

  async function handleCreateOrder() {
    if (!buyerSession || !cart?.items.length) {
      return;
    }

    setCreatingOrder(true);
    setErrorMessage(null);
    setStatusMessage(null);

    try {
      const response = await createOrder(buyerSession.accessToken, {
        note: checkoutNote.trim() || undefined,
      });
      const [nextCart, nextOrders] = await Promise.all([
        fetchCart(buyerSession.accessToken),
        fetchOrders(buyerSession.accessToken),
      ]);

      setCart(nextCart);
      setOrders(nextOrders.items);
      setCheckoutNote("");
      setStatusMessage(
        `${response.order.id} 주문을 생성했습니다. 이제 mock payment confirmation으로 다음 상태를 확인할 수 있습니다.`,
      );
    } catch (error) {
      setErrorMessage(messageFromError(error));
    } finally {
      setCreatingOrder(false);
    }
  }

  async function handleConfirmPayment() {
    if (!buyerSession || !actionableOrder) {
      return;
    }

    setConfirmingPayment(true);
    setErrorMessage(null);
    setStatusMessage(null);

    try {
      const response = await confirmMockPayment(buyerSession.accessToken, actionableOrder.id);
      const nextOrders = await fetchOrders(buyerSession.accessToken);
      setOrders(nextOrders.items);
      setStatusMessage(
        `${response.order.id} 결제 mock confirmation이 반영되었습니다. 주문 read model을 최신 상태로 갱신했습니다.`,
      );
    } catch (error) {
      setErrorMessage(messageFromError(error));
    } finally {
      setConfirmingPayment(false);
    }
  }

  return (
    <div className="shell">
      <header className="topbar">
        <div className="brand-block">
          <p className="eyebrow">Edition Lecture Store</p>
          <h1>buyer auth와 checkout을 붙인 storefront 정본</h1>
          <p className="lede">
            상품은 먼저 둘러보고, buyer 계정으로 로그인하면 개인 cart, 주문 생성, mock payment
            confirmation까지 한 화면에서 이어집니다.
          </p>
        </div>

        <nav className="topnav">
          <a href="#products">Products</a>
          <a href="#cart">Cart</a>
          <a href="#checkout">Checkout</a>
          <a href="#orders">Orders</a>
          <a href="http://127.0.0.1:5174" target="_blank" rel="noreferrer">
            Admin
          </a>
        </nav>
      </header>

      <main className="layout">
        <section className="hero card">
          <div className="hero-copy">
            <p className="eyebrow">Storefront Flow</p>
            <h2>{catalog?.brand.headline ?? "storefront surface를 준비하는 중"}</h2>
            <p>{catalog?.brand.subhead ?? "catalog, buyer auth, cart, order, payment mock을 연결합니다."}</p>
            <div className="pill-row">
              {(catalog?.collections ?? ["Buyer login", "Cart snapshot", "Payment mock"]).map(
                (collection) => (
                  <span key={collection} className="pill">
                    {collection}
                  </span>
                ),
              )}
            </div>
          </div>

          <div className="hero-aside">
            <p className="hero-panel-label">Session Signal</p>
            <strong>{buyerSession ? buyerSession.buyer.name : "Guest buyer"}</strong>
            <p>{buyerSession ? buyerSession.buyer.email : "로그인 전에는 browse-only mode로 동작합니다."}</p>
            <dl className="hero-metrics">
              <div>
                <dt>Catalog</dt>
                <dd>{catalog?.items.length ?? 0} SKU</dd>
              </div>
              <div>
                <dt>Cart</dt>
                <dd>{cart?.item_count ?? 0} items</dd>
              </div>
              <div>
                <dt>Orders</dt>
                <dd>{orders.length}</dd>
              </div>
              <div>
                <dt>Paid</dt>
                <dd>{paidOrders}</dd>
              </div>
            </dl>
          </div>
        </section>

        {errorMessage ? <p className="banner banner-error">{errorMessage}</p> : null}
        {statusMessage ? <p className="banner banner-status">{statusMessage}</p> : null}

        <section className="feature-grid">
          <section id="buyer-auth" className="card auth-panel">
            <div className="section-heading">
              <div>
                <p className="eyebrow">Buyer Access</p>
                <h2>{buyerSession ? "현재 buyer 세션" : "로그인 또는 회원가입"}</h2>
              </div>
              <span className={`auth-chip ${buyerSession ? "auth-chip-live" : ""}`}>
                {buyerSession ? "authenticated" : "guest"}
              </span>
            </div>

            {buyerSession ? (
              <div className="session-card">
                <div>
                  <p className="session-label">Signed in as</p>
                  <strong>{buyerSession.buyer.name}</strong>
                  <p>{buyerSession.buyer.email}</p>
                </div>
                <ul className="benefit-list">
                  <li>buyer 단위 cart 조회</li>
                  <li>주문 생성 후 payment mock 진행</li>
                  <li>최근 order read model 확인</li>
                </ul>
                <button type="button" className="secondary-button" onClick={handleLogout}>
                  로그아웃
                </button>
              </div>
            ) : (
              <>
                <div className="auth-toggle">
                  <button
                    type="button"
                    className={authMode === "login" ? "is-active" : ""}
                    onClick={() => setAuthMode("login")}
                  >
                    Login
                  </button>
                  <button
                    type="button"
                    className={authMode === "register" ? "is-active" : ""}
                    onClick={() => setAuthMode("register")}
                  >
                    Register
                  </button>
                </div>

                <form className="auth-form" onSubmit={handleAuthSubmit}>
                  {authMode === "register" ? (
                    <label>
                      <span>Name</span>
                      <input
                        type="text"
                        value={authForm.name}
                        onChange={(event) => updateAuthField("name", event.target.value)}
                        placeholder="Kim Hana"
                        required
                      />
                    </label>
                  ) : null}
                  <label>
                    <span>Email</span>
                    <input
                      type="email"
                      value={authForm.email}
                      onChange={(event) => updateAuthField("email", event.target.value)}
                      placeholder="buyer@example.com"
                      required
                    />
                  </label>
                  <label>
                    <span>Password</span>
                    <input
                      type="password"
                      value={authForm.password}
                      onChange={(event) => updateAuthField("password", event.target.value)}
                      placeholder="8자 이상 비밀번호"
                      minLength={8}
                      required
                    />
                  </label>
                  <button type="submit" className="primary-button" disabled={isAuthSubmitting}>
                    {isAuthSubmitting
                      ? "요청 중..."
                      : authMode === "register"
                        ? "계정 만들기"
                        : "로그인"}
                  </button>
                </form>
              </>
            )}
          </section>

          <section className="card pulse-panel">
            <div className="section-heading">
              <div>
                <p className="eyebrow">Flow Snapshot</p>
                <h2>checkout rhythm</h2>
              </div>
            </div>

            <div className="stage-grid">
              <article className="stage-card">
                <span>01</span>
                <strong>Browse</strong>
                <p>{catalog?.selling_points[0] ?? "catalog API로 상품을 노출합니다."}</p>
              </article>
              <article className="stage-card">
                <span>02</span>
                <strong>Order</strong>
                <p>{cart?.item_count ? `${cart.item_count}개 상품이 cart에 있습니다.` : "로그인 후 cart mutation이 열립니다."}</p>
              </article>
              <article className="stage-card accent-card">
                <span>03</span>
                <strong>Confirm</strong>
                <p>
                  {actionableOrder
                    ? `${actionableOrder.id} 결제 확인 대기`
                    : "주문 생성 후 mock payment confirmation을 진행합니다."}
                </p>
              </article>
            </div>

            <div className="stat-row">
              <div>
                <small>Order Volume</small>
                <strong>{formatCurrency(totalOrderVolume)}</strong>
              </div>
              <div>
                <small>Buyer Data</small>
                <strong>{isBuyerDataLoading ? "syncing" : buyerSession ? "live" : "locked"}</strong>
              </div>
            </div>
          </section>
        </section>

        <section id="products" className="catalog-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Catalog</p>
              <h2>상품 목록은 API에서 바로 읽고 cart mutation만 buyer 세션에 묶습니다.</h2>
            </div>
            <div className="chip-row">
              {(catalog?.selling_points ?? ["React storefront", "Typed API client", "Mock payment"]).map(
                (point) => (
                  <span key={point} className="chip">
                    {point}
                  </span>
                ),
              )}
            </div>
          </div>

          <div className="product-grid">
            {(catalog?.items ?? []).map((product) => (
              <article key={product.id} className="product-card card">
                <div className="product-meta">
                  <span>{product.category}</span>
                  <span>★ {product.rating.toFixed(1)}</span>
                </div>
                <h3>{product.title}</h3>
                <p className="summary">{product.summary}</p>
                <div className="tag-row">
                  {product.tags.map((tag) => (
                    <span key={tag} className="tag">
                      {tag}
                    </span>
                  ))}
                </div>
                <div className="price-row">
                  <strong>{formatCurrency(product.price)}</strong>
                  {product.compare_at_price ? (
                    <span>{formatCurrency(product.compare_at_price)}</span>
                  ) : null}
                </div>
                <div className="product-footer">
                  <small>재고 {product.inventory}개</small>
                  <button
                    type="button"
                    className="primary-button"
                    onClick={() => void handleAddToCart(product)}
                    disabled={pendingProductId === product.id || isCatalogLoading}
                  >
                    {pendingProductId === product.id ? "추가 중..." : "Add to cart"}
                  </button>
                </div>
              </article>
            ))}

            {!catalog?.items.length && !isCatalogLoading ? (
              <article className="card empty-card">
                <p className="eyebrow">No Products</p>
                <h3>카탈로그 응답이 비어 있습니다.</h3>
                <p>backend seed 또는 `/catalog/products` 응답 형식을 확인해야 합니다.</p>
              </article>
            ) : null}
          </div>
        </section>

        <section className="checkout-grid">
          <section id="cart" className="card cart-panel">
            <div className="section-heading">
              <div>
                <p className="eyebrow">Cart</p>
                <h2>buyer별 cart snapshot</h2>
              </div>
              <strong>{cart?.item_count ?? 0} items</strong>
            </div>

            {buyerSession ? (
              <>
                <div className="cart-list">
                  {cart?.items.length ? (
                    cart.items.map((item) => (
                      <article key={item.product_id} className="cart-item">
                        <div>
                          <strong>{item.title}</strong>
                          <p>{formatCurrency(item.line_total)}</p>
                        </div>
                        <div className="qty-controls">
                          <button
                            type="button"
                            onClick={() => void handleQuantityChange(item.product_id, item.quantity - 1)}
                            disabled={pendingProductId === item.product_id}
                          >
                            -
                          </button>
                          <span>{item.quantity}</span>
                          <button
                            type="button"
                            onClick={() => void handleQuantityChange(item.product_id, item.quantity + 1)}
                            disabled={pendingProductId === item.product_id}
                          >
                            +
                          </button>
                        </div>
                      </article>
                    ))
                  ) : (
                    <p className="empty-state">
                      아직 담긴 상품이 없습니다. 상품 카드에서 cart에 담은 뒤 주문 흐름을 이어가세요.
                    </p>
                  )}
                </div>

                <dl className="totals">
                  <div>
                    <dt>Subtotal</dt>
                    <dd>{formatCurrency(cart?.subtotal ?? 0)}</dd>
                  </div>
                  <div>
                    <dt>Shipping</dt>
                    <dd>{formatCurrency(cart?.shipping_fee ?? 0)}</dd>
                  </div>
                  <div className="total-row">
                    <dt>Total</dt>
                    <dd>{formatCurrency(cart?.total ?? 0)}</dd>
                  </div>
                </dl>
                <p className="policy">{cart?.shipping_policy ?? "배송 정책을 준비 중입니다."}</p>
              </>
            ) : (
              <p className="empty-state">guest 모드에서는 상품만 조회할 수 있습니다. 주문 전 로그인이 필요합니다.</p>
            )}
          </section>

          <section id="checkout" className="card checkout-panel">
            <div className="section-heading">
              <div>
                <p className="eyebrow">Checkout</p>
                <h2>order create + payment mock</h2>
              </div>
            </div>

            {buyerSession ? (
              <>
                <label className="note-field">
                  <span>Order note</span>
                  <textarea
                    rows={4}
                    value={checkoutNote}
                    onChange={(event) => setCheckoutNote(event.target.value)}
                    placeholder="문 앞에 놓아 주세요 / 강의용 데모 주문 메모"
                  />
                </label>

                <button
                  type="button"
                  className="primary-button"
                  onClick={() => void handleCreateOrder()}
                  disabled={isCreatingOrder || !cart?.items.length}
                >
                  {isCreatingOrder ? "주문 생성 중..." : "Create order from cart"}
                </button>

                <div className="payment-callout">
                  <div>
                    <p className="callout-label">Mock Payment</p>
                    <strong>{actionableOrder?.id ?? "대기 중인 주문 없음"}</strong>
                    <p>
                      {actionableOrder?.payment_attempt
                        ? `${actionableOrder.payment_attempt.provider} · ${actionableOrder.payment_attempt.status}`
                        : "주문 생성 후 payment attempt가 여기에 표시됩니다."}
                    </p>
                  </div>
                  <button
                    type="button"
                    className="secondary-button"
                    onClick={() => void handleConfirmPayment()}
                    disabled={isConfirmingPayment || !actionableOrder}
                  >
                    {isConfirmingPayment ? "확인 중..." : "Confirm mock payment"}
                  </button>
                </div>
              </>
            ) : (
              <p className="empty-state">
                checkout panel은 인증된 buyer 세션에서만 열립니다. 먼저 계정을 만들거나 로그인하세요.
              </p>
            )}
          </section>
        </section>

        <section id="orders" className="card orders-panel">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Orders</p>
              <h2>buyer read model preview</h2>
            </div>
            <span className="muted-copy">{isBuyerDataLoading ? "syncing..." : `${orders.length} records`}</span>
          </div>

          {buyerSession ? (
            <div className="orders-list">
              {orders.length ? (
                orders.map((order) => (
                  <article key={order.id} className="order-card">
                    <div className="order-head">
                      <div>
                        <strong>{order.id}</strong>
                        <p>{formatOrderTimestamp(order.created_at)}</p>
                      </div>
                      <div className="order-meta">
                        <span className={`status-badge status-${isPendingPayment(order) ? "pending" : "paid"}`}>
                          {order.payment_status}
                        </span>
                        <strong>{formatCurrency(order.total_amount)}</strong>
                      </div>
                    </div>

                    <div className="order-body">
                      <p>{order.item_count}개 상품 · {order.status}</p>
                      {order.note ? <p className="order-note">{order.note}</p> : null}
                    </div>
                  </article>
                ))
              ) : (
                <p className="empty-state">아직 생성된 주문이 없습니다. cart에서 주문을 만들어 read model을 채우세요.</p>
              )}
            </div>
          ) : (
            <p className="empty-state">로그인 후 buyer별 order history를 조회할 수 있습니다.</p>
          )}
        </section>
      </main>
    </div>
  );
}
```

## `client/storefront/src/lib/api.ts`

```ts
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? "/api/v1";
const buyerSessionStorageKey = "lecture.storefront.buyer-session";

export class ApiError extends Error {
  status: number;

  detail: string;

  constructor(status: number, detail: string) {
    super(detail);
    this.name = "ApiError";
    this.status = status;
    this.detail = detail;
  }
}

export type BuyerProfile = {
  id: string;
  name: string;
  email: string;
  segment?: string | null;
};

export type BuyerSession = {
  buyer: BuyerProfile;
  accessToken: string;
  tokenType: string;
};

export type LoginPayload = {
  email: string;
  password: string;
};

export type RegisterPayload = {
  name: string;
  email: string;
  password: string;
};

export type Product = {
  id: string;
  slug: string;
  title: string;
  category: string;
  price: number;
  compare_at_price: number | null;
  inventory: number;
  rating: number;
  tags: string[];
  summary: string;
};

export type CatalogResponse = {
  brand: {
    name: string;
    headline: string;
    subhead: string;
  };
  collections: string[];
  selling_points: string[];
  items: Product[];
};

export type CartItem = {
  product_id: string;
  title: string;
  quantity: number;
  unit_price: number;
  line_total: number;
};

export type Cart = {
  items: CartItem[];
  item_count: number;
  subtotal: number;
  shipping_fee: number;
  total: number;
  shipping_policy: string;
};

export type PaymentAttempt = {
  id: string;
  status: string;
  provider: string;
  amount: number;
  reference?: string | null;
  confirmed_at?: string | null;
};

export type BuyerOrder = {
  id: string;
  status: string;
  payment_status: string;
  total_amount: number;
  item_count: number;
  created_at?: string | null;
  note?: string | null;
  items: CartItem[];
  payment_attempt: PaymentAttempt | null;
};

export type OrdersResponse = {
  items: BuyerOrder[];
};

export type CreateOrderPayload = {
  note?: string;
};

export type CreateOrderResponse = {
  order: BuyerOrder;
  payment_attempt: PaymentAttempt | null;
};

export type ConfirmPaymentResponse = {
  order: BuyerOrder;
  payment_attempt: PaymentAttempt | null;
};

type RequestOptions = RequestInit & {
  token?: string | null;
};

type AuthResponse = {
  buyer: BuyerProfile;
  user?: BuyerProfile & { full_name?: string };
  access_token?: string;
  token?: string;
  token_type?: string;
};

function toRecord(value: unknown): Record<string, unknown> {
  return typeof value === "object" && value !== null ? (value as Record<string, unknown>) : {};
}

function toStringValue(value: unknown, fallback = "") {
  return typeof value === "string" ? value : fallback;
}

function toNumberValue(value: unknown, fallback = 0) {
  return typeof value === "number" && Number.isFinite(value) ? value : fallback;
}

function normalizeCartItem(input: unknown): CartItem {
  const record = toRecord(input);
  return {
    product_id: toStringValue(record.product_id ?? record.productId),
    title: toStringValue(record.title),
    quantity: toNumberValue(record.quantity),
    unit_price: toNumberValue(record.unit_price ?? record.unitPrice ?? record.price),
    line_total: toNumberValue(record.line_total ?? record.lineTotal ?? record.total),
  };
}

function normalizeCart(input: unknown): Cart {
  const record = toRecord(input);
  const items = Array.isArray(record.items) ? record.items.map(normalizeCartItem) : [];
  return {
    items,
    item_count: toNumberValue(record.item_count ?? record.itemCount, items.length),
    subtotal: toNumberValue(record.subtotal),
    shipping_fee: toNumberValue(record.shipping_fee ?? record.shippingFee),
    total: toNumberValue(record.total),
    shipping_policy: toStringValue(record.shipping_policy ?? record.shippingPolicy, "배송 정책 정보를 준비 중입니다."),
  };
}

function normalizePaymentAttempt(input: unknown): PaymentAttempt | null {
  if (!input) {
    return null;
  }

  const record = toRecord(input);
  return {
    id: toStringValue(record.id ?? record.payment_attempt_id),
    status: toStringValue(record.status, "pending"),
    provider: toStringValue(record.provider, "mock"),
    amount: toNumberValue(record.amount ?? record.total_amount ?? record.total),
    reference: toStringValue(record.reference ?? record.confirmation_code ?? record.pg_reference) || null,
    confirmed_at: toStringValue(record.confirmed_at ?? record.confirmedAt) || null,
  };
}

function normalizeOrder(input: unknown): BuyerOrder {
  const record = toRecord(input);
  const rawItems = Array.isArray(record.items)
    ? record.items
    : Array.isArray(record.line_items)
      ? record.line_items
      : [];
  const items = rawItems.map(normalizeCartItem);
  const paymentAttempt = normalizePaymentAttempt(
    record.payment_attempt ?? record.latest_payment_attempt ?? record.paymentAttempt ?? record.payment,
  );

  return {
    id: toStringValue(record.id),
    status: toStringValue(record.status, "draft"),
    payment_status: toStringValue(
      record.payment_status ?? paymentAttempt?.status,
      paymentAttempt ? paymentAttempt.status : "pending",
    ),
    total_amount: toNumberValue(record.total_amount ?? record.total),
    item_count: toNumberValue(record.item_count ?? record.itemCount, items.length),
    created_at: toStringValue(record.created_at ?? record.createdAt) || null,
    note: toStringValue(record.note ?? record.notes) || null,
    items,
    payment_attempt: paymentAttempt,
  };
}

function normalizeSession(input: AuthResponse | BuyerSession): BuyerSession {
  if ("accessToken" in input) {
    return input;
  }

  const buyer = input.buyer ?? {
    id: toStringValue(toRecord(input.user).id),
    email: toStringValue(toRecord(input.user).email),
    name: toStringValue(toRecord(input.user).name ?? toRecord(input.user).full_name),
    segment: null,
  };

  return {
    buyer,
    accessToken: toStringValue(input.access_token ?? input.token),
    tokenType: toStringValue(input.token_type, "Bearer"),
  };
}

async function request<T>(path: string, init: RequestOptions = {}): Promise<T> {
  const { token, ...requestInit } = init;
  const headers = new Headers(requestInit.headers ?? {});

  if (requestInit.body && !(requestInit.body instanceof FormData) && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  const response = await fetch(`${apiBaseUrl}${path}`, {
    ...requestInit,
    headers,
  });

  const contentType = response.headers.get("content-type") ?? "";
  const payload = contentType.includes("application/json") ? await response.json() : await response.text();

  if (!response.ok) {
    const detail =
      typeof payload === "string"
        ? payload
        : toStringValue(toRecord(payload).detail ?? toRecord(payload).message, `request_failed:${response.status}`);
    throw new ApiError(response.status, detail);
  }

  return payload as T;
}

export function readBuyerSession(): BuyerSession | null {
  if (typeof window === "undefined") {
    return null;
  }

  const rawValue = window.localStorage.getItem(buyerSessionStorageKey);
  if (!rawValue) {
    return null;
  }

  try {
    return normalizeSession(JSON.parse(rawValue) as BuyerSession);
  } catch {
    window.localStorage.removeItem(buyerSessionStorageKey);
    return null;
  }
}

export function writeBuyerSession(input: AuthResponse | BuyerSession): BuyerSession {
  const normalized = normalizeSession(input);

  if (typeof window !== "undefined") {
    window.localStorage.setItem(buyerSessionStorageKey, JSON.stringify(normalized));
  }

  return normalized;
}

export function clearBuyerSession() {
  if (typeof window !== "undefined") {
    window.localStorage.removeItem(buyerSessionStorageKey);
  }
}

export function fetchCatalog() {
  return request<CatalogResponse>("/catalog/products");
}

export function registerBuyer(payload: RegisterPayload) {
  return request<AuthResponse>("/auth/register", {
    method: "POST",
    body: JSON.stringify(payload),
  }).then(writeBuyerSession);
}

export function loginBuyer(payload: LoginPayload) {
  return request<AuthResponse>("/auth/login", {
    method: "POST",
    body: JSON.stringify(payload),
  }).then(writeBuyerSession);
}

export function fetchCart(token: string) {
  return request<unknown>("/cart", { token }).then(normalizeCart);
}

export function addCartItem(token: string, productId: string, quantity: number) {
  return request<unknown>("/cart/items", {
    method: "POST",
    token,
    body: JSON.stringify({ product_id: productId, quantity }),
  }).then(normalizeCart);
}

export function updateCartItem(token: string, productId: string, quantity: number) {
  return request<unknown>(`/cart/items/${productId}`, {
    method: "PATCH",
    token,
    body: JSON.stringify({ quantity }),
  }).then(normalizeCart);
}

export function removeCartItem(token: string, productId: string) {
  return request<unknown>(`/cart/items/${productId}`, {
    method: "DELETE",
    token,
  }).then(normalizeCart);
}

export function fetchOrders(token: string) {
  return request<unknown>("/orders", { token }).then((payload) => {
    const record = toRecord(payload);
    const rawItems = Array.isArray(payload)
      ? payload
      : Array.isArray(record.items)
        ? record.items
        : Array.isArray(record.orders)
          ? record.orders
          : [];

    return {
      items: rawItems.map(normalizeOrder),
    } satisfies OrdersResponse;
  });
}

export function createOrder(token: string, payload: CreateOrderPayload = {}) {
  return request<unknown>("/orders", {
    method: "POST",
    token,
    body: JSON.stringify(payload),
  }).then((response) => {
    const record = toRecord(response);
    const order = normalizeOrder(record.order ?? response);
    const paymentAttempt = normalizePaymentAttempt(
      record.payment_attempt ?? order.payment_attempt,
    );

    return {
      order,
      payment_attempt: paymentAttempt,
    } satisfies CreateOrderResponse;
  });
}

export function confirmMockPayment(token: string, orderId: string) {
  return request<unknown>("/payments/mock/confirm", {
    method: "POST",
    token,
    body: JSON.stringify({ order_id: orderId }),
  }).then((response) => {
    const record = toRecord(response);
    const order = normalizeOrder(record.order ?? response);
    const paymentAttempt = normalizePaymentAttempt(
      record.payment_attempt ?? order.payment_attempt,
    );

    return {
      order,
      payment_attempt: paymentAttempt,
    } satisfies ConfirmPaymentResponse;
  });
}
```

## `client/storefront/src/styles/main.css`

```css
:root {
  color-scheme: light;
  font-family: "Fraunces", "Pretendard", "Noto Sans KR", serif;
  line-height: 1.5;
  font-weight: 400;
  color: #2a221d;
  background:
    radial-gradient(circle at top left, rgba(255, 227, 190, 0.88), transparent 28%),
    radial-gradient(circle at bottom right, rgba(221, 194, 174, 0.7), transparent 26%),
    linear-gradient(135deg, #f7efe2 0%, #f5f0ea 48%, #ebe1d6 100%);
  --ink: #2a221d;
  --muted: #75665a;
  --card: rgba(255, 250, 244, 0.82);
  --card-strong: rgba(245, 232, 219, 0.95);
  --line: rgba(72, 52, 36, 0.12);
  --accent: #9d4f26;
  --accent-strong: #7f3515;
  --accent-soft: rgba(157, 79, 38, 0.11);
  --olive: #4b5d3b;
  --shadow: 0 22px 60px rgba(73, 51, 35, 0.14);
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
}

a {
  color: inherit;
  text-decoration: none;
}

button,
input,
textarea {
  font: inherit;
}

button {
  cursor: pointer;
}

input,
textarea {
  color: var(--ink);
}

#root {
  min-height: 100vh;
}

.shell {
  min-height: 100vh;
  padding: 28px 18px 42px;
}

.topbar,
.layout {
  width: min(1200px, 100%);
  margin: 0 auto;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 24px;
  margin-bottom: 26px;
}

.brand-block h1 {
  margin: 8px 0 10px;
  max-width: 11ch;
  font-size: clamp(2.6rem, 5vw, 5.4rem);
  line-height: 0.95;
  letter-spacing: -0.06em;
}

.lede {
  margin: 0;
  max-width: 56ch;
  color: var(--muted);
  font-size: 1.02rem;
}

.topnav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.topnav a {
  padding: 11px 16px;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(255, 251, 246, 0.75);
  backdrop-filter: blur(14px);
}

.eyebrow {
  margin: 0;
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.layout {
  display: grid;
  gap: 18px;
}

.card {
  border: 1px solid var(--line);
  border-radius: 30px;
  background: var(--card);
  box-shadow: var(--shadow);
  backdrop-filter: blur(16px);
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 1.45fr) minmax(320px, 0.9fr);
  gap: 18px;
  padding: 28px;
}

.hero-copy h2 {
  margin: 12px 0 12px;
  font-size: clamp(2rem, 3.8vw, 3.55rem);
  line-height: 0.98;
  letter-spacing: -0.05em;
}

.hero-copy p {
  margin: 0;
  max-width: 54ch;
  color: var(--muted);
}

.hero-aside {
  padding: 20px;
  border-radius: 24px;
  background:
    linear-gradient(155deg, rgba(43, 30, 21, 0.96), rgba(79, 46, 28, 0.92)),
    linear-gradient(180deg, rgba(255, 255, 255, 0.08), transparent);
  color: #f9f3eb;
}

.hero-aside strong {
  display: block;
  margin-top: 4px;
  font-size: 1.4rem;
}

.hero-aside p {
  margin: 8px 0 0;
  color: rgba(249, 243, 235, 0.74);
}

.hero-panel-label,
.callout-label,
.session-label {
  margin: 0;
  color: rgba(249, 243, 235, 0.68);
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.75rem;
}

.hero-metrics {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin: 18px 0 0;
}

.hero-metrics div {
  padding: 14px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.08);
}

.hero-metrics dt,
.hero-metrics dd {
  margin: 0;
}

.hero-metrics dt {
  color: rgba(249, 243, 235, 0.62);
  font-size: 0.82rem;
}

.hero-metrics dd {
  margin-top: 4px;
  font-size: 1.05rem;
  font-weight: 700;
}

.banner {
  margin: 0;
  padding: 15px 18px;
  border-radius: 18px;
  border: 1px solid var(--line);
}

.banner-error {
  background: rgba(168, 63, 40, 0.12);
  color: #8f2c1c;
}

.banner-status {
  background: rgba(75, 93, 59, 0.12);
  color: #314223;
}

.feature-grid,
.checkout-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.auth-panel,
.pulse-panel,
.cart-panel,
.checkout-panel,
.orders-panel {
  padding: 24px;
}

.section-heading {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 18px;
}

.section-heading h2 {
  margin: 6px 0 0;
  font-size: clamp(1.45rem, 2.5vw, 2.15rem);
  letter-spacing: -0.04em;
}

.auth-chip {
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(66, 53, 44, 0.08);
  color: var(--muted);
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}

.auth-chip-live {
  background: rgba(75, 93, 59, 0.14);
  color: var(--olive);
}

.auth-toggle {
  display: inline-grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 6px;
  padding: 6px;
  border-radius: 18px;
  background: rgba(88, 65, 49, 0.07);
}

.auth-toggle button,
.primary-button,
.secondary-button,
.qty-controls button {
  border: 0;
  border-radius: 16px;
}

.auth-toggle button {
  padding: 10px 14px;
  background: transparent;
  color: var(--muted);
}

.auth-toggle .is-active {
  background: #fff7f0;
  color: var(--ink);
  box-shadow: 0 10px 24px rgba(70, 48, 31, 0.08);
}

.auth-form,
.note-field,
.cart-list,
.totals,
.orders-list {
  display: grid;
  gap: 14px;
}

.auth-form {
  margin-top: 18px;
}

.auth-form label,
.note-field {
  display: grid;
  gap: 8px;
}

.auth-form span,
.note-field span {
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}

.auth-form input,
.note-field textarea {
  width: 100%;
  padding: 14px 16px;
  border: 1px solid rgba(82, 62, 47, 0.14);
  border-radius: 18px;
  background: rgba(255, 252, 248, 0.86);
  outline: none;
}

.auth-form input:focus,
.note-field textarea:focus {
  border-color: rgba(157, 79, 38, 0.45);
  box-shadow: 0 0 0 4px rgba(157, 79, 38, 0.12);
}

.primary-button,
.secondary-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 48px;
  padding: 0 18px;
  transition: transform 160ms ease, opacity 160ms ease;
}

.primary-button {
  background: linear-gradient(145deg, var(--accent), var(--accent-strong));
  color: #fffaf6;
}

.secondary-button {
  background: rgba(71, 55, 43, 0.08);
  color: var(--ink);
}

.primary-button:disabled,
.secondary-button:disabled,
.qty-controls button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.primary-button:not(:disabled):hover,
.secondary-button:not(:disabled):hover,
.qty-controls button:not(:disabled):hover {
  transform: translateY(-1px);
}

.session-card {
  display: grid;
  gap: 16px;
  padding: 20px;
  border-radius: 24px;
  background: var(--card-strong);
}

.session-card strong {
  font-size: 1.4rem;
}

.session-card p {
  margin: 6px 0 0;
  color: var(--muted);
}

.benefit-list,
.pill-row,
.chip-row,
.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.benefit-list {
  margin: 0;
  padding-left: 18px;
  color: var(--muted);
}

.pill,
.chip,
.tag,
.status-badge {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 8px 12px;
}

.pill {
  background: var(--accent-soft);
  color: var(--accent-strong);
}

.chip {
  background: rgba(255, 251, 245, 0.72);
  border: 1px solid rgba(74, 57, 46, 0.1);
}

.tag {
  background: rgba(75, 93, 59, 0.12);
  color: var(--olive);
  font-size: 0.84rem;
}

.pulse-panel {
  background:
    linear-gradient(180deg, rgba(255, 249, 241, 0.94), rgba(244, 232, 219, 0.94));
}

.stage-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}

.stage-card {
  min-height: 160px;
  padding: 18px;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.55);
  border: 1px solid rgba(83, 60, 40, 0.08);
}

.stage-card span {
  display: inline-flex;
  width: 34px;
  height: 34px;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  background: rgba(157, 79, 38, 0.1);
  color: var(--accent);
  font-weight: 700;
}

.stage-card strong {
  display: block;
  margin-top: 16px;
  font-size: 1.16rem;
}

.stage-card p {
  margin: 10px 0 0;
  color: var(--muted);
}

.accent-card {
  background: linear-gradient(155deg, rgba(80, 92, 59, 0.14), rgba(255, 255, 255, 0.65));
}

.stat-row {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin-top: 18px;
}

.stat-row div {
  padding: 16px 18px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.56);
}

.stat-row small {
  display: block;
  color: var(--muted);
}

.stat-row strong {
  display: block;
  margin-top: 6px;
  font-size: 1.18rem;
}

.catalog-section {
  display: grid;
  gap: 16px;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
}

.product-card {
  display: grid;
  gap: 14px;
  padding: 20px;
}

.product-card h3 {
  margin: 0;
  font-size: 1.42rem;
  letter-spacing: -0.03em;
}

.product-meta,
.product-footer,
.order-head,
.payment-callout,
.cart-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.product-meta,
.summary,
.product-footer small,
.empty-state,
.policy,
.order-body p,
.order-note,
.muted-copy {
  color: var(--muted);
}

.summary,
.empty-state,
.policy,
.order-body p,
.order-note {
  margin: 0;
}

.price-row {
  display: flex;
  align-items: baseline;
  gap: 10px;
}

.price-row strong {
  font-size: 1.18rem;
}

.price-row span {
  color: #9b8b7d;
  text-decoration: line-through;
}

.empty-card {
  padding: 20px;
}

.cart-item,
.order-card {
  padding-bottom: 14px;
  border-bottom: 1px solid rgba(78, 58, 43, 0.08);
}

.cart-item p,
.order-head p {
  margin: 5px 0 0;
  color: var(--muted);
}

.qty-controls {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.qty-controls button {
  width: 34px;
  height: 34px;
  background: rgba(67, 48, 33, 0.08);
  color: var(--ink);
}

.totals div {
  display: flex;
  justify-content: space-between;
  gap: 16px;
}

.totals dt,
.totals dd {
  margin: 0;
}

.total-row {
  font-size: 1.12rem;
  font-weight: 700;
}

.payment-callout {
  padding: 18px;
  border-radius: 24px;
  background:
    linear-gradient(160deg, rgba(81, 97, 59, 0.14), rgba(255, 255, 255, 0.7));
  border: 1px solid rgba(75, 93, 59, 0.12);
}

.payment-callout strong {
  display: block;
  margin-top: 4px;
  font-size: 1.2rem;
}

.payment-callout p {
  margin: 8px 0 0;
  color: var(--muted);
}

.orders-list {
  gap: 16px;
}

.order-card {
  display: grid;
  gap: 14px;
}

.order-meta {
  text-align: right;
}

.status-badge {
  margin-bottom: 8px;
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.status-pending {
  background: rgba(157, 79, 38, 0.12);
  color: var(--accent-strong);
}

.status-paid {
  background: rgba(75, 93, 59, 0.14);
  color: var(--olive);
}

@media (max-width: 1120px) {
  .hero,
  .feature-grid,
  .checkout-grid {
    grid-template-columns: 1fr;
  }

  .product-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 720px) {
  .shell {
    padding: 18px 14px 30px;
  }

  .topbar,
  .section-heading,
  .topnav,
  .product-footer,
  .product-meta,
  .cart-item,
  .payment-callout,
  .order-head {
    flex-direction: column;
    align-items: flex-start;
  }

  .hero,
  .auth-panel,
  .pulse-panel,
  .cart-panel,
  .checkout-panel,
  .orders-panel {
    padding: 20px;
  }

  .hero-metrics,
  .stage-grid,
  .stat-row,
  .product-grid {
    grid-template-columns: 1fr;
  }

  .order-meta {
    text-align: left;
  }

  .topnav {
    width: 100%;
  }
}
```
