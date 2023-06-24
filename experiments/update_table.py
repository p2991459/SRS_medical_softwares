import openai
import pandas as pd
list_to_update_deficiencies = [
   {
      "role":"system",
      "content":'''As an expert in evaluating Software Requirement Specifications (SRS) in the medical field, your role is to update a given pandas dataframe by removing  deficiencies that are related to the IEC 62304 standard. Your task is to make suitable changes to the provided SRS document and provide an updated version after eliminating the identified deficiencies. 
      
      Input dateframe and deficiencies will be provided to you in below format:
      `dataframe: df
      found_deficiencies: list of deficiencies`
      
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
        messages= list_to_update_deficiencies
    )

    # Retrieve the model's reply from the response
    reply = response['choices'][0]['message']['content']
    list_to_update_deficiencies.pop()
    # AI_dict = {
    #     "role": "assistant",
    #     "content": reply
    # }
    # updated_messages = messages.append(AI_dict)
    # open("messages.json","w",encoding="utf-8").write(json.dumps(updated_messages))
    return reply

if __name__ == '__main__':
    df = pd.read_csv("table.csv")
    issues = open("../issues.txt").read()
    input = f"dataframe: {df}\nfound_deficiencies: {issues}"
    output = update_deficiencies(input)
    print(output)

    open("updated_table.txt", "w", encoding="utf-8").write(output)