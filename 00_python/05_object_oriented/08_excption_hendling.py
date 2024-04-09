# Exception hendling

# try 
    # code which might throw an exception(error)

# except
    # Exception type
        # value error
        # type error
        # zero division error
    # exception
# code to hendel the exception

# finally
    # code which will be executed regardless exception


# example practice

a = int(input("Enter the divident : "))
b = int(input("Enter the divisor : "))

try:
    result = a / b

except ZeroDivisionError:
    result = None
    print("Cannot divide by zero")

finally:
    print("Division : ",result)

