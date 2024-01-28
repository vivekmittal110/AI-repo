# Tuples items
'''
ordered
immutable
dublicates allowed
any data types
mix of different data type
'''
colors = (1, "red", 4.8, "blue")

# if we make a tuple with only one item so we have to use comma or typecasting to identify that it is tuple
one = ("apple") # apple # string
one1 = ("apple",) # ("apple",)
one2 = tuple(("apple")) #('a','p','p','l','e')
# check the type of a tuple 
print(type(one))
print(type(one1))
print(type(one2))

# check the lenght of a tuple 
print(len(one1)) # 1
print(len(colors)) # 4
print(len(one2)) # 5

# accessing items in tuple
print(colors[1])
print(colors[-1])
print(colors[1:3])

# check if a item is present in a tuple 
print( "True" if "red" in colors else "False")

# traverse a tuple
for i in colors:
    print(i,end=" ")
print()
# concatinate two tuples

more_colors = ("pink","orange")
colors += more_colors
print(colors)


# reverse a tuple
for i in reversed(colors):
    print(i, end=" ")
print()

# example
tup1 = (1,2,3,4,5,6,7)
tup2 = []
for i in reversed(tup1):
    tup2.append(i)

tup1 = tuple(tup2)
print(tup1)
print(type(tup1))