num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

operator = input("Enter operator : ")

match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _ :
        print("Enter valid operator")