---
title: "6. Admin 프론트 코드"
source_kind: page
source_path: manual-local/lecture/fullstack-study/11-practice-code/06-admin
parent_notion_id: 32be313f58b980078dbbeed4f006f95b
---
# 6. Admin 프론트 코드
이 페이지는 운영자용 admin 앱의 전체 코드를 담습니다. 03장 3절에서 기획한 운영자 화면과 08장에서 구현한 주문 운영, 상품 운영, 접근 제어가 실제 코드로 어떻게 나타났는지 확인합니다.

`src/app/auth.tsx`가 로그인과 세션을 맡고, `src/app/dashboard.tsx`가 운영 화면 본체를 담습니다. admin은 storefront와 같은 서버를 보지만 권한이 다르므로, `src/lib/api.ts`에서 인증 헤더를 붙이는 방식이 storefront와 어떻게 다른지 비교해 보면 06장 4절의 접근 제어 설명이 분명해집니다.

# 파일

## `client/admin/index.html`

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lecture Admin</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
  </html>
```

## `client/admin/package.json`

```json
{
  "name": "lecture-admin",
  "private": true,
  "version": "0.1.0",
  "packageManager": "pnpm@10.32.1",
  "type": "module",
  "scripts": {
    "dev": "vite --host 0.0.0.0 --port 5174",
    "build": "tsc -b && vite build",
    "preview": "vite preview --host 0.0.0.0 --port 4174"
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

## `client/admin/tsconfig.json`

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

## `client/admin/vite.config.ts`

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
    port: 5174,
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
    port: 4174,
  },
});
```

## `client/admin/src/main.tsx`

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

## `client/admin/src/app/App.tsx`

```tsx
import { Navigate, Outlet, Route, Routes, useLocation } from "react-router-dom";

import { AuthProvider, useAuth } from "@/app/auth";
import {
  AdminShell,
  LoginPage,
  OrdersPage,
  OverviewPage,
  PaymentAttemptsPage,
  ProductsPage,
} from "@/app/dashboard";

function ProtectedRoute() {
  const location = useLocation();
  const { isHydrated, session } = useAuth();

  if (!isHydrated) {
    return <div className="boot-splash">Admin session 준비 중...</div>;
  }

  if (!session) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }

  return <Outlet />;
}

function LoginRoute() {
  const { isHydrated, session } = useAuth();

  if (!isHydrated) {
    return <div className="boot-splash">Admin session 준비 중...</div>;
  }

  if (session) {
    return <Navigate to="/overview" replace />;
  }

  return <LoginPage />;
}

export default function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/login" element={<LoginRoute />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/" element={<AdminShell />}>
            <Route index element={<Navigate to="/overview" replace />} />
            <Route path="overview" element={<OverviewPage />} />
            <Route path="products" element={<ProductsPage />} />
            <Route path="orders" element={<OrdersPage />} />
            <Route path="payments" element={<PaymentAttemptsPage />} />
          </Route>
        </Route>
        <Route path="*" element={<Navigate to="/overview" replace />} />
      </Routes>
    </AuthProvider>
  );
}
```

## `client/admin/src/app/auth.tsx`

```tsx
import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

import { loginAdmin, type AdminLoginCredentials, type AdminSession } from "@/lib/api";

const SESSION_STORAGE_KEY = "lecture-admin-session";

type AuthContextValue = {
  isAuthenticating: boolean;
  isHydrated: boolean;
  session: AdminSession | null;
  login: (credentials: AdminLoginCredentials) => Promise<AdminSession>;
  logout: () => void;
};

const AuthContext = createContext<AuthContextValue | null>(null);

function readStoredSession(): AdminSession | null {
  if (typeof window === "undefined") {
    return null;
  }

  try {
    const rawValue = window.localStorage.getItem(SESSION_STORAGE_KEY);
    return rawValue ? (JSON.parse(rawValue) as AdminSession) : null;
  } catch {
    return null;
  }
}

function persistSession(session: AdminSession | null) {
  if (typeof window === "undefined") {
    return;
  }

  if (session) {
    window.localStorage.setItem(SESSION_STORAGE_KEY, JSON.stringify(session));
    return;
  }

  window.localStorage.removeItem(SESSION_STORAGE_KEY);
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [session, setSession] = useState<AdminSession | null>(() => readStoredSession());
  const [isHydrated, setIsHydrated] = useState(false);
  const [isAuthenticating, setIsAuthenticating] = useState(false);

  useEffect(() => {
    setIsHydrated(true);
  }, []);

  async function login(credentials: AdminLoginCredentials) {
    setIsAuthenticating(true);

    try {
      const nextSession = await loginAdmin(credentials);
      setSession(nextSession);
      persistSession(nextSession);
      return nextSession;
    } finally {
      setIsAuthenticating(false);
    }
  }

  function logout() {
    setSession(null);
    persistSession(null);
  }

  return (
    <AuthContext.Provider
      value={{
        isAuthenticating,
        isHydrated,
        session,
        login,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }

  return context;
}
```

## `client/admin/src/app/dashboard.tsx`

```tsx
import { startTransition, useDeferredValue, useEffect, useState, useTransition } from "react";
import {
  NavLink,
  Outlet,
  useLocation,
  useNavigate,
  useOutletContext,
} from "react-router-dom";

import { useAuth } from "@/app/auth";
import {
  ApiError,
  demoCredentials,
  fetchAdminSnapshot,
  type AdminOrder,
  type AdminProduct,
  type AdminSnapshot,
  type PaymentAttempt,
} from "@/lib/api";

const currencyFormatter = new Intl.NumberFormat("ko-KR");
const dateTimeFormatter = new Intl.DateTimeFormat("ko-KR", {
  dateStyle: "medium",
  timeStyle: "short",
});

type AdminRouteContext = {
  error: string | null;
  isRefreshing: boolean;
  lastUpdated: string | null;
  refresh: () => Promise<void>;
  snapshot: AdminSnapshot | null;
};

function formatCurrency(value: number) {
  return `${currencyFormatter.format(value)}원`;
}

function formatDateTime(value: string) {
  return dateTimeFormatter.format(new Date(value));
}

function humanize(value: string) {
  return value.split("_").join(" ");
}

function readRedirectTarget(state: unknown): string {
  if (!state || typeof state !== "object" || !("from" in state)) {
    return "/overview";
  }

  const candidate = (state as { from?: unknown }).from;
  return typeof candidate === "string" ? candidate : "/overview";
}

function useAdminRouteData() {
  return useOutletContext<AdminRouteContext>();
}

function StatusBadge({ value }: { value: string }) {
  const tone =
    value.includes("fail") || value.includes("declin")
      ? "danger"
      : value.includes("retry") || value.includes("low") || value.includes("watch")
        ? "warning"
        : value.includes("ready") || value.includes("paid") || value.includes("success")
          ? "success"
          : "neutral";

  return <span className={`status-badge status-${tone}`}>{humanize(value)}</span>;
}

function TableEmptyState({ title, body }: { title: string; body: string }) {
  return (
    <div className="table-empty-state">
      <strong>{title}</strong>
      <p>{body}</p>
    </div>
  );
}

export function LoginPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const { isAuthenticating, login } = useAuth();

  const [email, setEmail] = useState(demoCredentials.email);
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);

    try {
      await login({ email, password });
      navigate(readRedirectTarget(location.state), { replace: true });
    } catch (requestError) {
      setError(
        requestError instanceof Error ? requestError.message : "로그인 요청을 처리하지 못했습니다.",
      );
    }
  }

  return (
    <div className="login-shell">
      <section className="login-hero">
        <p className="eyebrow">Lecture Commerce</p>
        <h1>운영 로그인을 거친 뒤에만 admin view를 여는 구조로 올립니다.</h1>
        <p className="lead-copy">
          상품, 주문, 결제 시도, 핵심 운영 메트릭을 분리된 protected view로 재구성했습니다.
          백엔드 세션 엔드포인트가 준비되면 그대로 연결되고, 현재는 demo fallback으로 강의 진행이
          가능합니다.
        </p>
        <div className="login-feature-list">
          <div className="feature-chip">Protected routes</div>
          <div className="feature-chip">Session persistence</div>
          <div className="feature-chip">Operations overview</div>
          <div className="feature-chip">Payment attempts feed</div>
        </div>
      </section>

      <section className="login-panel">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Admin Access</p>
            <h2>Lecture Admin</h2>
          </div>
          <span className="surface-tag">/api/v1/admin/session</span>
        </div>

        <form className="login-form" onSubmit={handleSubmit}>
          <label>
            <span>Operator Email</span>
            <input
              autoComplete="email"
              name="email"
              type="email"
              value={email}
              onChange={(event) => setEmail(event.currentTarget.value)}
            />
          </label>
          <label>
            <span>Password</span>
            <input
              autoComplete="current-password"
              name="password"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.currentTarget.value)}
            />
          </label>
          {error ? <p className="form-error">{error}</p> : null}
          <button className="primary-button" disabled={isAuthenticating} type="submit">
            {isAuthenticating ? "Signing in..." : "Enter Admin"}
          </button>
        </form>

        <div className="demo-credentials">
          <p className="eyebrow">Demo Fallback</p>
          <strong>{demoCredentials.email}</strong>
          <span>{demoCredentials.password}</span>
          <p>세션 엔드포인트가 아직 없을 때 위 계정으로 prototype 인증을 통과합니다.</p>
        </div>
      </section>
    </div>
  );
}

export function AdminShell() {
  const location = useLocation();
  const navigate = useNavigate();
  const { logout, session } = useAuth();
  const [snapshot, setSnapshot] = useState<AdminSnapshot | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [isPending, startUiTransition] = useTransition();
  const [lastUpdated, setLastUpdated] = useState<string | null>(null);

  async function loadSnapshot() {
    if (!session) {
      return;
    }

    setError(null);
    setIsLoading(true);

    try {
      const nextSnapshot = await fetchAdminSnapshot(session);
      startUiTransition(() => {
        setSnapshot(nextSnapshot);
        setLastUpdated(new Date().toISOString());
      });
    } catch (requestError) {
      if (requestError instanceof ApiError && [401, 403].includes(requestError.status)) {
        logout();
        navigate("/login", { replace: true, state: { from: location.pathname } });
        return;
      }

      setError(
        requestError instanceof Error
          ? requestError.message
          : "관리자 데이터를 불러오지 못했습니다.",
      );
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    void loadSnapshot();
  }, [session?.source, session?.token]);

  const routeContext: AdminRouteContext = {
    error,
    isRefreshing: isLoading || isPending,
    lastUpdated,
    refresh: loadSnapshot,
    snapshot,
  };

  return (
    <div className="admin-shell">
      <aside className="rail">
        <div className="rail-brand">
          <p className="eyebrow">Ops Control</p>
          <h1>Lecture Admin</h1>
          <p>강의용 운영자 surface를 로그인과 권한 전제로 정리한 정본 shell입니다.</p>
        </div>

        <nav className="nav-stack" aria-label="Admin views">
          <NavLink
            className={({ isActive }) => `nav-link${isActive ? " nav-link-active" : ""}`}
            to="/overview"
          >
            Overview
          </NavLink>
          <NavLink
            className={({ isActive }) => `nav-link${isActive ? " nav-link-active" : ""}`}
            to="/products"
          >
            Products
          </NavLink>
          <NavLink
            className={({ isActive }) => `nav-link${isActive ? " nav-link-active" : ""}`}
            to="/orders"
          >
            Orders
          </NavLink>
          <NavLink
            className={({ isActive }) => `nav-link${isActive ? " nav-link-active" : ""}`}
            to="/payments"
          >
            Payment Attempts
          </NavLink>
        </nav>

        <div className="rail-card">
          <p className="eyebrow">Session</p>
          <strong>{session?.operator.name}</strong>
          <span>{session?.operator.email}</span>
          <span>{session?.operator.role}</span>
          <button className="ghost-button" onClick={logout} type="button">
            Sign out
          </button>
        </div>
      </aside>

      <div className="workspace">
        <header className="workspace-header">
          <div>
            <p className="eyebrow">Protected Dashboard</p>
            <h2>{snapshot?.dataMode === "live" ? "Live admin feed" : "Lecture admin control plane"}</h2>
          </div>
          <div className="header-actions">
            {session ? <span className="surface-tag">{session.source} auth</span> : null}
            {snapshot ? <span className="surface-tag">{snapshot.dataMode} data</span> : null}
            <a
              className="ghost-link"
              href="http://127.0.0.1:5173"
              rel="noreferrer"
              target="_blank"
            >
              Storefront
            </a>
            <button className="primary-button" onClick={() => void loadSnapshot()} type="button">
              {isLoading || isPending ? "Refreshing..." : "Refresh"}
            </button>
          </div>
        </header>

        {lastUpdated ? (
          <p className="meta-line">Last synced {formatDateTime(lastUpdated)}</p>
        ) : null}

        {error ? <div className="error-banner">{error}</div> : null}
        {snapshot?.notices.map((notice) => (
          <div key={notice} className="info-banner">
            {notice}
          </div>
        ))}

        {!snapshot && !error ? (
          <div className="loading-panel">
            <p className="eyebrow">Loading</p>
            <h3>Admin datasets are booting.</h3>
            <p>Session-authenticated overview, inventory, order, and payment data are loading now.</p>
          </div>
        ) : null}

        {!snapshot && error ? (
          <div className="loading-panel">
            <p className="eyebrow">Retry</p>
            <h3>Admin 데이터를 다시 요청해야 합니다.</h3>
            <button className="primary-button" onClick={() => void loadSnapshot()} type="button">
              Retry
            </button>
          </div>
        ) : null}

        {snapshot ? <Outlet context={routeContext} /> : null}
      </div>
    </div>
  );
}

export function OverviewPage() {
  const { error, isRefreshing, lastUpdated, snapshot } = useAdminRouteData();

  if (!snapshot) {
    return null;
  }

  const failedPayments = snapshot.paymentAttempts.filter((attempt) =>
    attempt.status.includes("fail"),
  ).length;
  const retryablePayments = snapshot.paymentAttempts.filter((attempt) => attempt.retryable).length;
  const readyOrders = snapshot.orders.filter((order) => order.status.includes("ready")).length;

  return (
    <main className="workspace-content">
      <section className="metrics-grid">
        {snapshot.dashboard.metrics.map((metric) => (
          <article key={metric.label} className="metric-card">
            <p>{metric.label}</p>
            <strong>{metric.value}</strong>
            <span>{metric.delta}</span>
          </article>
        ))}
      </section>

      <section className="hero-panels">
        <article className="panel spotlight-card">
          <div className="panel-header">
            <div>
              <p className="eyebrow">Highlight Order</p>
              <h3>{snapshot.dashboard.highlight_order.id}</h3>
            </div>
            <StatusBadge value={snapshot.dashboard.highlight_order.status} />
          </div>
          <dl className="detail-grid">
            <div>
              <dt>Customer</dt>
              <dd>{snapshot.dashboard.highlight_order.customer}</dd>
            </div>
            <div>
              <dt>Channel</dt>
              <dd>{snapshot.dashboard.highlight_order.channel}</dd>
            </div>
            <div>
              <dt>Total</dt>
              <dd>{formatCurrency(snapshot.dashboard.highlight_order.total_amount)}</dd>
            </div>
            <div>
              <dt>Items</dt>
              <dd>{snapshot.dashboard.highlight_order.item_count}</dd>
            </div>
          </dl>
        </article>

        <article className="panel watchlist-card">
          <div className="panel-header">
            <div>
              <p className="eyebrow">Inventory Watchlist</p>
              <h3>Low stock attention</h3>
            </div>
            <span className="surface-tag">{snapshot.dashboard.watchlist.length} SKU</span>
          </div>
          <ul className="watchlist">
            {snapshot.dashboard.watchlist.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </article>
      </section>

      <section className="panel-cluster">
        <article className="panel">
          <div className="panel-header">
            <div>
              <p className="eyebrow">Operational Pulse</p>
              <h3>Order + payment health</h3>
            </div>
            {lastUpdated ? <span className="surface-tag">{formatDateTime(lastUpdated)}</span> : null}
          </div>
          <div className="insight-grid">
            <div className="insight-tile">
              <span>Ready to ship</span>
              <strong>{readyOrders}</strong>
              <p>fulfillment-ready orders in the current sample window</p>
            </div>
            <div className="insight-tile">
              <span>Failed payments</span>
              <strong>{failedPayments}</strong>
              <p>attempts that need operator review or customer retry</p>
            </div>
            <div className="insight-tile">
              <span>Retry queue</span>
              <strong>{retryablePayments}</strong>
              <p>payment attempts still eligible for the next operation</p>
            </div>
          </div>
        </article>

        <article className="panel">
          <div className="panel-header">
            <div>
              <p className="eyebrow">Runtime Status</p>
              <h3>Surface notes</h3>
            </div>
          </div>
          <ul className="watchlist">
            <li>{snapshot.dataMode === "live" ? "All datasets are live." : "Prototype fallback data is active."}</li>
            <li>{error ? error : "No active request errors."}</li>
            <li>{isRefreshing ? "A refresh cycle is running." : "Dashboard is currently idle."}</li>
          </ul>
        </article>
      </section>
    </main>
  );
}

export function ProductsPage() {
  const { snapshot } = useAdminRouteData();
  const [query, setQuery] = useState("");
  const [stockFilter, setStockFilter] = useState<"all" | "low" | "stable">("all");
  const deferredQuery = useDeferredValue(query);

  if (!snapshot) {
    return null;
  }

  const visibleProducts = snapshot.products.filter((product) => {
    const matchesQuery =
      deferredQuery.trim().length === 0 ||
      [product.title, product.category, product.tags.join(" ")]
        .join(" ")
        .toLowerCase()
        .includes(deferredQuery.trim().toLowerCase());

    const matchesStock = stockFilter === "all" || product.stock_state === stockFilter;
    return matchesQuery && matchesStock;
  });

  const lowStockCount = snapshot.products.filter((product) => product.stock_state === "low").length;

  return (
    <main className="workspace-content">
      <section className="panel section-panel">
        <div className="panel-header panel-header-spaced">
          <div>
            <p className="eyebrow">Products</p>
            <h3>Inventory command view</h3>
          </div>
          <span className="surface-tag">{snapshot.products.length} items</span>
        </div>

        <div className="toolbar">
          <label className="toolbar-search">
            <span>Search</span>
            <input
              type="search"
              value={query}
              onChange={(event) => {
                const value = event.currentTarget.value;
                startTransition(() => setQuery(value));
              }}
              placeholder="title, category, tag"
            />
          </label>
          <div className="segmented-control" role="tablist" aria-label="Stock filter">
            {(["all", "low", "stable"] as const).map((value) => (
              <button
                key={value}
                className={stockFilter === value ? "segment-active" : ""}
                onClick={() => setStockFilter(value)}
                type="button"
              >
                {value === "all" ? "All stock" : humanize(value)}
              </button>
            ))}
          </div>
        </div>

        <div className="summary-strip">
          <div>
            <span>Low stock SKU</span>
            <strong>{lowStockCount}</strong>
          </div>
          <div>
            <span>Visible rows</span>
            <strong>{visibleProducts.length}</strong>
          </div>
        </div>

        <div className="table-scroll">
          <table>
            <thead>
              <tr>
                <th>Product</th>
                <th>Category</th>
                <th>Tags</th>
                <th>Price</th>
                <th>Inventory</th>
                <th>State</th>
              </tr>
            </thead>
            <tbody>
              {visibleProducts.map((product) => (
                <tr key={product.id}>
                  <td>
                    <strong>{product.title}</strong>
                    <div className="subcopy">{product.id}</div>
                  </td>
                  <td>{product.category}</td>
                  <td>{product.tags.join(" · ")}</td>
                  <td>{formatCurrency(product.price)}</td>
                  <td>{product.inventory}</td>
                  <td>
                    <StatusBadge value={product.stock_state} />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {visibleProducts.length === 0 ? (
            <TableEmptyState
              body="다른 키워드나 재고 상태 필터로 다시 좁혀 보세요."
              title="표시할 상품이 없습니다."
            />
          ) : null}
        </div>
      </section>
    </main>
  );
}

export function OrdersPage() {
  const { snapshot } = useAdminRouteData();
  const [query, setQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");
  const deferredQuery = useDeferredValue(query);

  if (!snapshot) {
    return null;
  }

  const uniqueStatuses = Array.from(new Set(snapshot.orders.map((order) => order.status)));
  const visibleOrders = snapshot.orders.filter((order) => {
    const matchesQuery =
      deferredQuery.trim().length === 0 ||
      [order.id, order.customer, order.channel]
        .join(" ")
        .toLowerCase()
        .includes(deferredQuery.trim().toLowerCase());
    const matchesStatus = statusFilter === "all" || order.status === statusFilter;
    return matchesQuery && matchesStatus;
  });

  const grossAmount = visibleOrders.reduce((total, order) => total + order.total_amount, 0);

  return (
    <main className="workspace-content">
      <section className="panel section-panel">
        <div className="panel-header panel-header-spaced">
          <div>
            <p className="eyebrow">Orders</p>
            <h3>Fulfillment and revenue watch</h3>
          </div>
          <span className="surface-tag">{formatCurrency(grossAmount)}</span>
        </div>

        <div className="toolbar">
          <label className="toolbar-search">
            <span>Search</span>
            <input
              type="search"
              value={query}
              onChange={(event) => {
                const value = event.currentTarget.value;
                startTransition(() => setQuery(value));
              }}
              placeholder="order id, customer, channel"
            />
          </label>
          <div className="segmented-control" role="tablist" aria-label="Order status filter">
            {["all", ...uniqueStatuses].map((value) => (
              <button
                key={value}
                className={statusFilter === value ? "segment-active" : ""}
                onClick={() => setStatusFilter(value)}
                type="button"
              >
                {value === "all" ? "All orders" : humanize(value)}
              </button>
            ))}
          </div>
        </div>

        <div className="table-scroll">
          <table>
            <thead>
              <tr>
                <th>Order</th>
                <th>Customer</th>
                <th>Channel</th>
                <th>Items</th>
                <th>Total</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {visibleOrders.map((order) => (
                <tr key={order.id}>
                  <td>{order.id}</td>
                  <td>{order.customer}</td>
                  <td>{order.channel}</td>
                  <td>{order.item_count}</td>
                  <td>{formatCurrency(order.total_amount)}</td>
                  <td>
                    <StatusBadge value={order.status} />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {visibleOrders.length === 0 ? (
            <TableEmptyState
              body="주문 상태 또는 검색어 조건을 다시 확인해 주세요."
              title="표시할 주문이 없습니다."
            />
          ) : null}
        </div>
      </section>
    </main>
  );
}

export function PaymentAttemptsPage() {
  const { snapshot } = useAdminRouteData();
  const [query, setQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");
  const deferredQuery = useDeferredValue(query);

  if (!snapshot) {
    return null;
  }

  const uniqueStatuses = Array.from(
    new Set(snapshot.paymentAttempts.map((attempt) => attempt.status)),
  );
  const visibleAttempts = snapshot.paymentAttempts.filter((attempt) => {
    const matchesQuery =
      deferredQuery.trim().length === 0 ||
      [attempt.id, attempt.order_id, attempt.customer, attempt.provider]
        .join(" ")
        .toLowerCase()
        .includes(deferredQuery.trim().toLowerCase());
    const matchesStatus = statusFilter === "all" || attempt.status === statusFilter;
    return matchesQuery && matchesStatus;
  });

  const totalAmount = visibleAttempts.reduce((total, attempt) => total + attempt.amount, 0);
  const retryQueue = visibleAttempts.filter((attempt) => attempt.retryable).length;

  return (
    <main className="workspace-content">
      <section className="panel section-panel">
        <div className="panel-header panel-header-spaced">
          <div>
            <p className="eyebrow">Payment Attempts</p>
            <h3>Collections and failure review</h3>
          </div>
          <span className="surface-tag">{snapshot.paymentAttempts.length} attempts</span>
        </div>

        <div className="summary-strip summary-strip-compact">
          <div>
            <span>Visible amount</span>
            <strong>{formatCurrency(totalAmount)}</strong>
          </div>
          <div>
            <span>Retryable</span>
            <strong>{retryQueue}</strong>
          </div>
        </div>

        <div className="toolbar">
          <label className="toolbar-search">
            <span>Search</span>
            <input
              type="search"
              value={query}
              onChange={(event) => {
                const value = event.currentTarget.value;
                startTransition(() => setQuery(value));
              }}
              placeholder="attempt, order, customer, provider"
            />
          </label>
          <div className="segmented-control" role="tablist" aria-label="Payment status filter">
            {["all", ...uniqueStatuses].map((value) => (
              <button
                key={value}
                className={statusFilter === value ? "segment-active" : ""}
                onClick={() => setStatusFilter(value)}
                type="button"
              >
                {value === "all" ? "All attempts" : humanize(value)}
              </button>
            ))}
          </div>
        </div>

        <div className="table-scroll">
          <table>
            <thead>
              <tr>
                <th>Attempt</th>
                <th>Order</th>
                <th>Customer</th>
                <th>Provider</th>
                <th>Amount</th>
                <th>At</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {visibleAttempts.map((attempt) => (
                <tr key={attempt.id}>
                  <td>
                    <strong>{attempt.id}</strong>
                    <div className="subcopy">
                      {attempt.retryable ? "retryable" : attempt.failure_reason ?? "closed"}
                    </div>
                  </td>
                  <td>{attempt.order_id}</td>
                  <td>{attempt.customer}</td>
                  <td>{attempt.provider}</td>
                  <td>{formatCurrency(attempt.amount)}</td>
                  <td>{formatDateTime(attempt.attempted_at)}</td>
                  <td>
                    <StatusBadge value={attempt.status} />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {visibleAttempts.length === 0 ? (
            <TableEmptyState
              body="결제 시도 상태나 검색어 조건을 조정해 주세요."
              title="표시할 결제 시도가 없습니다."
            />
          ) : null}
        </div>
      </section>
    </main>
  );
}
```

## `client/admin/src/lib/api.ts`

```ts
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? "/api/v1";

export type Metric = {
  label: string;
  value: string;
  delta: string;
};

export type AdminProduct = {
  id: string;
  title: string;
  category: string;
  price: number;
  inventory: number;
  stock_state: "stable" | "low";
  tags: string[];
};

export type AdminOrder = {
  id: string;
  customer: string;
  channel: string;
  status: string;
  total_amount: number;
  item_count: number;
};

export type PaymentAttempt = {
  id: string;
  order_id: string;
  customer: string;
  provider: string;
  status: string;
  amount: number;
  attempted_at: string;
  failure_reason: string | null;
  retryable: boolean;
};

export type DashboardPayload = {
  metrics: Metric[];
  highlight_order: AdminOrder;
  watchlist: string[];
};

export type AdminOperator = {
  email: string;
  name: string;
  role: string;
  scopes: string[];
};

export type AdminSession = {
  expires_at: string;
  operator: AdminOperator;
  source: "live" | "demo";
  token: string;
};

export type AdminSnapshot = {
  dashboard: DashboardPayload;
  dataMode: "live" | "hybrid" | "demo";
  notices: string[];
  orders: AdminOrder[];
  paymentAttempts: PaymentAttempt[];
  products: AdminProduct[];
};

export type AdminLoginCredentials = {
  email: string;
  password: string;
};

type SessionResponse = {
  access_token?: string;
  expires_at?: string;
  operator?: Partial<AdminOperator>;
  token?: string;
  user?: Partial<AdminOperator>;
};

type RequestOptions = {
  body?: unknown;
  method?: "GET" | "POST";
  token?: string;
};

export class ApiError extends Error {
  detail: unknown;
  status: number;

  constructor(message: string, status: number, detail?: unknown) {
    super(message);
    this.name = "ApiError";
    this.detail = detail;
    this.status = status;
  }
}

export const demoCredentials = {
  email: "ops@lecture.local",
  password: "lecture-admin-demo",
};

const demoProducts: AdminProduct[] = [
  {
    category: "Outer",
    id: "prod_hooded_shell",
    inventory: 6,
    price: 129000,
    stock_state: "low",
    tags: ["best", "spring", "navy"],
    title: "Field Shell Jacket",
  },
  {
    category: "Top",
    id: "prod_rib_tee",
    inventory: 14,
    price: 42000,
    stock_state: "stable",
    tags: ["new", "core"],
    title: "Rib Essential Tee",
  },
  {
    category: "Bottom",
    id: "prod_tapered_pants",
    inventory: 8,
    price: 86000,
    stock_state: "low",
    tags: ["restock", "uniform"],
    title: "Tapered Utility Pants",
  },
  {
    category: "Bag",
    id: "prod_canvas_tote",
    inventory: 18,
    price: 39000,
    stock_state: "stable",
    tags: ["merch", "lightweight"],
    title: "Canvas Daily Tote",
  },
];

const demoOrders: AdminOrder[] = [
  {
    channel: "web",
    customer: "Kim Sujin",
    id: "ord_240421_01",
    item_count: 3,
    status: "ready_to_ship",
    total_amount: 215000,
  },
  {
    channel: "instagram",
    customer: "Lee Minho",
    id: "ord_240421_02",
    item_count: 1,
    status: "payment_review",
    total_amount: 129000,
  },
  {
    channel: "web",
    customer: "Park Yejin",
    id: "ord_240421_03",
    item_count: 2,
    status: "packed",
    total_amount: 125000,
  },
  {
    channel: "offline",
    customer: "Choi Yura",
    id: "ord_240421_04",
    item_count: 4,
    status: "processing",
    total_amount: 344000,
  },
];

const demoPaymentAttempts: PaymentAttempt[] = [
  {
    amount: 215000,
    attempted_at: "2026-04-21T08:30:00.000Z",
    customer: "Kim Sujin",
    failure_reason: null,
    id: "pay_240421_01",
    order_id: "ord_240421_01",
    provider: "kakaopay",
    retryable: false,
    status: "paid",
  },
  {
    amount: 129000,
    attempted_at: "2026-04-21T09:10:00.000Z",
    customer: "Lee Minho",
    failure_reason: "3ds_timeout",
    id: "pay_240421_02",
    order_id: "ord_240421_02",
    provider: "tosspayments",
    retryable: true,
    status: "retry_required",
  },
  {
    amount: 125000,
    attempted_at: "2026-04-21T10:00:00.000Z",
    customer: "Park Yejin",
    failure_reason: null,
    id: "pay_240421_03",
    order_id: "ord_240421_03",
    provider: "naverpay",
    retryable: false,
    status: "authorized",
  },
  {
    amount: 344000,
    attempted_at: "2026-04-21T10:40:00.000Z",
    customer: "Choi Yura",
    failure_reason: "insufficient_funds",
    id: "pay_240421_04",
    order_id: "ord_240421_04",
    provider: "card",
    retryable: false,
    status: "failed",
  },
];

const demoDashboard: DashboardPayload = {
  highlight_order: demoOrders[0],
  metrics: [
    { delta: "+18%", label: "Gross Revenue", value: "813,000 KRW" },
    { delta: "+4", label: "Orders", value: "4" },
    { delta: "watch", label: "Low Stock SKU", value: "2" },
    { delta: "+7%", label: "AOV", value: "203,250 KRW" },
  ],
  watchlist: demoProducts
    .filter((product) => product.stock_state === "low")
    .map((product) => product.title),
};

async function request<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const headers = new Headers({
    Accept: "application/json",
  });

  if (options.body) {
    headers.set("Content-Type", "application/json");
  }

  if (options.token) {
    headers.set("Authorization", `Bearer ${options.token}`);
  }

  const response = await fetch(`${apiBaseUrl}${path}`, {
    body: options.body ? JSON.stringify(options.body) : undefined,
    headers,
    method: options.method ?? "GET",
  });

  const text = await response.text();
  const payload = text ? safelyParseJson(text) : null;

  if (!response.ok) {
    throw new ApiError(
      response.status === 401 || response.status === 403
        ? "관리자 세션이 만료되었거나 권한이 없습니다."
        : `admin_request_failed:${response.status}`,
      response.status,
      payload,
    );
  }

  return payload as T;
}

function safelyParseJson(value: string) {
  try {
    return JSON.parse(value) as unknown;
  } catch {
    return value;
  }
}

function isFallbackFriendly(error: unknown) {
  return (
    error instanceof TypeError ||
    (error instanceof ApiError && [404, 405, 501, 503].includes(error.status))
  );
}

function makeDemoSession(): AdminSession {
  const expiresAt = new Date();
  expiresAt.setHours(expiresAt.getHours() + 12);

  return {
    expires_at: expiresAt.toISOString(),
    operator: {
      email: demoCredentials.email,
      name: "Lecture Operator",
      role: "admin",
      scopes: ["dashboard:read", "products:read", "orders:read", "payments:read"],
    },
    source: "demo",
    token: "lecture-demo-session-token",
  };
}

function normalizeLiveSession(payload: SessionResponse): AdminSession {
  const operatorSeed = payload.operator ?? payload.user ?? {};
  const token = payload.token ?? payload.access_token;

  if (!token) {
    throw new Error("세션 응답에 token 이 없습니다.");
  }

  return {
    expires_at: payload.expires_at ?? new Date(Date.now() + 12 * 60 * 60 * 1000).toISOString(),
    operator: {
      email: operatorSeed.email ?? demoCredentials.email,
      name: operatorSeed.name ?? "Admin Operator",
      role: operatorSeed.role ?? "admin",
      scopes: operatorSeed.scopes ?? ["dashboard:read"],
    },
    source: "live",
    token,
  };
}

async function loadDataset<T>(
  load: () => Promise<T>,
  fallback: T,
  notice: string,
  allowFallback: boolean,
) {
  try {
    return { notice: null, payload: await load(), usedFallback: false };
  } catch (error) {
    if (allowFallback && isFallbackFriendly(error)) {
      return { notice, payload: fallback, usedFallback: true };
    }

    throw error;
  }
}

export async function loginAdmin(credentials: AdminLoginCredentials): Promise<AdminSession> {
  try {
    const payload = await request<SessionResponse>("/admin/session", {
      body: credentials,
      method: "POST",
    });
    return normalizeLiveSession(payload);
  } catch (error) {
    if (
      isFallbackFriendly(error) &&
      credentials.email === demoCredentials.email &&
      credentials.password === demoCredentials.password
    ) {
      return makeDemoSession();
    }

    if (error instanceof ApiError && [401, 403].includes(error.status)) {
      throw new Error("이메일 또는 비밀번호가 올바르지 않습니다.");
    }

    if (isFallbackFriendly(error)) {
      throw new Error("현재는 demo fallback 계정으로만 로그인할 수 있습니다.");
    }

    throw error;
  }
}

export async function fetchAdminSnapshot(session: AdminSession): Promise<AdminSnapshot> {
  const allowSeedFallback = session.source === "demo";

  const [dashboard, products, orders, paymentAttempts] = await Promise.all([
    loadDataset(
      () => request<DashboardPayload>("/admin/dashboard", { token: session.token }),
      demoDashboard,
      "Dashboard endpoint unavailable. Showing seeded lecture metrics.",
      allowSeedFallback,
    ),
    loadDataset(
      async () =>
        (await request<{ items: AdminProduct[] }>("/admin/products", {
          token: session.token,
        })).items,
      demoProducts,
      "Product endpoint unavailable. Showing seeded catalog inventory.",
      allowSeedFallback,
    ),
    loadDataset(
      async () =>
        (await request<{ items: AdminOrder[] }>("/admin/orders", {
          token: session.token,
        })).items,
      demoOrders,
      "Order endpoint unavailable. Showing seeded operational orders.",
      allowSeedFallback,
    ),
    loadDataset(
      async () =>
        (await request<{ items: PaymentAttempt[] }>("/admin/payment-attempts", {
          token: session.token,
        })).items,
      demoPaymentAttempts,
      "Payment attempts endpoint unavailable. Showing prototype attempt feed until backend wiring lands.",
      true,
    ),
  ]);

  const notices = [dashboard.notice, products.notice, orders.notice, paymentAttempts.notice].filter(
    (notice): notice is string => Boolean(notice),
  );
  const fallbackCount = [dashboard, products, orders, paymentAttempts].filter(
    (dataset) => dataset.usedFallback,
  ).length;

  return {
    dashboard: dashboard.payload,
    dataMode:
      fallbackCount === 0 ? "live" : fallbackCount === 4 ? "demo" : "hybrid",
    notices,
    orders: orders.payload,
    paymentAttempts: paymentAttempts.payload,
    products: products.payload,
  };
}
```

## `client/admin/src/styles/main.css`

```css
:root {
  color-scheme: light;
  font-family: "Manrope", "Pretendard", "Noto Sans KR", sans-serif;
  line-height: 1.5;
  font-weight: 400;
  background:
    radial-gradient(circle at top left, rgba(255, 173, 92, 0.22), transparent 22%),
    radial-gradient(circle at top right, rgba(115, 156, 255, 0.2), transparent 26%),
    linear-gradient(180deg, #e8edf3 0%, #dce4ee 100%);
  color: #142033;
  --bg-deep: #102237;
  --bg-panel: rgba(255, 255, 255, 0.78);
  --bg-panel-strong: rgba(255, 255, 255, 0.92);
  --border: rgba(20, 32, 51, 0.1);
  --ink: #142033;
  --muted: #67758a;
  --primary: #163657;
  --primary-strong: #102746;
  --accent: #f48d46;
  --success: #17795f;
  --warning: #b9691b;
  --danger: #bf4a43;
  --shadow: 0 24px 72px rgba(20, 32, 51, 0.14);
}

* {
  box-sizing: border-box;
}

html,
body,
#root {
  min-height: 100%;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
  color: var(--ink);
}

button,
input {
  font: inherit;
}

a {
  color: inherit;
  text-decoration: none;
}

.boot-splash {
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-size: 1.05rem;
  color: var(--muted);
}

.login-shell,
.admin-shell {
  min-height: 100vh;
}

.login-shell {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(320px, 460px);
  gap: 24px;
  padding: 28px;
}

.login-hero,
.login-panel,
.rail,
.panel,
.loading-panel {
  border: 1px solid var(--border);
  border-radius: 30px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(18px);
}

.login-hero {
  position: relative;
  overflow: hidden;
  padding: 40px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background:
    linear-gradient(135deg, rgba(16, 34, 55, 0.95), rgba(29, 58, 92, 0.82)),
    linear-gradient(180deg, rgba(255, 255, 255, 0.12), transparent);
  color: white;
}

.login-hero::after {
  content: "";
  position: absolute;
  inset: auto -10% -20% auto;
  width: 280px;
  height: 280px;
  border-radius: 999px;
  background: radial-gradient(circle, rgba(244, 141, 70, 0.42), transparent 68%);
}

.login-hero h1,
.login-panel h2,
.workspace-header h2,
.panel h3 {
  margin: 8px 0 0;
  letter-spacing: -0.05em;
}

.login-hero h1 {
  max-width: 10ch;
  font-size: clamp(2.8rem, 5vw, 5rem);
}

.lead-copy {
  max-width: 56ch;
  color: rgba(255, 255, 255, 0.78);
  font-size: 1.05rem;
}

.login-feature-list {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.feature-chip,
.surface-tag {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 9px 12px;
  font-size: 0.82rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.feature-chip {
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.12);
}

.surface-tag {
  background: rgba(22, 54, 87, 0.08);
  border: 1px solid rgba(22, 54, 87, 0.12);
  color: #35506f;
}

.login-panel {
  padding: 28px;
  background: var(--bg-panel-strong);
}

.panel-header,
.workspace-header,
.panel-header-spaced {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.login-form {
  display: grid;
  gap: 18px;
  margin-top: 24px;
}

.login-form label,
.toolbar-search {
  display: grid;
  gap: 8px;
}

.login-form span,
.toolbar-search span {
  color: var(--muted);
  font-size: 0.86rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.login-form input,
.toolbar-search input {
  width: 100%;
  border: 1px solid rgba(20, 32, 51, 0.12);
  border-radius: 18px;
  padding: 14px 16px;
  background: rgba(255, 255, 255, 0.92);
  color: var(--ink);
}

.primary-button,
.ghost-button,
.ghost-link,
.segmented-control button {
  border: 0;
  cursor: pointer;
  transition:
    transform 160ms ease,
    background-color 160ms ease,
    color 160ms ease,
    opacity 160ms ease;
}

.primary-button:hover,
.ghost-button:hover,
.ghost-link:hover,
.segmented-control button:hover,
.nav-link:hover {
  transform: translateY(-1px);
}

.primary-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 18px;
  padding: 14px 18px;
  background: linear-gradient(135deg, var(--primary), var(--primary-strong));
  color: white;
  font-weight: 700;
}

.primary-button:disabled {
  opacity: 0.7;
  cursor: wait;
}

.ghost-button,
.ghost-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 18px;
  padding: 12px 16px;
  background: rgba(22, 54, 87, 0.08);
  color: var(--primary);
}

.demo-credentials,
.rail-card {
  margin-top: 24px;
  display: grid;
  gap: 6px;
  padding: 18px;
  border-radius: 22px;
  background: rgba(16, 34, 55, 0.04);
}

.demo-credentials strong,
.rail-card strong {
  font-size: 1.08rem;
}

.demo-credentials span,
.rail-card span {
  color: var(--muted);
}

.form-error,
.error-banner {
  color: #952c24;
}

.form-error {
  margin: 0;
}

.admin-shell {
  display: grid;
  grid-template-columns: 320px minmax(0, 1fr);
  gap: 18px;
  padding: 18px;
}

.rail {
  position: sticky;
  top: 18px;
  align-self: start;
  display: grid;
  gap: 22px;
  min-height: calc(100vh - 36px);
  padding: 28px;
  background:
    linear-gradient(180deg, rgba(16, 34, 55, 0.96), rgba(23, 43, 69, 0.92)),
    radial-gradient(circle at bottom left, rgba(244, 141, 70, 0.2), transparent 34%);
  color: rgba(255, 255, 255, 0.92);
}

.rail-brand p,
.rail-brand h1,
.rail-brand span,
.rail-brand strong {
  margin: 0;
}

.rail-brand h1 {
  margin-top: 8px;
  font-size: 2.1rem;
}

.rail-brand p:last-child {
  margin-top: 12px;
  color: rgba(255, 255, 255, 0.64);
}

.nav-stack {
  display: grid;
  gap: 10px;
}

.nav-link {
  display: flex;
  align-items: center;
  min-height: 52px;
  padding: 0 16px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 18px;
  color: rgba(255, 255, 255, 0.7);
  background: rgba(255, 255, 255, 0.03);
}

.nav-link-active {
  background: rgba(255, 255, 255, 0.12);
  color: white;
}

.workspace {
  display: grid;
  gap: 16px;
  align-content: start;
  padding: 8px 4px 28px;
}

.workspace-header {
  padding: 14px 10px 0;
}

.workspace-content {
  display: grid;
  gap: 16px;
}

.header-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
}

.meta-line,
.error-banner,
.info-banner {
  margin: 0;
  padding: 0 10px;
}

.meta-line {
  color: var(--muted);
  font-size: 0.94rem;
}

.error-banner,
.info-banner {
  border-radius: 22px;
  padding: 14px 18px;
}

.error-banner {
  background: rgba(191, 74, 67, 0.1);
}

.info-banner {
  background: rgba(22, 54, 87, 0.07);
  color: #244361;
}

.loading-panel,
.panel {
  background: var(--bg-panel);
}

.loading-panel,
.panel,
.section-panel {
  padding: 24px;
}

.metrics-grid,
.hero-panels,
.panel-cluster,
.insight-grid {
  display: grid;
  gap: 16px;
}

.metrics-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.hero-panels,
.panel-cluster {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.metric-card {
  padding: 22px;
  border: 1px solid var(--border);
  border-radius: 24px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.88), rgba(245, 248, 252, 0.84));
  box-shadow: var(--shadow);
}

.metric-card p,
.metric-card span,
.subcopy,
.table-empty-state p,
.insight-tile p,
.watchlist li,
.status-badge {
  color: var(--muted);
}

.metric-card p,
.metric-card span,
.watchlist,
.detail-grid dt,
.detail-grid dd {
  margin: 0;
}

.metric-card strong,
.insight-tile strong {
  display: block;
  margin: 12px 0 10px;
  font-size: clamp(1.7rem, 2.6vw, 2.2rem);
  letter-spacing: -0.05em;
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin: 18px 0 0;
}

.detail-grid div,
.insight-tile {
  padding: 16px;
  border-radius: 20px;
  background: rgba(16, 34, 55, 0.05);
}

.detail-grid dt {
  font-size: 0.86rem;
  color: var(--muted);
}

.detail-grid dd {
  margin-top: 6px;
  font-weight: 700;
}

.watchlist {
  padding-left: 18px;
  display: grid;
  gap: 10px;
}

.toolbar,
.summary-strip,
.segmented-control {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.toolbar {
  align-items: end;
  justify-content: space-between;
  margin: 22px 0 18px;
}

.toolbar-search {
  min-width: min(100%, 320px);
}

.segmented-control {
  align-items: center;
  padding: 6px;
  border-radius: 20px;
  background: rgba(20, 32, 51, 0.06);
}

.segmented-control button {
  border-radius: 16px;
  padding: 10px 14px;
  background: transparent;
  color: var(--muted);
}

.segmented-control .segment-active {
  background: white;
  color: var(--primary);
  box-shadow: 0 10px 24px rgba(20, 32, 51, 0.08);
}

.summary-strip {
  margin-bottom: 16px;
}

.summary-strip div {
  min-width: 140px;
  padding: 16px 18px;
  border-radius: 20px;
  background: rgba(16, 34, 55, 0.05);
}

.summary-strip span,
.insight-tile span {
  display: block;
  color: var(--muted);
}

.summary-strip strong {
  display: block;
  margin-top: 8px;
  font-size: 1.5rem;
  letter-spacing: -0.05em;
}

.summary-strip-compact {
  margin-top: 20px;
}

.table-scroll {
  overflow-x: auto;
}

table {
  width: 100%;
  min-width: 760px;
  border-collapse: collapse;
}

th,
td {
  padding: 15px 12px;
  border-bottom: 1px solid rgba(20, 32, 51, 0.08);
  text-align: left;
  vertical-align: top;
}

th {
  color: var(--muted);
  font-size: 0.8rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.table-empty-state {
  padding: 18px 4px 0;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(20, 32, 51, 0.06);
  text-transform: capitalize;
}

.status-success {
  background: rgba(23, 121, 95, 0.12);
  color: var(--success);
}

.status-warning {
  background: rgba(185, 105, 27, 0.14);
  color: var(--warning);
}

.status-danger {
  background: rgba(191, 74, 67, 0.14);
  color: var(--danger);
}

.status-neutral {
  color: #40536d;
}

.eyebrow {
  margin: 0;
  color: #5a78a0;
  font-size: 0.78rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-weight: 800;
}

.rail .eyebrow {
  color: rgba(255, 255, 255, 0.56);
}

@media (max-width: 1240px) {
  .login-shell {
    grid-template-columns: 1fr;
  }

  .admin-shell {
    grid-template-columns: 1fr;
  }

  .rail {
    position: static;
    min-height: auto;
  }

  .metrics-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 760px) {
  .login-shell,
  .admin-shell {
    padding: 14px;
  }

  .login-hero,
  .login-panel,
  .rail,
  .panel,
  .loading-panel {
    border-radius: 24px;
  }

  .login-hero,
  .login-panel,
  .rail,
  .panel,
  .loading-panel,
  .section-panel {
    padding: 20px;
  }

  .workspace-header,
  .panel-header,
  .panel-header-spaced,
  .toolbar {
    flex-direction: column;
    align-items: flex-start;
  }

  .header-actions {
    justify-content: flex-start;
  }

  .metrics-grid,
  .hero-panels,
  .panel-cluster,
  .detail-grid {
    grid-template-columns: 1fr;
  }

  .login-hero h1 {
    font-size: clamp(2.2rem, 10vw, 3.8rem);
  }
}
```
