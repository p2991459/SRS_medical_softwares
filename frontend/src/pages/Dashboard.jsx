import React, { useState } from "react";

import Sidebar from "../partials/Sidebar";
import Header from "../partials/Header";

import DashboardCard08 from "../partials/dashboard/DashboardCard08";
import DashboardCard09 from "../partials/dashboard/DashboardCard09";


function Dashboard() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [responsedData, setresponsedData] = useState("");
  const [showDownload, setShowDownload] = useState("");


  const getResponseData = (data) =>{
      setresponsedData(data)
  }

  const showDownloadButton = (data) =>{
      setShowDownload(data)
  }

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Sidebar */}
      <Sidebar sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} getResponseData={getResponseData} showDownloadButton={showDownloadButton} />

      {/* Content area */}
      <div className="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
        {/*  Site header */}
        <Header sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />

        <main>
          <div className="w-full max-w-9xl mx-auto">

            {/* Dashboard actions */}
            <div className="sm:flex sm:justify-between sm:items-center">
              <div className="grid grid-flow-col sm:auto-cols-max justify-start sm:justify-end gap-2"></div>
            </div>

            {/* Cards */}
            <div className="grid grid-cols-12 gap-2">
              <DashboardCard08 />
              <DashboardCard09 responsedData={responsedData}  showDownload={showDownload} />
            </div>
          </div>
        </main>

      </div>
    </div>
  );
}

export default Dashboard;
