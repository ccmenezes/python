# Lecture 7
# Dictionary

""" Create a dictionary of HTTP response codes and modify the dictionary appropriately. """

def main():
  # Create a dictionary of HTTP response codes and their descriptions
  http_resp_code = {
    "200": "created",
    "400": "bad",
    "500": "internal server error"
  }
  
  # Print the dictionary
  print("Simple dictionary of HTTP response codes and descriptions:")
  print(http_resp_code)
  
  # Access the description of an item in the dictionary
  description = http_resp_code["400"]
  print(f"\nDescription of 400: {description}")
  
  # Modify the description of a service
  http_resp_code["400"] = "bad request"
  print(f"\nUpdated description of ...: {http_resp_code}")
  
  # Add a new service and its description on the dictionary
  http_resp_code["404"] = "not found"
  print(f"\nAdded description of ...: {http_resp_code}")
  
  # Remove the ... service from the dictionary
  del http_resp_code["400"]
  print(f"\nRemoved 400 ...: {http_resp_code}")
  
  # Use the keys (), values(), and items() methods to display different aspects of the dictionary
  print(http_resp_code.keys())
  print(http_resp_code.values())
  print(http_resp_code.items())
  
  # Modify the dictionary to add a nested structure with additional information (launch_year)
  http_resp_code["500"] = {
    "description": "internal server error",
    "launch_year": 2006
  }
  
  # Print the modified dictionary with nested structure
  print("\nModified dictionary with nested structure")
  print(http_resp_code["500"])

  # Not allowed duplicity
  http_resp_code["200"] = "ok"
  print(http_resp_code)

  # Count the HTTP response codes
  list_lenght = len(http_resp_code)
  print(f"Lenght of the response codes dictionary: {list_lenght}")
    
if __name__ == "__main__":
  main()
