def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def calculate(num1, operator, num2):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return sub(num1, num2)
    elif operator == '*':
        return mul(num1, num2)
    elif operator == '/':
        return div(num1, num2)
    else:
        return "Invalid operator!"

def main():
    num1 = float(input("Type the number you want to perform operations on: "))
    
    while True:
        print("+ \n- \n* \n/")
        operator = input("Pick an operator: ")
        num2 = float(input("What's the next number? "))
        
        result = calculate(num1, operator, num2)
        print(f"The result of {num1} {operator} {num2} is: {result}")
        
        cont = input("If you want to continue with this number type 'y' or if you want to start calculations with a new number type 'n'. To exit, type 'exit': ")
        
        if cont == 'y':
            num1 = result
        elif cont == 'n':
            num1 = float(input("Type the number you want to perform operations on: "))
        elif cont == 'exit':
            break
        else:
            print("Invalid input. Exiting.")
            break

if __name__ == "__main__":
    main()