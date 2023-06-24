import openai

system_message = [
    {
        "role": "system",
        "content": '''You will be provided the tables of an SRS DOC and the deficiencies related to IEC 63304 standard, Your job is improve Software requirement specification based on IEC62304 standards from the listed deficiencies.Always give answer in given table format.
        Input will be in the below format
        `table_text: tables of SRS doc
        'deficiencies: listed deficiencies`
        You should talk about the thought process, how and what you are doing,follow below mechanism
        ```task: Here you should talk about the provided task
        thoughts: Here you should list your thought process
        action: Final action you should provide here.

'''
    }

]


def ask_a_question(message):
    user_dict = {
        "role": "user",
        "content": message
    }
    system_message.append(user_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=system_message
    )
    reply = response['choices'][0]['message']['content']
    system_message.pop()
    return reply

table_text = open("../play_with_doc/table_text.txt").read()
deficiencies = open("table_deficiencies.txt").read()

if __name__ == '__main__':
    prompt = f"table_text: {table_text}\ndeficiencies: "
    print(ask_a_question(table_text))