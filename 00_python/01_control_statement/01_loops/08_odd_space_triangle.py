rows = int(input("Enter number of rows : "))
# a = rows
for i in range(1,rows+1):
    # for sp in range(a-1,0,-1):
    for sp in range(rows-i):
        print(" ",end="")
    # a = a-1
    for j in range(1,i*2):
        print(j,end="")
    print()