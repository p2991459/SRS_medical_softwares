import json

prompt =''' As an expert in evaluating Software Requirement Specifications (SRS) in the medical field using various standards such as IEC 62304, your role is to thoroughly analyze the SRS and identify any deficiencies in relation to these standards.You possess in-depth knowledge and understanding of the specified standards and can effectively outline areas where the SRS does not align with the requirements set by IEC 62304. Your expertise allows you to provide valuable insights and recommendations for improving the SRS to meet the necessary standards and ensure compliance in the medical software development process.'''
list_to_get_deficiencies = [
   {
      "role":"system",
      "content":"As an expert in evaluating Software Requirement Specifications (SRS) in the medical field using  IEC 62304 standard, your role is to thoroughly analyze the SRS and identify any deficiencies in relation to these standards."
   }

]
list_to_update_deficiencies = [
   {
      "role":"system",
      "content":'''As an expert in evaluating Software Requirement Specifications (SRS) in the medical field, your role is to update a given document by removing specific deficiencies that are related to the IEC 62304 standard. Your task is to make suitable changes to the provided SRS document and provide an updated version after eliminating the identified deficiencies. The input will follow the following format:\nSRS_DOC: [The Software Requirement Specifications (SRS) document part that needs to be updated from the given deficiencies. Please note that only a part of the document is provided due to token limitations, and you should update the document based on the provided deficiencies. You may not find all the deficiencies in the text, so only correct based on the matched deficiencies.]

Deficiencies: [List of all the deficiencies related to IEC 62304. Please ensure that you format the updated text properly and remove unnecessary words.]
'''
   }

]

open("messages.json","w").write(json.dumps(list_to_update_deficiencies))

data = json.loads(open("messages.json").read())

user_dict = {
   "role": "user",
   "content": "hello"
}
messages = json.loads(open("messages.json").read())
messages.append(user_dict)
print(messages)