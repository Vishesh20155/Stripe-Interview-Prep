class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return self.name + " " + str(self.age)
        
l = []
l.append(Person('Vishesh', 23))
l.append(Person('Virat', 35))
l.append(Person('Abhay', 29))
l.append(Person('Abhay', 24))
l.append(Person('Abhay', 26))
l.append(Person('Aahay', 26))   

def cmp(p1: Person, p2: Person):
    if p1.name == p2.name:
        return p1.age-p2.age
    return p1.name > p2.name

l.sort(key=cmp)

for p in l:
    print(p)
        