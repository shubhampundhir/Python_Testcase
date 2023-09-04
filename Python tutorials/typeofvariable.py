total = 0 #global variable outside function definition
def sum(a,b):
    print("a: ",a)
    print("b: ",b)
    total = a + b #local variable inside function definition
    print("total inside function: ",total)
    return total

n = sum(b=9,a=6)
print("total outside function: ",total)