import React, { useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import "./ChatPDFUploader .css";

function ChatPDFUploader() {
  const navigate = useNavigate();
  const [pdfFile, setPdfFile] = useState("");
  const [uploadProgress, setUploadProgress] = useState(0);
  const fileInputRef = useRef(null);

  const handlePdfFileChange = (e) => {
    let selectedFile = e.target.files[0];
    setPdfFile(selectedFile);
    // console.log("selectedFile", selectedFile);
  };

  const handlePdfFileSubmit = (e) => {
    e.preventDefault();

    var formdata = new FormData();
    formdata.append("file", pdfFile);

    // console.log("formdata",formdata)

    const interval = setInterval(() => {
      setUploadProgress((prevProgress) => prevProgress + 10);
    }, 500);

    setTimeout(() => {
      var requestOptions = {
        method: "POST",
        body: formdata,
      };

      // console.log("formdata",requestOptions)

      fetch("http://127.0.0.1:8000/api/uploadDoc", requestOptions)
        .then((response) => response.json())
        .then((data) => {
          //   console.log("first",data)
          if (data.message === "File uploaded successfully") {
            //-------- Convert docx to pdf ----------//
            var requestOptions = {
              method: "GET",
              redirect: "follow",
            };
            fetch("http://127.0.0.1:8000/api/DocToPdf", requestOptions)
              .then((response) => response.json())
              .then((data) => {
                console.log("ConvertPdf", data.message);
                if (data.message === true) {
                  clearInterval(interval);
                  setUploadProgress(0);
                  localStorage.setItem("ViewPdf", data.pdf_path);
                  localStorage.setItem("PdfName", pdfFile.name);
                  navigate("/chat");
                }
              })
              .catch((error) => {
                console.log("Error:", error);
              });
          }
        })
        .catch((error) => {
          console.log("error", error);
        });
    }, 5000);
  };

  const isFileSelected = pdfFile !== "";

  return (
    <div>
      <picture>
        <source type="image/avif" srcSet="/bg.avif" />
        <img
          loading="lazy"
          src="bg.avif"
          alt="background"
          width="100%"
          height="100%"
          style={{ position: "fixed", zIndex: -1, height: "100vh" }}
        />
      </picture>
      <div className="padding">
        <header style={{ margin: "36px 0px 48px" }}>
          <h1
            className="ant-typography css-w8mnev"
            style={{
              fontWeight: 600,
              fontSize: "46px",
              textAlign: "center",
              padding: 0,
              margin: "0px 0px 12px",
              color: "black",
            }}
          >
            Chat with any PDF
          </h1>
          <div
            className="header-buttons"
            style={{
              display: "flex",
              justifyContent: "center",
              margin: 0,
              gap: "8px",
            }}
          >
            <button
              type="button"
              className="ant-btn css-w8mnev ant-btn-default"
              style={{ display: "flex", gap: "6px", alignItems: "center" }}
            >
              <svg
                fill="currentColor"
                xmlns="http://www.w3.org/2000/svg"
                width="16.5"
                height="14"
                viewBox="0 0 127.14 96.36"
              >
                <path d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.7,77.7,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.25,105.25,0,0,0,126.6,80.22h0C129.24,52.84,122.09,29.11,107.7,8.07ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,46,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,46,96.12,53,91.08,65.69,84.69,65.69Z"></path>
              </svg>
              <div>Join Discord</div>
            </button>
            <button
              type="button"
              className="ant-btn css-w8mnev ant-btn-default"
              style={{ display: "flex", gap: "6px", alignItems: "center" }}
            >
              <span
                role="img"
                aria-label="twitter-circle"
                className="anticon anticon-twitter-circle"
              >
                <svg
                  viewBox="64 64 896 896"
                  focusable="false"
                  data-icon="twitter-circle"
                  width="1em"
                  height="1em"
                  fill="currentColor"
                  aria-hidden="true"
                >
                  <path d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32zm-92.4 233.5h-63.9c-50.1 0-59.8 23.8-59.8 58.8v77.1h119.6l-15.6 120.7h-104V912H539.2V602.2H434.9V481.4h104.3v-89c0-103.3 63.1-159.6 155.3-159.6 44.2 0 82.1 3.3 93.2 4.8v107.9z"></path>
                </svg>
              </span>
              <div>Post to Twitter</div>
            </button>
            <button
              type="button"
              className="ant-btn css-w8mnev ant-btn-default desktop-only flex"
              style={{ display: "flex", gap: "6px", alignItems: "center" }}
            >
              <span
                role="img"
                aria-label="facebook"
                className="anticon anticon-facebook"
              >
                <svg
                  viewBox="64 64 896 896"
                  focusable="false"
                  data-icon="facebook"
                  width="1em"
                  height="1em"
                  fill="currentColor"
                  aria-hidden="true"
                >
                  <path d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32zm-92.4 233.5h-63.9c-50.1 0-59.8 23.8-59.8 58.8v77.1h119.6l-15.6 120.7h-104V912H539.2V602.2H434.9V481.4h104.3v-89c0-103.3 63.1-159.6 155.3-159.6 44.2 0 82.1 3.3 93.2 4.8v107.9z"></path>
                </svg>
              </span>
              <div>Share on Facebook</div>
            </button>
          </div>
        </header>

        <div className="container mx-auto px-4 upload-box">
          <form onSubmit={handlePdfFileSubmit}>
            <input
              className="file-input"
              type="file"
              name="file"
              hidden
              ref={fileInputRef}
              accept=".doc, .docx, .pdf"
              onChange={handlePdfFileChange}
            />
            <div className="icon" onClick={() => fileInputRef.current.click()}>
              <img
                src="https://www.ezcopy.net/wp-content/uploads/2018/02/upload-1.png"
                alt="Upload"
              />
            </div>
            <p>Browser pdf to upload</p>
            <h6>Pdf Name :{pdfFile.name}</h6>
            {uploadProgress > 0 && uploadProgress < 100 && (
              <progress value={uploadProgress} max="100" />
            )}
            <br />
            <button
              type="submit"
              disabled={!isFileSelected}
              style={{
                backgroundColor: "#54aedd",
                padding: "8px",
                width: "130px",
                color: "white",
                borderRadius: "5px",
              }}
            >
              UPLOAD
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default ChatPDFUploader;
