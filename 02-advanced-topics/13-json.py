# Lecture 13
# JSON

import json

# Convert from JSON to python
# some json
fruits_json = '{"fruit": "banana", "price":"2.50"}'

# parse fruits_json
load_json = json.loads(fruits_json)

print(load_json["fruit"])

# Convert from python to JSON

# python object
fruits = {
  "fruit": "apple", "price":"1.75"
}

# convert into JSON
fruits_json = json.dumps(fruits)

print(fruits_json)
