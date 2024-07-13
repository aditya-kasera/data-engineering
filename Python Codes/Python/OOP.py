# Python is an object oriented programming language. 
# Everything in Python is an object
# We instantiate a class to create an object. 
# The class defines attributes and the behavior of the object,
# while the object, on the other hand, represents the class.

# a class without a constructor is not really useful in real applications

class employee():
    def __init__(self,name,age,id,salary): # constructor
        self.name = name
        self.age = age
        self.salary = salary
        self.skills = []

    def person_info(self): # object method
        return f'{self.name} is {self.age} years old. He gets {self.salary}.'

    def add_skill(self, skill):
          self.skills.append(skill)


class student(employee):
    # def __init__(self,name,age,id,salary):
    #     self.name = name
    #     self.age = age
    #     self.salary = 0
    #     self.id = id
    #     self.skills = []
    pass
    
e1 = employee("Aditya", 22, 1.5, 3)
print(e1.person_info())
e1.add_skill('HTML')
e1.add_skill('CSS')
e1.add_skill('JavaScript')
print(e1.skills)
print(e1.__dict__) #{'name': 'adi', 'age': 30, 'salary': 3, 'id': 1}

s1 = student("Arya", 21, 3, None)
s1.add_skill('M')
s1.add_skill('E')
s1.add_skill('R')
s1.add_skill('N')
print(s1.__dict__) #{'name': 'tya', 'age': 29, 'salary': 4, 'id': 2}

pass # null statement