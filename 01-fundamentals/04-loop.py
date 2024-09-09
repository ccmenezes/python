# Lecture
# Loops

""" Use a list of HTTP response code and demonstrate various loop operations. """

# List HTTP resp code
http_resp_code = ["200", "400", "404", "500"]
print(f"HTTP response code list: {http_resp_code}")

# Use a for loop to iterate throught the list
# print("\Using a for loop to iterate the list.")
for code in http_resp_code:
  print(code)

# Use a while loop to iterate throught the list in reverse order
# print("\nUsing a while loop to iterate throught the list in reverse order:")
index = len(http_resp_code) - 1
print(index)
while index >=0:
  print(http_resp_code)
  index -= 1

# Using enumerate() with a for loop to get both index and value
print("\nUsing enumerate() with a for loop to get both index and value:")
for index, code in enumerate(http_resp_code):
  print(f"code # {index + 1}: {code}")
