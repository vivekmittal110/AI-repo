def rev(n):
    if n == 0:
        return
    print(n)
    rev(n-1)
num = int(input("Enter nth number : "))
rev(num)