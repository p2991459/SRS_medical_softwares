from flask import Flask, request, jsonify
from raw_text_from_pdf import pdfExtractor
from deficiencies_mapper import get_deficiencies
from werkzeug.utils import secure_filename
from  update_deficiencies import update_deficiencies
import tiktoken
app = Flask(__name__)
import os
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/api/uploadPdf', methods=['POST'])
def uploadPdf():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    # Check if the file has a valid filename
    if file.filename == '':
        return 'Empty filename', 400
    # Check if the file extension is allowed
    if not allowed_file(file.filename):
        return 'Invalid file extension', 400
    # Save the file with a secure filename to the UPLOAD_FOLDER
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "SRS.pdf"))
    return 'File uploaded successfully'


@app.route('/api/extractPdf', methods=['GET', 'POST'])
def extractor():
    text= pdfExtractor()
    return jsonify({"text": text})

@app.route('/api/deficiancies', methods=['GET', 'POST'])
def deficiancies():
    SRS_Text = open("raw_text.txt").read()
    output = get_deficiencies(SRS_Text)
    open("issues.txt", "w", encoding="utf-8").write(output)
    return jsonify({"deficiencies_found": output})

@app.route('/api/updateDoc', methods=['GET', 'POST'])
def updateDoc():
    SRS_Text = open("raw_text.txt").read()
    tt_encoding = tiktoken.get_encoding("cl100k_base")
    tokens = tt_encoding.encode(SRS_Text)
    ChunkSize = 2000
    chunks = [tokens[0:2000], tokens[2000:-1]]
    issues = open("issues.txt").read()

    prompt = f'''SRS_DOC: {SRS_Text}\nDeficiencies: {issues}'''
    output = ''
    for chunk in chunks:
        decoded_text = tt_encoding.decode(chunk)
        output += update_deficiencies(f'''SRS_DOC: {decoded_text}\nDeficiencies: {issues}''')
        print(output)
    open("final_output.txt", "w", encoding="utf-8").write(output)
    print(output)
    return jsonify({"updated_doc": output})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True)


