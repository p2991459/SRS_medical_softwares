import os
from dotenv import load_dotenv
load_dotenv()
import openai


def openai_text_formatter(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a text formatter with the ability to accurately format text based on contextual information,Always remove page number and page number related information. This prompt challenges you to leverage your understanding and context to produce accurate and appropriate text formatting. You can always remove unnecessory punctuations,words,few texts etc and provide the best formatted result from the text"},
            {"role": "user", "content": message}
        ]
    )

    # Retrieve the model's reply from the response
    reply = response['choices'][0]['message']['content']
    return reply
