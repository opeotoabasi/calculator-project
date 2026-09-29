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


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("The sum is:", x + y)
print("The difference is:", x - y)
print("The product is:", x * y)
print("The quotient is:", x / y)

# person 2 make the fuunctions ie addition, subtraction, multiplication, division
# person 3 make the menu for the calculator app
