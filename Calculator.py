def simple_calculator():
    print("Calculator!")
  
    num1 = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
  
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operation!"

    return f"The result of {num1} {operation} {num2} is: {result}"

print(simple_calculator())
