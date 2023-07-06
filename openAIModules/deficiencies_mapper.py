import openai
import json

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
        messages= messages
    )

    # Retrieve the model's reply from the response
    reply = response['choices'][0]['message']['content']
    # AI_dict = {
    #     "role": "assistant",
    #     "content": reply
    # }
    # updated_messages = messages.append(AI_dict)
    # open("messages.json","w",encoding="utf-8").write(json.dumps(updated_messages))
    return reply

if __name__ == '__main__':
    SRS_Text = open("raw_text.txt").read()
    output = get_deficiencies(SRS_Text)
    print(output)
    open("../issues.txt", "w", encoding="utf-8").write(output)
