from fastapi import BackgroundTasks
from fastapi.staticfiles import StaticFiles
from docx2pdf import convert
import logging
import docExtractors
import os
from openAIModules.deficiencies_mapper import get_deficiencies
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from docMaker import DocAI


logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
HOST_URL = "http://localhost:8000"

BASE_PATH = os.getcwd()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# Dictionary to store tasks
tasks = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


ALLOWED_EXTENSIONS = {"pdf","docx"}

# Define upload folder
UPLOAD_FOLDER = "static"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.post('/api/uploadDoc')
async def upload_doc(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail='No file uploaded')
    if file.filename == '':
        raise HTTPException(status_code=400, detail='Empty filename')
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail='Invalid file extension')

    # Save the file with a secure filename to the UPLOAD_FOLDER
    file_path = Path(UPLOAD_FOLDER) / "SRS.docx"
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)

    return {"message":'File uploaded successfully'}

@app.get("/api/deficiencies")
def deficiancies():
    SRS_Text = docExtractors.extractDoc(f"{BASE_PATH}/static/SRS.docx")
    output = get_deficiencies(SRS_Text)
    open("issues.txt", "w", encoding="utf-8").write(output)
    return {"deficiencies_found": output}


@app.get("/api/updateDoc")
async def DocUpdate(background_tasks: BackgroundTasks):
    docAI = DocAI()
    background_tasks.add_task(docAI.updateDoc)
    return {"message": "Updating the SRS DOC"}

@app.get('/api/check_file_status')
def check_file_status():
    directory = 'static'
    files = os.listdir(directory)
    latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(directory, f)))
    file_path = os.path.join('static', 'output_document.docx')  # Adjust the file name and extension
    file_path_error = os.path.join('static', 'error.txt')
    if os.path.exists(file_path) or os.path.exists(file_path_error):
        return {'file_created': True,'file_name': latest_file}
    else:
        return {'file_created': False}

@app.get('/api/DocToPdf')
async def converter():
    try:
        convert(f'{BASE_PATH}/static/SRS.docx',f"{BASE_PATH}/static/SRS.pdf")
        return {"message": True,"pdf_path": f"{HOST_URL}/static/SRS.pdf"}
    except Exception as e:
        return {'message': f'Conversion failed: {str(e)}'}



