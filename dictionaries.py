# I am following the following tutorial to learn dictionaries
# https://www.youtube.com/watch?v=daefaLgNkw0
# Also I add \n to some print statements to make reading the output easier
student = {"name" : "John", "age": 25, "courses" : ["Math", "CompiSci"]}

print(student) # Print the whole dictionary

print(student["name"]) # Print the name key from the dictionary 

print(student["courses"])

# Check if key exists
print(student.get("name"))
print(student.get("phone")) # Will return none since the key "phone"  does not exist
print(student.get("phone", "not found")) # Will return a custom value if the key does not exist

# Update a dictionary
student.update({"name" : "Jane", "age" : 26, "phone" : "555-555-5555"})
# NOTE: A dictionary can also be updated with student["name"] = "Hello, world!"
print(student)

# Delete a key's value
print("Delete a key's value")
del student["age"]
student.update({"age" : 26})
age = student.pop("age") # copy value of a key to a variable and then remove the value of the key
print(student)

# Print various information about a dictionary
print("The number of keys in the dictionary: " + str(len(student))) # Print number of keys in a dictionary
# Print only the keys in a dictionary line by line
print("The keys in the dictionary")
for key in student:
    print (key)
# Print the pairs of keys and values in a dictionary
print("Pairs of keys and values in the dictionary")
for key, value in student.items():
    print(key, value)