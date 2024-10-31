

# inheritance

class Parent:
    def __init__(self,name,age):
     self.name=name
     self.age=age
class Child(Parent):
     def greet(self):
            return f"my name is {self.name}, i am{self. age} years old"
             # instance

child=Child("Mary",15)
child=Child("James", 25)
print(child.greet())
print(child.greet())

