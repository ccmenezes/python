# Lecture 14
# Try ...Except

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong.")
else:
  print("Nothing went wrong")
finally:
  print("Tre 'try except' is finished")

# Another example
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 
