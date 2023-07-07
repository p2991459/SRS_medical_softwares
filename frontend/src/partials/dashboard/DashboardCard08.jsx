import React from "react";
import DocViewer from "react-doc-viewer";

function DashboardCard08() {
  const ViewData = localStorage.getItem("ViewPdf");
 

  return (
    <div className="flex flex-col col-span-full sm:col-span-6 bg-white dark:bg-slate-800 shadow-lg rounded-sm border border-slate-200 dark:border-slate-700">
      <div className="pdf-container">
        <iframe 
          className="rounded-lg"
          src={ViewData}
          width="100%"
          height="635px"
        />
        
      </div>
    </div>
  );
}

export default DashboardCard08;
