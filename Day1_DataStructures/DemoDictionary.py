"""
Create a dictionary as following
{
“brand”: “Ford”,
“model”: “Bronco Sport”,
“year”: 2022
}
"""
thisdict = {
    "brand": "Ford",
    "model": "Bronco Sport",
    "year": 2022
}
print(thisdict)

# Retrieve a list of the keys of the dictionary.
x = thisdict.keys()
print( x)

# Add a new item to the dictionary with value color: black.
thisdict["color"] = "black"
print("Dictionary after added: ", thisdict)

# Update the color of the car with red value.
thisdict.update({"color": "red"})
print("Dictionary after changed: ", thisdict)

# Remove the item with key name as year. Print new dictionary.
thisdict.pop("year")
print("Dictionary after remove key: ", thisdict)