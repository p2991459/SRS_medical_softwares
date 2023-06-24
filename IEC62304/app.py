from flask import Flask, request, jsonify,Response
import sys
sys.path.append('H:\myprojects\medical_softwares')
import docExtractors
from docx import Document
import GPTs
app = Flask(__name__)
import os


@app.route('/api/updateDoc', methods=['GET', 'POST'])
def updateDoc():
    def generate():
        input_file = 'SRS.docx'
        # output_file = 'output.docx'
        # convert_to_docx(input_file, output_file)
        doc = Document(input_file)
        # table_text = ''
        for table in doc.tables:
            table_data = docExtractors.read_table(table)
            table_text = docExtractors.tabulate_table(table_data)
            prompt = f"table_text: {table_text}"
            response = GPTs.tableCorrection(prompt)
            collected_chunks = []
            collected_messages = []
            # iterate through the stream of events
            for chunk in response:
                collected_chunks.append(chunk)  # save the event response
                chunk_message = chunk['choices'][0]['delta']  # extract the message
                if "content" in chunk_message.keys():
                    chunk_message = chunk['choices'][0]['delta']["content"]
                collected_messages.append(chunk_message)
                print(chunk_message,sep='')
                yield "data: " + str(chunk_message) + "\n\n"
    return app.response_class(generate(), mimetype='text/event-stream')





if __name__ == '__main__':
    app.run(debug=True)


