def rev(n):
    if n == 0:
        return
    rev(n-1)
    print(n)

rev(4)