def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

calculator(x, y)