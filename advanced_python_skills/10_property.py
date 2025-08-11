# Setters and getters in Python

class Person:
    
    def __init__(self, age):
        self._age = age
    
    def category(self):
        if self._age < 18:
            return "Child"
        elif 18 <= self._age < 65:
            return "Adult"
        else:
            return "Senior"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        print("Setting age to", value)
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @age.deleter
    def age(self):
        print("Deleting age")
        del self._age
    
    @age.getter
    def age(self):
        print("Getting age")
        return self._age
    

person = Person(35)
print(person.category())
try:
    person.age = -70
except ValueError as e:
    print(e)
print(person.category())