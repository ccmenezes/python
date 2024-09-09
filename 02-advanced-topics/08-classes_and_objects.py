# Lecture 01
# Classes and Objects

# Define a class
class Car:
  def __init__(self, doors, year) :
    self.doors = doors
    self.year = year

# Create a object of class and assign values
car1 = Car("3", 2000)

# Access attributes 
print(f"Car: doors: {car1.doors}, year: {car1.year}")

# Modify object properties
car1.year = 1.82
print("--- Modify object properties ---")
print(f"Car: doors: {car1.doors}, year: {car1.year}")

# Delete object properties
del car1.year
print("--- Delete object properties ---")
print(f"Car: doors: {car1.doors}, year: {car1.year}")

# Delete the object
del car1
