## Class 03
## Dictionaries

phone = {"Fulano": 92874949, "Sicrano": 73633383}
print(phone)
 
# Add a phone
phone["Maria"] = 73787838
print(phone)

## Not allowed duplicity
phone["Maria"] = 999924784
print(phone)

# Count the phone
print(len(phone))

# Remove the phone
del phone["Sicrano"]
print(phone)