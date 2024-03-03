def power(x,y):
    if y == 0:
        return 1
    ans = x * power(x,y-1)
    return ans

a = int(input("Enter base : "))
b = int(input("Enter power : "))
print(power(a,b))
# 2*2*2*2 = 16