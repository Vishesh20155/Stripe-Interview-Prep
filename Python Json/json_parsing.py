import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))

# print()

# # Add indentation to printing string
# print(json.dumps(x, indent=4))

# print()

# # Change the separators while converting to string
# print(json.dumps(x, indent=4, separators=(". ", " = ")))

# print()

# # Order the keys using sort_keys
# print(json.dumps(x, indent=4, sort_keys=True))



# # To read a json file: (use json.load())

# # Opening JSON file
# f = open('data.json',)
 
# # returns JSON object as
# # a dictionary
# data = json.load(f)
 
# # Iterating through the json
# # list
# for i in data['emp_details']:
#     print(i)
 
# # Closing file
# f.close()



# Write to a json file (using json.dump()):
with open("sample.json", "w") as outfile:
  json.dump(x, outfile, indent=4)
