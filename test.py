family = [{"name": "ratan", "age": 20}, {"name": "rajat", "age": 7}]
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        tot = 0
        if name == 'ratan':
            tot = 0
        else:
            tot = 1
        self.prob = tot

for obj in family:
    print(obj)

people = []

for obj in family:
    newPerson = Person(obj["name"], obj["age"])
    people.append(newPerson)
    print(newPerson.name)
    

