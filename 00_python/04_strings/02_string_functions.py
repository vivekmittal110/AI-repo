# we can not modify original srting due to its immutability
name1 = "My name is Vivek mittal"

# for converting characters into upper case use upper()
# print(name1.upper())
# print(name1)

# name2 = name1.upper()
# print(name2)


# for converting characters into lower case use lower()
# print(name1.lower())


# for capitilizing characters use capitilize()
# print(name1.capitalize())

# for stripping/removing any tralling whitespaces
# str = "    hello world!!   "
# print(str.strip())

# replace function
# str_name.replace("old substring", "new substring", count)
str_sen = "My name is vivek, vivek is a good boy. my full name is vivek mittal"
print(str_sen.replace("vivek","nitin",2)) # count is optional, if you dont give count it will replace every old substring with new one

# split function returns a list
# string_name.split(seperator, maxsplit) # (both parameters are optional)
# by default white spaces are the saperator
str_fruits = "apple banana mango orange pineapple"
print(str_fruits.split())

str_fruits2 = "apple,banana,mango,orange,pineapple,kiwi"
list_fruits = str_fruits2.split(",",3)
print(list_fruits)

# concatination
str1 = "my name is "
str2 = "vivek"
print(str1 + str2)

# string formatting
student_name = "vivek"
student_marks = 99
str_mar = "The student name is {s} and marks is {m}".format(s = student_name, m = student_marks)
print(str_mar)