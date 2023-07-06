import openai

initial_prompt = [
    {
        "role": "system",
        "content": '''You will be provided the table of an SRS DOC, Your job is improve Software requirement specification based on IEC62304 standards from the listed deficiencies.You must modify the text and insert some valuable information in empty or None cell. Every table is independent of the SRS doc so you should not remove valubale information also do not inculde the term such as `according to IEC 62304 , IEC 62304 or similar term like this. Always give answer in given table format.
        Input will be in the below format:
        `table_text: {input table of SRS Doc}`

        You should follow the below path to reach the final output:
        ```
        deficiencies: You should find the deficiencies which are related to IEC 62304  and update the doc according to these deficiencies.`
        output:  {updated table after removing the deficiencies}. 
        Here is the sample example of output table format:
        [['key:', 'value'], 
['key:', 'value'], 
['key:', 'value']]
You should remember below instructions to create the output:
1. No additional Table should be added.
2. Text of the updated table should not be as it is as provided table, you should update or modify the text
3. You should not change the table formatting. 
3. You must add some valuable information to the provided table.
```

'''
    }

]


def agent(message):
    user_dict = {
        "role": "user",
        "content": message
    }
    initial_prompt.append(user_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=initial_prompt,
        temperature=.3
    )
    reply = response['choices'][0]['message']['content']
    # list_to_update_deficiencies.pop()
    return reply




if __name__ == '__main__':
    table_text = open("../play_with_doc/table_text.txt").read()
    prompt = f"table_text: {table_text}"
    print(agent(table_text))


