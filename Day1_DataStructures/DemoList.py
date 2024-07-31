list_number = [2, 5, 6, 1, 0, 3, 7, 9, 8, 34] #Create a list that contains 10 integer numbers

print("Length of list: ", len(list_number))     #Detemine how many items the list has
print("The first: ", list_number[0])       #Retrieve the first
print("The last: ",list_number[9])    #Retrieve the last
print("The second: ",list_number[1])       #Retrieve the second.
print("The second to the end: ", list_number[1:])      #Retrieve all items from the second to the end of the list.

# #Change the value of the third item as 10 and print new list.
print("Old List: ", list_number)
list_number[2] = 10
print("New List: ", list_number)

# 	Change the values from the sixth to eight items with the values -5, -6, -7
list_number[5:8] = [-5, -6, -7]
print("New List after change: ", list_number)

# Insert a new item at index 4 and a new item at the end of the list.
list_number.insert(4,4)
list_number.append(11)
print("New list after insert a new item: ", list_number)

# Remove item as -6 from the list and remove the fifth item of the list.
list_number.remove(-6)
list_number.pop(5)
print("New list after remove items: ", list_number)

# Sort the list in descending order
list_number.sort(reverse=True)
print("List after sort descending: ", list_number)


