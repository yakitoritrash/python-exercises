def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    if n2==0:
        print("Undefined.")
    return n1/n2

operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
}

num1 = float(input("What is the first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = float(input("What is the next number? "))
answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
