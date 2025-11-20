# 🧮 Robust Calculator with diagnostics
print(">>> calculator_simple IMPORTED <<<")

import sys

# Переключатель режима отладки
DEBUG = True  # ← при необходимости переключи на False


def d(msg: str) -> None:
    """Print debug message if DEBUG is enabled."""
    if DEBUG:
        print(f"[DEBUG] {msg}")


def add(a: float, b: float) -> float:
    d(f"add({a}, {b})")
    return a + b


def subtract(a: float, b: float) -> float:
    d(f"subtract({a}, {b})")
    return a - b


def multiply(a: float, b: float) -> float:
    d(f"multiply({a}, {b})")
    return a * b


def divide(a: float, b: float):
    d(f"divide({a}, {b})")
    try:
        return a / b
    except ZeroDivisionError:
        d("ZeroDivisionError in divide()")
        return "❌ Error: Division by zero!"


def calculate(op: str, a: float, b: float):
    """Core calculation function with debug messages."""
    d(f"calculate(op={op!r}, a={a}, b={b})")

    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        d(f"Unknown operation: {op!r}")
        return "⚠️ Unknown operation"


def run_cli_debug() -> None:
    """
    Interactive CLI loop with diagnostics.
    Вынесено в отдельную функцию, чтобы можно было импортировать модуль в pytest,
    не запуская сразу input().
    """
    d("Program started (run_cli_debug)")

    while True:
        print("\n==========================")
        print(" Robust Calculator (DEBUG) ")
        print("==========================")
        print("Available operations: +  -  *  /")
        print("Type 'exit' to quit")
        print("------------------------------")

        op = input("Enter operation: ").strip()
        d(f"user entered operation: {op!r}")

        if op.lower() == "exit":
            print("Exiting program...")
            d("User requested exit → sys.exit(0)")
            sys.exit(0)

        try:
            a_raw = input("Enter first number: ").strip()
            b_raw = input("Enter second number: ").strip()
            d(f"raw inputs: a={a_raw!r}, b={b_raw!r}")

            a = float(a_raw)
            b = float(b_raw)
        except ValueError:
            print("⚠️ Error: please enter numbers only!")
            d("ValueError on number parsing → continue loop")
            continue

        d("before calculate()")
        result = calculate(op, a, b)
        d("after calculate()")

        print(f"✅ Result: {result}")


if __name__ == "__main__":
    # Важно для тестирования:
    # при запуске файла напрямую — стартует CLI,
    # при импортировании в pytest — НИЧЕГО не запускается автоматически.
    run_cli_debug()
