import openai

messages = [
    {
        "role": "system",
        "content": '''You will be provided the tables of an SRS DOC, Your job is improve Software requirement specification based on IEC62304 standards from the listed deficiencies.You must modify the text and insert some valuable information in empty or None cell. Every table is independent of the SRS doc so you should not remove valubale information also do not inculde the term such as `according to IEC 62304 , IEC 62304 etc`. Always give answer in given table format.
        Input will be in the below format
        `table_text: tables of SRS doc
        'deficiencies: You should find the deficiencies which are related to IEC 62304 and list them here.`
        You should talk about the thought process, how and what you are doing,follow below mechanism
        ```task: Here you should talk about the provided task
        thoughts: Here you should list your thought process
        action: your doable actions you should provide here.
        output: final output is the same table provided in the input with updated text after removing the listed deficiencies. Make sure you follow the same table formatting.

'''
    }

]


def tableCorrection(message):
    user_dict = {
        "role": "user",
        "content": message
    }
    messages.append(user_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        stream=True
    )
    # reply = response['choices'][0]['message']['content']
    # list_to_update_deficiencies.pop()
    return response




if __name__ == '__main__':
    table_text = open("../play_with_doc/table_text.txt").read()
    prompt = f"table_text: {table_text}"
    print(tableCorrection(table_text))


