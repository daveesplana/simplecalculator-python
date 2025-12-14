import os
from dotenv import load_dotenv

cogs_list = [
    'addition',
    'subtraction',
    'multiplication',
    'division'
]

print("Welcome to my simple calculator!")

while True:
    try:
        a = float(input("Please enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Tip: use numbers only")

while True:
    c = input("Select an operation (+ - * /): ").strip()
    if c in "+-*/":
        break
    else:
        print("Invalid operation. Tip: choose one of + - * /")

while True:
    try:
        b = float(input("Great! Now enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Tip: use numbers only")

def calculate(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        if y == 0:
            return "Error: division by zero"
        return x / y
    return "Invalid operator"

result = calculate(a, b, c)
print("Result:", result)
