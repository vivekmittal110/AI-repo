# it stores key value pairs
numbers = {
    "vivek" : 123,
    "nitin" : 456
    }
# dictionary items
'''
ordered
changable
unindexed
dublicaates are not allowed (for keys)
any data type
'''
print(numbers)

# check lenght of a dictionary
print(len(numbers))

# check data type of a dictionary
print(type(numbers))

# accessing items of a dictionary
print(numbers["vivek"])
print(numbers.get("vivek"))
print(numbers.keys())

# update values
numbers["nitin"] = 143
print(numbers)

# add elements in a dict
numbers["mannat"] = 159
print(numbers)

more_num = {
    "ayush" : 135,
}
numbers.update(more_num)
print(numbers)

# remove element from a dict
numbers.pop("mannat")
print(numbers)

numbers.popitem() # this will remove the last item
print(numbers)

print()

# numbers.clear() # this will empty the dict
# print(numbers)

# printing the values of a dict (traverse through a dict
# for x in numbers :
#     print(x)          this will print the values

# for x in numbers.items() :
#     print(x)          this will print keys with their values

# for x,y in numbers.items() :
#     print(x,y)          this will print keys and values saparately


print()

# nested dict
phones = {
    "area1" : {
        "nitin" : 46464,
        "vivek" : 464 
    },
    "area2" : {
        "ayush" : 67864,
        "mannat" : 5456
    }
}

print(phones["area1"]["nitin"])
