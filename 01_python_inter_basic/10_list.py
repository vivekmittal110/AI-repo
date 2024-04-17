dogs = ["abc", "dfc", 1, True]
print("abc" in dogs)
print(dogs[0])

dogs[2] = "mouse"
print(dogs)

# accessing the list
print(dogs[-2])

print(dogs[1:3])

# add items in a list
dogs.append("cat")
print(dogs)

dogs.extend(["bird", "fish"])
dogs += ["rat", "elephant"]
print(dogs)

dogs.insert(1, "nothing")

# deleting the items in a list
dogs.remove("abc")
print(dogs)

print(dogs.pop())
print(dogs)

# sort a list (don't sort multiple data types)
names = ["vivek", "ayush", "nitin", "anyone"]
names.sort()
print(names)
# # it will sort capitilized alfabet first
names2 = ["Ayush","ayush","Vivek","nitin"]
names2.sort()
print(names2)
# if you want to sort in according to alfabet what ever the case(upper/lower)
names2.sort(key=str.lower)
print(names2)
# shorted
print(sorted(names2)) # it will return sorted list without modifying the original list