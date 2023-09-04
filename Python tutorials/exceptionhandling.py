x = input("enter number1: ")
y = input("enter number2: ")

try:
    z = int(x) / int(y)

except ZeroDivisionError as e:
    print("Division by zero exception occured: ",e)
    z = None
print("Division is: ",z)