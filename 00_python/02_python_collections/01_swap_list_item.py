list = [23,65,19,90]
# 23 == 19 swap places
# list[0], list[2] = list[2], list[0]
list[0] += list[2]
list[2] = list[0] - list[2]
list[0] = list[0] - list[2]
print(list)