# These allows us to store multiple items in a single variable
# example
fruits = ["apple", "banana", "mango", 1, 4.5, False]

# list Items
'''
indexed
ordered
mutable
duplicates allowed
any data type
mix of differente data type
'''
print(fruits[2])
print(type(fruits))
print(len(fruits))

print("True" if "banana" in fruits else "false")
print("True" if "kiwi" not in fruits else "false")

# change value of item at specific index
fruits[0] = "orange"
print(fruits)

#  accessing items of a list
'''
indexing
negative indexing
range of indexes
range of negative indexes
'''
print(fruits[1])
print(fruits[-3])
print(fruits[1:3])
print(fruits[-5:-1])

# adding elements to a list
'''
append -> add to the end
insert
edtend
+ operator
'''
fruits.append("vivek")
print(fruits)

fruits.insert(0,"kiwi")
print(fruits)

veg = ["patato", "tomato"]
fruits.extend(veg)
print(fruits)

fruits += veg
print(fruits)
# Removing elements from a list
'''
remove
pop -> remove item by index or last item
del -> delete item by index or whole list
'''
fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(2)
print(fruits)

# del(fruits)
# print(fruits)  # this will give an error because fruits is deleted

# change item in a list
#  at an index
fruits[4] = "orange"
print(fruits)

# in a range
fruits[4:6] = ["vivek","orange"]
print(fruits)

# sorting a list
# ascending
# shoting is posssible when data type is same
list_sort = [10, 50, 80, 20]
list_sort.sort()
print(list_sort)

# in descending
list_sort.sort(reverse = True)
print(list_sort)

# reverse a list
fruits.reverse()
print(fruits)


# **** list comprehension ****
# when we want to make a list from a existing list
# and do some operation on each element of the list

new_list = [x for x in list_sort if x > 30]
print(new_list)

# copy a list
copy_fruits = fruits.copy()
print(copy_fruits)

# nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[2][1])
matrix.insert(1,[2,3,4])
print(matrix)