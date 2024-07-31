# Write a program in Python to display the factorial of a number.

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n


print("Factorial is:", factorial(4))


# Write a program in Python to reverse a string.

def reverse_string(string_a):
    list_reverse = string_a.split(" ")
    list_reverse.reverse()
    str_reverse = ""
    str_new = ""
    for x in list_reverse:
        str_reverse += x.lower() + ' '
    print(str_reverse)
    i = len(string_a) - 1
    while i >= 0:
        str_new = str_new + string_a[i].lower()
        i -= 1
    print(str_new)


a = "Write a program in Python to reverse a string"
reverse_string(a)


# Write a program to separate positive and negative number from a list.

def separate_positive_and_negative():
    list_int = [3, 5, 7, -2, -20, 5, -5]
    list_positive = []
    list_negative = []
    for x in list_int:
        if x > 0:
            list_positive.append(x)
        else:
            list_negative.append(x)
    print("List number: ", list_int)
    print("List negative: ", list_negative)
    print("List Positive: ", list_positive)


separate_positive_and_negative()


# Write a program to remove duplicates in a string.

def remove_duplicates(string_a):
    new_string = ""
    for x in string_a:
        if x not in new_string:
            new_string = new_string + x
    print(new_string, end="")
    print()


string_b = "geeksforgeeks"
remove_duplicates(string_b)


# Define a keyword that accepts a number and returns whether the number is even or odd.

def even_odd(number):
    remainder = number % 2
    if remainder == 0:
        print(number, " is even")
    else:
        print(number, " is odd")


num = eval(input("input number: "))
even_odd(num)


# Define a keyword that accepts lowercase and returns uppercase words

def uppercase_word(str1):
    return str1.upper()


str2 = input("Enter words: ")
print(uppercase_word(str2))
