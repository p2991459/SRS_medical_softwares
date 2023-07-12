import React, { useEffect, useState, useRef } from "react";
import "./DashboardCard09.css";

function DashboardCard09({
  responsedData,
  showDownload,
  cardComponentData,
  progressComponent,
}) {
  const DocumentData = localStorage.getItem("Docx");

  const points = responsedData.split(/\d+\.\s/).filter(Boolean);

  let formattedList = [];
  let headerTxt = "";
  for (let i = 0; i < points.length; i++) {
    if (i > 0) {
      const listItem = <li>{points[i]}</li>;
      formattedList.push(listItem);
    } else {
      headerTxt = points[0];
    }
  }
  // console.log("orderedList", formattedList);

  const [modalOpen, setModalOpen] = useState(false);
  const chatContainerRef = useRef(null);

  useEffect(() => {
    // console.log("cardComponentData",cardComponentData)
    if (cardComponentData === true) {
      setModalOpen(true);
      setTimeout(() => {
        setModalOpen(false);
      }, 198000); // Close the modal after 3 seconds (adjust the time as needed)
    }
  }, [cardComponentData]);

  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [responsedData]);

  // const handleWindow = () => {
  //   window.open('http://127.0.0.1:8000/api/log_stream', '_blank');
  // }

  return (
    <div>
      {/* loader middle chat  */}
      {progressComponent === true ? (
        <div className="absolute top-1/2 left-1/2 -mt-4 -ml-2 h-8 w-4 text-indigo-700">
          <div className="absolute z-10 ml-64 mt-18 h-8 w-8">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="animate-spin"
              fill="currentColor"
              stroke="currentColor"
              stroke-width="0"
              viewBox="0 0 16 16"
            >
              <path d="M8 0c-4.418 0-8 3.582-8 8s3.582 8 8 8 8-3.582 8-8-3.582-8-8-8zM8 4c2.209 0 4 1.791 4 4s-1.791 4-4 4-4-1.791-4-4 1.791-4 4-4zM12.773 12.773c-1.275 1.275-2.97 1.977-4.773 1.977s-3.498-0.702-4.773-1.977-1.977-2.97-1.977-4.773c0-1.803 0.702-3.498 1.977-4.773l1.061 1.061c0 0 0 0 0 0-2.047 2.047-2.047 5.378 0 7.425 0.992 0.992 2.31 1.538 3.712 1.538s2.721-0.546 3.712-1.538c2.047-2.047 2.047-5.378 0-7.425l1.061-1.061c1.275 1.275 1.977 2.97 1.977 4.773s-0.702 3.498-1.977 4.773z"></path>
            </svg>
            <p className="text-xs -ml-4">Deficiencies</p>
          </div>
          <div
            className="absolute top-4 h-5 w-4 animate-bounce border-l-2 border-gray-200"
            style={{ rotate: "-90deg" }}
          ></div>
          <div
            className="absolute top-4 h-5 w-4 animate-bounce border-r-2 border-gray-200"
            style={{ rotate: "90deg" }}
          ></div>
        </div>
      ) : (
        ""
      )}
      {/* loader middle chat  */}

      <div className="container mx-auto" style={{ width: "538px" }}>
        <div className="max-w-2xl border rounded">
          <div className="">
            <div className="">
              <div className="relative flex items-center p-3 border-b border-gray-300">
                <img
                  className="object-cover w-10 h-10 rounded-full"
                  src="https://cdn.pixabay.com/photo/2018/01/15/07/51/woman-3083383__340.jpg"
                  alt="username"
                />
                <span className="block ml-2 font-bold text-gray-600">Emma</span>
                <span className="absolute w-3 h-3 bg-green-600 rounded-full left-10 top-3"></span>
              </div>
              <div
                className="relative w-full p-6 overflow-y-auto h-[31rem]"
                ref={chatContainerRef}
              >
                <ul className="space-y-2">
                  <li className="flex justify-start">
                    <div className="relative max-w-xl px-4 py-2 text-gray-700 rounded">
                      {/* <p className="block">{responsedData}</p> */}
                      <strong>{headerTxt}</strong>
                      <br />
                      <br />
                      <ol className="list">{formattedList}</ol>
                      <br />
                      <br />
                      {showDownload ? (
                        //------  chat show button ------//
                        <a
                          href={DocumentData}
                          className="text-blue-950 border-dashed border-blue-700 border-2 p-2 bg-slate rounded-md relative"
                          target="_blank"
                          rel="noopener noreferrer"
                        >
                          Download Docx
                        </a>
                      ) : (
                        //------  chat show button ------//
                        ""
                      )}
                    </div>
                  </li>
                  {/* li data is chat */}
                </ul>
                {modalOpen && (
                  <div className="fixed top-0 left-0 right-0 inset-0 flex items-center justify-center">
                    <div className="w-96  max-w-xl">
                      <div className="bg-white rounded-lg shadow">
                        <div className="flex items-start justify-between p-4 border-b rounded-t">
                          <h3 className="text-xl font-semibold text-gray-900 ">
                            Updating SRS Document...
                          </h3>
                          <button
                            type="button"
                            className="text-gray-600 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center"
                            onClick={() => setModalOpen(false)}
                          >
                            <svg
                              className="w-3 h-3"
                              aria-hidden="true"
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 14 14"
                            >
                              <path
                                stroke="currentColor"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                              />
                            </svg>
                            <span className="sr-only">Close modal</span>
                          </button>
                        </div>
                        <div className="p-6 space-y-6">
                          <p className="text-base leading-relaxed text-gray-500">
                            <div class="bg-gray-200 h-4 w-full rounded relative">
                              <div class="h-full rounded absolute animate-progress"></div>
                            </div>
                          </p>
                          <p className="text-base leading-relaxed text-red-500 text-center">
                            Updating the Docx through AI is a long
                            <br /> process. It can take upto 3-5 min.
                          </p>
                          <div class="flex justify-center">
                            <button
                              type="button"
                              class="text-white bg-blue-500 hover:bg-blue-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                              onClick={() =>
                                window.open(
                                  "http://127.0.0.1:8000/api/log_stream",
                                  "_blank"
                                )
                              }
                              target="_blank"
                            >
                              Check logs
                            </button>
                          </div>
                          <p className="-mb-7 font-semibold text-center">
                            You can download the updated doc once updating
                            process is finished
                          </p>
                        </div>

                        {showDownload ? (
                          <div className="flex justify-center p-6 space-x-2 border-t border-gray-200 rounded-b">
                            <a
                              href={DocumentData}
                              className="text-blue-900 border-dashed border-blue-700 border-2 p-2 bg-slate rounded-md relative text-center"
                              target="_blank"
                              rel="noopener noreferrer"
                            >
                              Download Docx
                            </a>
                          </div>
                        ) : (
                          ""
                        )}
                      </div>
                    </div>
                  </div>
                )}
              </div>

              <div className="flex items-center justify-between w-full p-3 border-t border-gray-300">
                <button>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="w-6 h-6 text-gray-500"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                </button>
                <button>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="w-5 h-5 text-gray-500"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"
                    />
                  </svg>
                </button>

                <input
                  type="text"
                  placeholder="Message"
                  className="block w-full py-2 pl-4 mx-3 bg-gray-100 rounded-full outline-none focus:text-gray-700"
                  name="message"
                  required
                />
                <button>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="w-5 h-5 text-gray-500"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"
                    />
                  </svg>
                </button>
                <button type="submit">
                  <svg
                    className="w-5 h-5 text-gray-500 origin-center transform rotate-90"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default DashboardCard09;