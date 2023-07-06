import React, { useEffect } from 'react';
import {
  Routes,
  Route,
  useLocation
} from 'react-router-dom';
import './css/style.css';
// Import pages
import Dashboard from './pages/Dashboard';
import ChatPDFUploader from './GeneratePages/ChatPDFUploader ';
import DashboardCard09 from './partials/dashboard/DashboardCard09';

function App() {

  const location = useLocation();

  useEffect(() => {
    document.querySelector('html').style.scrollBehavior = 'auto'
    window.scroll({ top: 0 })
    document.querySelector('html').style.scrollBehavior = ''
  }, [location.pathname]); // triggered on route change

  return (
    <>
      <Routes>
        <Route exact path="/" element={<ChatPDFUploader />} />
        <Route exact path="/chat" element={<Dashboard />} />
      </Routes>
    </>
  );
}

export default App;
