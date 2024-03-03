def fact(n):
    ans = 1
    if n == 0:
        return 1
    else:
        ans = n * fact(n-1)
        return ans
num = int(input("Enter a number : "))
print(fact(num))