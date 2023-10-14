import json
from json import JSONEncoder
from typing import Any

class Student:
    def __init__(self, name, rollNo, address) -> None:
        self.name = name
        self.rollNo = rollNo
        self.address = address

class Address: 
    def __init__(self, city, street, pin): 
        self.city = city 
        self.street = street 
        self.pin = pin
        
class EncodeStudent(JSONEncoder):
    def default(self, o):
        return o.__dict__

address = Address("Bulandshahr", "Adarsh Nagar", "203001") 
student = Student("Raju", 53, address)

studentJson = json.dumps(student, cls=EncodeStudent, indent=4)
print(studentJson)

print()
print(json.loads(studentJson))