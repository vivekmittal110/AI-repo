# it is an block of reusable code
# 1 in built function
# 2 user define function
# def sum(m,n):
#     ans = m+n
#     return ans

# a = 10
# b = 21
# sum = sum(a,b)
# print(sum)

# arbitary arguements (*agrs, **kwargs)

# *args is used when we don't know how many arguments are going to passed
# *args stores agruments as tuple
# def sum_all_number(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# output = sum_all_number(1,3,4,2,2,45)
# print("the sum is", output)

# keyworded arguements **kwargs where we pass keys and its values like dict
def student_info(**kwargs):
    for x,y in kwargs.items():
        print(x,y)

student_info(name = "vivek", roll_no = 621202022, age = 20)
