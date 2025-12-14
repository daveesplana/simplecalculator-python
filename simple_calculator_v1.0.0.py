print("Welcome to my simple calculator!")

while True:
    try:
        Firstnum = float(input("Please enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Tip: use numbers only")

while True:
    Operation = input("Select an operation (+ - * /): ")
    if Operation in "+-*/":
        break
    else:
        print("Invalid operation. Tip: choose one of + - * /")

while True:
    try:
        Secondnum = float(input("Great! Now enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Tip: use numbers only")


def calculate(Firstnum, Secondnum, Operation):
    if Operation == "+":
        return Firstnum + Secondnum
    elif Operation == "-":
        return Firstnum - Secondnum
    elif Operation == "*":
        return Firstnum * Secondnum
    elif Operation == "/":
        return Firstnum / Secondnum
    else:
        return "Invalid operator"

result = calculate(Firstnum, Secondnum, Operation)
print("Result:", result)