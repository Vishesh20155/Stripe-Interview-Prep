import json

# Sample JSON string
json_string = {"name": "John", "age": 30, "city": "New York"}

# Parse JSON string into a dictionary
data = json.dumps(json_string, indent=4)

print(data)
