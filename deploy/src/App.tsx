import { HubPage } from './pages/HubPage';
import { SrapBridgePage } from './pages/SrapBridgePage';
import { SRAP_ROUTES } from './pages/routes';

function App() {
  const path = window.location.pathname;
  if (SRAP_ROUTES.has(path)) {
    return <SrapBridgePage />;
  }

  return <HubPage />;
}

export default App;
