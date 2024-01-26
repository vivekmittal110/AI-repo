# divisible by 3 and 5 but not by 15
num1 = int(input("Enter a number : "))
if ((num1 % 3 == 0 or num1 % 5 == 0) and num1 % 15 != 0):
    print("yes it is divisible")
else :
    print("it is not divisible")