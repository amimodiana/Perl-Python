
class Fruits:
    # connstructor method

    def __init__(self,name,price,color):
      self.name=name
      self.price=price
      self.color=color

    # method
    def display(self):
        print(f"I love eating {self.name}, it cost {self.price} and it is{self.color} in color")

        # istance (object.)
        myobj=Fruits("banana", 30, "yellow")
        myobj.display()
        myobj2=Fruits("mangoes",20,"green")
        myobj2.display()

