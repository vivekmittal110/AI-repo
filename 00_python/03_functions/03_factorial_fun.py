def fact(n):
    a = 1
    if n == 0:  
        return 1
    else :
        for i in range(1,n+1):
            a *= i
    return a

num = int(input("Enter a number : "))
print(fact(num))