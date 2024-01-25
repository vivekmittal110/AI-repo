"vivek"
'vivek'
name = "vivek"
phase = "vivek" + " is my name"
phase2 = name + " is my name"
name += " is my name"

# multiline strings
print("""my 
name 
is 
vivek""")

# Strings method
print(len(name)) # gives the length of string
print(name.upper()) # converts all letters to uppercase
print(name.lower()) # converts all letters to lowercase
print(name.title()) # Converts first letter of each word to UpperCase
print(name.capitalize()) # Capitalizes only the first char of a String
print(name.count('i')) # Counts non-overlapping occurrences of substring
print(name[0]) # Accessing character in string by index, it starts from 0
print(name[-1]) # Accessing last character in string by negative index
print(name[1:3]) # Slicing the string, it includes start and ex
#cludes end, so here 've' will be printed
print(name[:3]) # Another way of slicing which means from beginning till 3
# characters are there
print(name[3:]) # This means print from 3rd character till the end of
# the string
print("\n".join(name)) # Joins elements of list with '\n', Here whole
# string will be joined with '\n'.


# string method
print("vivek".upper())
print("Vivek".lower())
print("my name is vivek".title())
print("vivek".islower())
print(len("vivek"))
print("viv" in "vivek")

print("vivek \\/ mittal")
print("vivek \nmittal")
#string methods returns the new modified string not alter the original string 

# slicing
name_new = "vivek mittal"
print(name_new[0:5:1])
print(name_new[0::1])
print(name_new[1:5:1])
print(name_new[:5:1])
print(name_new[0:5:])
print(name_new[0:5:2])

# accessing the part of string
print(name_new[4])
