# Lecture 11
# Modules

import datetime

now = datetime.datetime.now()
print(now)


# Print year and name of weekday
# strftime takes one parameter, it's format
print(now.year)
print(now.strftime("%A")) # %A weekday, full version

# Creating date objects
input_date = datetime.datetime(2024, 9, 9)
print(input_date)
