def sum(num):
    ans = 0
    for i in range(1,num+1):
        ans += i
    return ans

n = int(input("Enter n-th term: "))
print(sum(n))