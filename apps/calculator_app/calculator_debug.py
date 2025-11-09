# 🧮 Robust Calculator with diagnostics
    import sys

    DEBUG = True  # ← при необходимости переключи на False

    def d(msg):
        if DEBUG:
            print(f"[DEBUG] {msg}")

    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "❌ Error: Division by zero!"

    def calculate(op, a, b):
        d(f"calculate() called with op={repr(op)}, a={a}, b={b}")
        if op == "+": return add(a, b)
        elif op == "-": return subtract(a, b)
        elif op == "*": return multiply(a, b)
        elif op == "/": return divide(a, b)
        else: return "⚠️ Unknown operation"

    print("== CALC START ==", __file__)  # поможет убедиться, что запускается нужный файл

    while True:
        print("\n==================")
        print(" Simple Python Calculator ")
        print("==================")
        print("Available operations: + - * /")
        print("Type 'exit' to quit")
        print("----------------------")

        op = input("Enter operation: ").strip()  # ВАЖНО: .strip()

        if op.lower() == "exit":
            print("Exiting program...")
            sys.exit(0)

        try:
            a = float(input("Enter first number: ").strip())   # ВАЖНО: .strip()
            b = float(input("Enter second number: ").strip())  # ВАЖНО: .strip()
        except ValueError:
            print("⚠️ Error: please enter numbers only!")
            d("ValueError on number parsing → continue loop")
            continue

        d("before calculate()")
        result = calculate(op, a, b)
        d("after calculate()")

        print(f"✅ Result: {result}")
