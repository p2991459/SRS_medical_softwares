import os
from dotenv import load_dotenv
load_dotenv()
import openai
import json
import time
start_time = time.time()
def get_deficiencies(message):
    messages = [
        {
            "role": "system",
            "content": "As an expert in evaluating Software Requirement Specifications (SRS) in the medical  your role is to identify a few deficiencies and areas where improvements can be made to align with the IEC 62304 standardsfield using  IEC 62304 standard,"
        }

    ]
    user_dict = {
        "role": "user",
        "content": message
    }

    messages.append(user_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages,
        temperature=0,
        stream=True
    )

    # Retrieve the model's reply from the response
    # AI_dict = {
    #     "role": "assistant",
    #     "content": reply
    # }
    # updated_messages = messages.append(AI_dict)
    # open("messages.json","w",encoding="utf-8").write(json.dumps(updated_messages))
    return response

if __name__ == '__main__':
    SRS_Text = open("raw_text.txt").read()
    response = get_deficiencies(SRS_Text)
    collected_chunks = []
    collected_messages = []
    # iterate through the stream of events
    for chunk in response:
        chunk_time = time.time() - start_time  # calculate the time delay of the chunk
        collected_chunks.append(chunk)  # save the event response
        chunk_message = chunk['choices'][0]['delta']# extract the message
        if "content" in chunk_message.keys():
            chunk_message = chunk['choices'][0]['delta']["content"]
        collected_messages.append(chunk_message)  # save the message
        print(f"{chunk_message}",end = " ")
        # print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

    # # print the time delay and text received
    #     print(f"Full response received {chunk_time:.2f} seconds after request")
    #     full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    #     print(f"Full conversation received: {full_reply_content}")
    #     # open("issues.txt","w",encoding="utf-8").write(output)
