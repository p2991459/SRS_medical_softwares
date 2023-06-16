import os
from dotenv import load_dotenv
load_dotenv()
import openai
import json
import tiktoken
import time
start_time = time.time()
list_to_update_deficiencies = [
   {
      "role":"system",
      "content":'''As an expert in evaluating Software Requirement Specifications (SRS) in the medical field, your role is to update a given document by removing specific deficiencies that are related to the IEC 62304 standard. Your task is to make suitable changes to the provided SRS document and provide an updated version after eliminating the identified deficiencies. The input will follow the following format:\nSRS_DOC: [The Software Requirement Specifications (SRS) document part that needs to be updated from the given deficiencies. Please note that only a part of the document is provided due to token limitations, and you should update the document based on the provided deficiencies. You may not find all the deficiencies in the text, so only correct based on the matched deficiencies.]

Deficiencies: [List of all the deficiencies related to IEC 62304. Please ensure that you format the updated text properly and remove unnecessary words.]
'''
   }

]
def update_deficiencies(message):
    user_dict = {
      "role":"user",
      "content": message
   }
    # messages = json.loads(open("messages.json").read())
    list_to_update_deficiencies.append(user_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= list_to_update_deficiencies,
        temperature=0,
        stream=True
    )

    # Retrieve the model's reply from the response
    list_to_update_deficiencies.pop()
    # AI_dict = {
    #     "role": "assistant",
    #     "content": reply
    # }
    # updated_messages = messages.append(AI_dict)
    # open("messages.json","w",encoding="utf-8").write(json.dumps(updated_messages))
    return response

if __name__ == '__main__':
    SRS_Text = open("raw_text.txt").read()
    tt_encoding = tiktoken.get_encoding("cl100k_base")
    tokens = tt_encoding.encode(SRS_Text)
    ChunkSize = 2000
    chunks  = [tokens[0:2000],tokens[2000:-1]]
    issues  = open("issues.txt").read()

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
            print(f"{chunk_message}", end=" ")