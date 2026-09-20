🧮 Python Console Calculators

Two educational Python console projects for learning functions, loops, debugging, and error-handling.
Located in: apps/calculator_app/

📌 Project Overview

This folder contains two training calculators:

calculator_simple.py
A basic calculator supporting addition, subtraction, multiplication, and division.

calculator_debug.py
An enhanced version with detailed debug messages to help understand program flow.

Both scripts are built as part of a learning journey toward Python development and QA Automation.

⚙️ How to Run
▶ Run the Simple Calculator
python calculator_simple.py

▶ Run the Debug Calculator
python calculator_debug.py

🧠 Features
Simple Calculator

Supports: +, -, *, /

Gracefully handles division by zero (try/except)

Infinite loop until the user types "exit"

Clean structure with standalone functions:

add()

subtract()

multiply()

divide()

calculate()

Debug Calculator

Shows [DEBUG] messages before and after each operation

Helps visualize how functions and loops behave internally

Useful for beginners learning Python flow control and diagnostics

🧪 Testing (pytest)

A full unit-test suite is included (in the same folder) for both calculators:

test_calculator_simple.py

test_calculator_debug.py

test_smoke.py

Run all tests:

python -m pytest -vv


Run a specific test file:

python -m pytest test_calculator_simple.py -vv


Run a specific test:

python -m pytest test_calculator_simple.py::test_add -vv

🎯 Purpose

These calculators were created as part of a structured learning path covering:

Python fundamentals

Functions and return values

Loops and logic

Error handling

Writing testable code

Building QA Automation skills

Preparing for Backend + FinTech roles

🚀 Next Steps

Planned future improvements:

Add colored console output (colorama)

Add logging instead of debug print

Create a GUI version (Tkinter)

Package into .exe using PyInstaller

Build an API version using FastAPI

Create Docker container + Postman testing collection

👨‍💻 About Me

I am learning Python, QA Automation, SQL, API testing, and automation tools as part of my journey to become a QA Automation Engineer / Python Developer, with a strong interest in FinTech systems.

🪪 License

This project is distributed under the MIT License, which allows free use, modification, and distribution.
See the LICENSE file for details.




