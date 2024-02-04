s = input("Enter the string : ")
n = int(input("Enter the n-th number : "))
s1 = list(s[0:n-1]) 
s2 = list(s[n-1:])
list1 = []
x = 122
while x >= 97 :
    list1.append(chr(x))
    x -= 1
list2 = list1.copy()
list2.reverse()

dict1 = dict(zip(list1,list2))
j = 0
for i in s2 :
    s2[j] = dict1[i]
    j += 1

final_str = s1 + s2
s3 = "".join(final_str)
print(s3)