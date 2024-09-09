# Lecture 02
# Inheritance

# Define a class
class Car:
  def __init__(self, doors, year) :
    self.doors = doors
    self.year = year

# Create a child class
class Make(Car):
  def __init__(self, doors, year, make, model):
    super().__init__(doors, year)
    self.make = make
    self.model = model

  def car_info(self):
    print("Car: doors:", self.doors, "year:", self.year, "make:", self.make, "model:", self.model)

# Create a object of class and assign values
car1 = Make(3, 2000, "Honda", "Civic")

# Access car info method
car1.car_info()
