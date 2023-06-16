from PyPDF2 import PdfReader
import os
# from openai_text_formatter import openai_text_formatter

# from langchain.text_splitter import CharacterTextSplitter

def pdfExtractor():
    current_file_path = os.getcwd()
    print(current_file_path)
    filepath = f"{current_file_path}\static\SRS.pdf"
    print(filepath)
    reader = PdfReader(filepath)
    raw_text = ''
    formatted_text = ''
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            # prompt = f"Reformat the below text\n\nRaw Text: {text}"
            # o_text = openai_text_formatter(prompt)
            # print(o_text)
            # formatted_text += openai_text_formatter(prompt)
            raw_text+=text


    open("raw_text.txt","w",encoding="utf-8").write(str(raw_text))
    open("formatted_text.txt","w",encoding="utf-8").write(str(formatted_text))
    return raw_text
