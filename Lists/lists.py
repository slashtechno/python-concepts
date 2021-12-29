# Make a list
x = ["item1", "item2", "item3"]
# Print list
print(x)
# Print the first item of the list
print(x[0])
# Print the last item of a list
print(x[-1])
# Print a range of items (first number included, second number is not included)
print(x[0:2])
# Print items from beginning to a specified number (second number is not included)
print(x[:1])
# Print items from a specified number to the end of the list 
print(x[1:])
# Check if an item exists in a list
if "thisitemdoesnotexist" in x:
    print("thisitemdoesnotexist does not exist") 
# Change item value
x[2] = "last_item"
print(x)
# Change a range of items (second number is not included)
x[1:3] = ["item#2", "item#3"]
print(x)
# Insert item without replacing
x.insert(0, "item0")
print(x)
# Append to list
x.append("item#4")
print(x)
# Add the content of one list to another
x.extend(x)
print(x) 
print("Resetting the list to ['item0', 'item1', 'item#2', 'item#3', 'item#4']")
x = ['item0', 'item1', 'item#2', 'item#3', 'item#4']
# Remove an item from a list
x.remove("item#4")
print(x)
print("Resetting the list to ['item0', 'item1', 'item#2', 'item#3', 'item#4']")
x = ['item0', 'item1', 'item#2', 'item#3', 'item#4']
# Remove an item in a list by its index
x.pop(3)
print(x)
# Empty a list
x.clear()