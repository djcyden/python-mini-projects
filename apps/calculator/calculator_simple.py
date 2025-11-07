# 🧮 Simple Python Calculator (clean version)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "❌ Error: Division by zero!"

def calculate(op, a, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "⚠️ Unknown operation"

while True:
    print("\n==================")
    print(" Simple Python Calculator ")
    print("==================")
    print("Available operations: +  -  *  /")
    print("Type 'exit' to quit")
    print("----------------------")

    op = input("Enter operation: ").strip()

    if op.lower() == "exit":
        print("Exiting program...")
        break  # ← здесь программа прерывает цикл и выходит

    try:
        a = float(input("Enter first number: ").strip())
        b = float(input("Enter second number: ").strip())
    except ValueError:
        print("⚠️ Error: please enter numbers only!")
        continue  # возвращает в начало цикла

    result = calculate(op, a, b)
    print(f"✅ Result: {result}")
