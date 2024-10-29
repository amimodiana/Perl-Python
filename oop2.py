# create a  class called person with name,age and gender as
# the attribe a construtor, a method and an object

class Person:
    # connstructor method

    def __init__(self,name,age,gender):
      self.name=name
      self.price=age
      self.gender=gender

    # method
    def display(self):
        print(f"I love playing{self.name}and it is{self.age} gender")

        # instance
        myobj=Person("Mary", 30, "Female")
        myobj.display()
        myobj=Person("James",20,"male")
        myobj.display()
