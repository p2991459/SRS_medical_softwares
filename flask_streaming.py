from flask import Flask, Response
import openai
import tiktoken
import time
from update_doc_stream import update_deficiencies
app = Flask(__name__)


@app.route('/stream', methods=['GET'])
def stream_conversation():
    start_time = time.time()

    def generate():
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
            response = update_deficiencies(f'''SRS_DOC: {decoded_text}\nDeficiencies: {issues}''')
            collected_chunks = []
            collected_messages = []
            # iterate through the stream of events
            for chunk in response:
                chunk_time = time.time() - start_time  # calculate the time delay of the chunk
                collected_chunks.append(chunk)  # save the event response
                chunk_message = chunk['choices'][0]['delta']  # extract the message
                if "content" in chunk_message.keys():
                    chunk_message = chunk['choices'][0]['delta']["content"]
                collected_messages.append(chunk_message)  # save the message
                print(str(chunk_message))

                yield str(chunk_message)  # yield the message within the generate() function

    return app.response_class(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run()
