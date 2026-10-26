"""
class Car:
    def __init__(self,x,y):
     self.brand=x
     self.colour=y

    def display(self):
     print(self.brand)
     print(self.colour)

    def Start(self):
        print("Car Started")

obj=Car("TOYOTA","BLACK")
obj.display()
obj.Start()
"""
class Calculator:
  def __init__(self):
    self.x=int(input("Enter x:"))
    self.y=int(input("Enter y:"))

  def Add(self):
    return self.x+self.y
  def Subtraction(self):
    return self.x-self.y  
  def Div(self):
    try:
      return self.x /self.y
    except ZeroDivisionError:
      return "Cannot divide by zero"
     

        
c=Calculator()
print("Addition:",c.Add())
print("Subtraction:",c.Subtraction())