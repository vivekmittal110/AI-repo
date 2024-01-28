# Sets items
'''
unordered
immutable
unindex
Dublicates are not allowed
any data type
mix of different data type
'''

set1 = {"vivek", "nitin", "mannat", "ayush"}
print(set1)

# check lenght of a set
print(len(set1))

# check data type of a set
print(type(set1))

# accessing items of a sets
for i in set1:
    print(i)
print(i)

# check itme if it is exist in set
if "vivek" in set1:
    print("yes")

# add elements in a set
set1.add("archit")
set1.add("nitin") # not added becaus it is already present in a set
print(set1)

# add another sequence in a set
names_list = ["piyush", "kartik"]
set1.update(names_list)
print(set1)

# remove an element from a set
set1.remove("piyush")
print(set1)

set1.discard("kartik") # this function will not throw an error if element is not present in a set
print(set1)

# join 2 sets
set2 = {'a', "b","nitin"}
set3 = set1.union(set2)
print(set3)

# keep only dublicates values while joining
# set1.intersection_update(set2)
print(set1)

# keep all values except dublicates
set1.symmetric_difference_update(set2)
print(set1)


# find common values
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,10]
ar3 = [3,4,15,20,30,70,80,120]

ar1 = set(ar1)
ar2 = set(ar2)
ar3 = set(ar3)
ar1.intersection_update(ar2)
ar1.intersection_update(ar3)

ar1 = list(ar1)
print(ar1)