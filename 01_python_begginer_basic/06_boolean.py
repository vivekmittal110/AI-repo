# every number excepts 0 is True
# 0 is False

# all strings are True exceps empty strings, blank spaces are also true
#  "" empty string is false

done = 10
# done = ""
if done:
    print("yes")
else:
    print("no")

# you can also checks the type 
d2 = True
print(type(d2) is bool)


# any and all function
book1 = True
book2 = False
read_any_book = print(any([book1,book2]))
read_any_book = print(all([book1,book2]))
