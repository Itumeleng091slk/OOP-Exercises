class Person:
    def __init__(self,name,age,gender,interest=[]):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.interest = interest

    def hello(self):
        interest = ",".join(self.interest)
        return "hello my name is {} and I am a {} years old. My interest's are {} ".format(self.name, self.age,interest)

person = Person('Ryan','30',"male",["being a hardarse, agile, ssd hard drives"] )  
print(person.hello())
