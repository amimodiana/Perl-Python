class Fruits:
    # connstructor method

    def __init__(self,name,price,color):
      self.name=name
      self.price=price
      self.color=color

    # method
    def display(self):
        print(f"I love eating{self.name}and it is{self.color}in color")

        # instance
        myobj=Fruits("Banana", 30, "yellow")
        myobj.display()
        myobj=Fruits("mangoes",20,"green")
        myobj.display()


