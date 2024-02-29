# call by value (immutable objects like int, str,  tuple)

# call by reference (objects like list, set, dict)
def modify_list(lst):
    lst.append(4)
    print(lst)

lst1 = [1,2,3]
modify_list(lst1)
print("After calling modify_list:", lst1)