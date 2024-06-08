def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number!")
    return x ** 0.5

def exponentiation(x, y):
    return x ** y

def calculator():
    print("Welcome to Simple Calculator App!")
    print("Operations available:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Quit")

    while True:
        choice = input("Enter operation number (1-7): ")

        if choice in ['1', '2', '3', '4', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
                elif choice == '6':
                    print("Result:", exponentiation(num1, num2))
            except ValueError as e:
                print("Invalid input:", e)
        elif choice == '5':
            try:
                num = float(input("Enter number: "))
                print("Result:", square_root(num))
            except ValueError as e:
                print("Invalid input:", e)
        elif choice == '7':
            print("Thank you for using Simple Calculator App!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    calculator()
