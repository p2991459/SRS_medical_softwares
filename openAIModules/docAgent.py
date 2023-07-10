import openai
import tiktoken


conversation = [
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

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = 0
    for message in messages:
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
    return num_tokens
#gpt-3.5-turbo
def agent(message):
    model = 'gpt-3.5-turbo-0301'
    user_dict = {
        "role": "user",
        "content": message
    }
    conversation.append(user_dict)
    tokens = num_tokens_from_messages(conversation)
    print(f"Token number of tokens received from conversation: {tokens}")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=.3,
        max_tokens = 2000
    )
    reply = response['choices'][0]['message']['content']
    conversation.pop()
    return reply




if __name__ == '__main__':
    pass


