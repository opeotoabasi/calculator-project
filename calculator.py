# calculator app
def add(a, b):
    return a + b

#hmmmm
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b




def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an operation: ")
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        return

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if choice == "1":
        print("The sum is:", add(x, y))
    elif choice == "2":
        print("The difference is:", subtract(x, y))
    elif choice == "3":
        print("The product is:", multiply(x, y))
    else:
        try:
            print("The quotient is:", divide(x, y))
        except ValueError as error:
            print(error)


menu()

    

# person 2 make the fuunctions ie addition, subtraction, multiplication, division
# person 3 make the menu for the calculator app
