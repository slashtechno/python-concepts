# I am following the following tutorials to learn dictionaries
# https://www.youtube.com/watch?v=daefaLgNkw0
# https://www.youtube.com/watch?v=9N6a-VLBa2I

import json

student = {"name": "John", "age": 25, "courses": ["Math", "CompiSci"]}

print("The dictionary:")
print(student)  # Print the whole dictionary
print("The value of the key \"name\"")

print(student["name"])  # Print the name key from the dictionary

# Print the courses key from the dictionary
print("The value of the key \"courses\"")
print(student["courses"])

# Check if key exists
print("Checking if a key exists")
print(student.get("name"))
# Will return none since the key "phone"  does not exist
print(student.get("phone"))
# Will return a custom value if the key does not exist
print(student.get("phone", "not found"))

# Update a dictionary
print("Updating the dictionary")
print("Before")
print(student)
student.update({"name": "Jane", "age": 26, "phone": "555-555-5555"})
# NOTE: A dictionary can also be updated with student["name"] = "Hello, world!"
print("After")
print(student)

# Delete a key's value
print("Before")
print(student)
print("Deleting a key's value")
del student["age"]
student.update({"age": 26})
# copy value of a key to a variable and then remove the value of the key
age = student.pop("age")
print("After")
print(student)

# Print various information about a dictionary
# Print number of keys in a dictionary
print("The number of keys in the dictionary: " + str(len(student)))

# Print only the keys in a dictionary line by line
print("The keys in the dictionary")
for key in student:
    print(key)

# Print the pairs of keys and values in a dictionary
print("Pairs of keys and values in the dictionary")
for key, value in student.items():
    print(key, value)  # The comma is like + but adds a space

# using a for loop
for person in student:
    print(student["name"])

# using JSON

# convert Python dictionary to JSON format
json_dictionary = json.dumps(student, indent=4)
