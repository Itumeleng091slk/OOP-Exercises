class Person:
    def __init__(self,name,age,gender,interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        print("hello my name is" + " " + self.name + " "+" and i am " + " " + self.age + " " + "years old and my interests are" + " " + self.interests)

person = Person('Ryan','30','male',"being a hardarse, agile, ssd hard drives" )  
person.hello()
