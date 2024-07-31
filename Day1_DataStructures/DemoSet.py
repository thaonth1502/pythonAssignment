# Create a set containing values apple, banana, cherry and retrieve the number of items.
set_fruits = {"apple", "banana", "cherry"}
print("Items in Set: ", set_fruits)
print("the number of items: ", len(set_fruits))

# Add one item to the set with value orange.
set_fruits.add("orange")
print("Set after add item: ", set_fruits)

# Add a list of items kiwi, kumquat to the set.
list_fruits = ["kiwi", "kumquat"]
set_fruits.update(list_fruits)
print("Set after add a list: ", set_fruits)

# Remove banana value from the set
set_fruits.remove("banana")
print("Set after remove item: ", set_fruits)

# Create another set consisting of apple, banana, orange. Join two sets and retrieve the number of items in new set.
set_other_fruits = {"apple", "banana", "orange"}
new_set_fruits = set_fruits | set_other_fruits
print("Set ofter join another set: ", new_set_fruits)
print("Length of new set: ", len(new_set_fruits))

