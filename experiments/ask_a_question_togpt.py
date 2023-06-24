import openai

list_to_update_deficiencies = [
    {
        "role": "system",
        "content": '''You will be provided the tables of an SRS DOC, Your job is improve Software requirement specification based on IEC62304 standards from the listed deficiencies.You must modify the text and insert some valuable information in empty or None cell. Every table is independent of the SRS doc so you should not remove valubale information also do not inculde the term such as `according to IEC 62304 , IEC 62304 or similar term like this. Always give answer in given table format.
        Input will be in the below format
        `table_text: input table of SRS doc
        'deficiencies: You should find the deficiencies which are related to IEC 62304 and and update the doc according to these deficiencies.`
        output:  output is the same table provided in the input with updated text after removing the listed deficiencies. Make sure you follow the same table formatting. Only give the table in output.
        Your response should follow the following format
        response: Here is the response(this is basically a table(format is the same as input foramt))

'''
    }

]


def ask_a_question(message):
    user_dict = {
        "role": "user",
        "content": message
    }
    list_to_update_deficiencies.append(user_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=list_to_update_deficiencies,
        temperature=.3
    )
    reply = response['choices'][0]['message']['content']
    # list_to_update_deficiencies.pop()
    return reply

table_text = open("../play_with_doc/table_text.txt").read()


if __name__ == '__main__':
    prompt = f"table_text: {table_text}"
    print(ask_a_question(table_text))



'''        You should talk about the thought process, how and what you are doing,follow below mechanism
        ```task: Here you should talk about the provided task
        thoughts: Here you should list your thought process'''
