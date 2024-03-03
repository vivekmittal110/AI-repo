def sum(n):
    if n == 1:
        return 1
    ans = n + sum(n-1)
    return ans
print(sum(5))