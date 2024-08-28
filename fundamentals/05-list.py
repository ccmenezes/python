## Lecture 05
## Lists

fruits = ["apple", "banana", "orange", "avocado"]
print(fruits)

# Access the first fruit in the list
first_fruit = fruits[0]
print(f"First fruit {first_fruit}")

# Access the last service in the list
# -1 go to the end of the list
last_fruit = fruits[-1]
print(f"Last fruit in the list {last_fruit}")

# Add fruits
fruits.append("limon")
print(fruits)

# Count the fruits
print(len(fruits))

# Remove a fruit
fruits.remove("orange")
print(fruits)

# Reverse the fruit list
print(fruits)
fruits.reverse()
print(fruits)

# Find the lenght of the list
list_lenght = len(fruits)
print(f"Lenght of the fruit list : {list_lenght}")

# Slice the list to get fruits from index 1 to 2
sliced_fruits = fruits[1:2]
print(f"Sliced fruits: {sliced_fruits}")

