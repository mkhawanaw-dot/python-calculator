# Basic Python Calculator

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero")
            return
    else:
        print("Invalid operator")
        return

    print("Result:", result)

calculator()
