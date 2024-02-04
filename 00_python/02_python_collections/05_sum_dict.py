input1 = {
    "a" : 100,
    "b" : 200,
    "c" : 300,
}
print(sum(input1.values()))
sum = 0
for x in input1 :
    sum += input1[x]
print(sum)