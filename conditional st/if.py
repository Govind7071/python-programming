'''age=int(input('enter the age: '))
if age>=18:
 print('eligible for vote')'''
def add(x, y):
    # Function for addition
    return x + y

def subtract(x, y):
    # Function for subtraction
    return x - y

def multiply(x, y):
    # Function for multiplication
    return x * y

def divide(x, y):
    # Function for division, handles ZeroDivisionError
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def basic_calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Get user input for the operation
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid Input")
        return

    try:
        # Get user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.")
        return

    # Perform calculation based on choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    else:
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

basic_calculator() # Uncomment to run the program
# The question asks to design the calculator, so the functions and 
# the selection logic are the core design.