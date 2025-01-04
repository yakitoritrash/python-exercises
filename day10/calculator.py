num1 = float(input("Type the number you want to perform operations on? "))

print("+ \n- \n* \n/")

operator = input("Pick an operator: ")

num2 = float(input("What's the next number? "))

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

if operator == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operator == '-':
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif operator == '*':
    print(f"{num1} * {num2} = {mul(num1, num2)}")
else:
    print(f"{num1} / {num2} = {div(num1, num2)}")


