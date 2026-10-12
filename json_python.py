import json
from encodings import utf_8

json_data ="""
{
  "name": "Ivan",
  "age": 30,
  "is_student": false,
  "courses": ["Python","QA Automation","API testing"],
  "adress": {
    "city": "London",
    "zip": "10011"
            
  }
}"""

parsed_data = json.loads(json_data)

#print(parsed_data['adress'])



# json_data=json.dumps(data, indent=4)
# #print(json_data)
#
# with open('json_exemple.json', 'r', encoding="utf_8") as file:
#     data =json.load(file)
#     print(data, type(data))
data={
    'name': 'Ivan',
    'age': 30,
    'is_student':False
}

with open("json_data.json", 'w', encoding="utf_8") as file:
    json.dump(data, file, indent=4)