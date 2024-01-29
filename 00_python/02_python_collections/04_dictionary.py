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