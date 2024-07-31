# Create a tuple having values: apple, banana, cherry, orange, kiwi, melon, mango, apple, cherry.
tuple_fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "apple", "cherry")
print("Tuple: ", tuple_fruits)

# Determine how many items the tuple have
len_tuple = len(tuple_fruits)
print("Length of tuple: ", len_tuple)

# Retrieve the last, the first and the second item of the tuple.
print("The first item of the tuple: ", tuple_fruits[0])
print("The second item of the tuple: ", tuple_fruits[1])
print("The last item of the tuple: ", tuple_fruits[len_tuple - 1])

# Retrieve the items from the beginning to, but not included kiwi.
for x in tuple_fruits:
    if x == "kiwi":
        continue
    else:
        print(x, end=' ')
print()

# Change kiwi value with the value grape
list_fruits =  list(tuple_fruits)
list_fruits.remove("kiwi")
tuple_fruits = tuple(list_fruits)
print("Tuple after remove: ", tuple_fruits)

# Add a new item to the tuple with value kumquat
list_fruits =  list(tuple_fruits)
list_fruits.append("kumquat")
tuple_fruits = tuple(list_fruits)
print("Tuple after add new item: ", tuple_fruits)

# Remove mango from the tuple
list_fruits =  list(tuple_fruits)
list_fruits.remove("mango")
tuple_fruits = tuple(list_fruits)
print("Tuple after remove item: ", tuple_fruits)
