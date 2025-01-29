Polymorphic Calculator in Python
This repository contains a polymorphic calculator implemented in Python. The calculator demonstrates the power of polymorphism in Object-Oriented Programming (OOP) by allowing different mathematical operations (addition, subtraction, multiplication, and division) to be performed using the same interface.

Features
Polymorphism: The calculator uses polymorphism to perform different operations (addition, subtraction, multiplication, division) with the same interface.

Extensible: New operations can be easily added by creating new subclasses of the Operation base class.

Error Handling: The division operation includes error handling for division by zero.

How It Works
The calculator is built using the following components:

Base Class (Operation):

Defines a perform() method that must be implemented by all subclasses.

Derived Classes:

Addition: Performs addition of two numbers.

Subtraction: Performs subtraction of two numbers.

Multiplication: Performs multiplication of two numbers.

Division: Performs division of two numbers (with error handling for division by zero).

Calculator Class:

Takes an Operation object and uses its perform() method to calculate results.

Code Example
python
Copy
# Base class for all operations
class Operation:
    def perform(self, a, b):
        raise NotImplementedError("Subclasses must implement this method")

# Addition class
class Addition(Operation):
    def perform(self, a, b):
        return a + b

# Subtraction class
class Subtraction(Operation):
    def perform(self, a, b):
        return a - b

# Multiplication class
class Multiplication(Operation):
    def perform(self, a, b):
        return a * b

# Division class
class Division(Operation):
    def perform(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

# Calculator class
class Calculator:
    def __init__(self, operation):
        self.operation = operation

    def calculate(self, a, b):
        return self.operation.perform(a, b)

# Usage
if __name__ == "__main__":
    # Create operation objects
    add = Addition()
    subtract = Subtraction()
    multiply = Multiplication()
    divide = Division()

    # Create calculator with different operations
    calculator = Calculator(add)
    print("10 + 5 =", calculator.calculate(10, 5))  # Output: 15

    calculator = Calculator(subtract)
    print("10 - 5 =", calculator.calculate(10, 5))  # Output: 5

    calculator = Calculator(multiply)
    print("10 * 5 =", calculator.calculate(10, 5))  # Output: 50

    calculator = Calculator(divide)
    print("10 / 5 =", calculator.calculate(10, 5))  # Output: 2.0
    print("10 / 0 =", calculator.calculate(10, 0))  # Output: Error: Division by zero!
How to Run the Code
Clone this repository:

bash
Copy
git clone https://github.com/hadi95383/polymorphic-calculator.git
Navigate to the repository directory:

bash
Copy
cd polymorphic-calculator
Run the Python script:

bash
Copy
python calculator.py
Output
When you run the script, you should see the following output:

Copy
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 / 0 = Error: Division by zero!
Key Concepts Demonstrated
Polymorphism: The same Calculator class can perform different operations using the same perform() method.

Inheritance: Each operation class inherits from the Operation base class and overrides the perform() method.

Error Handling: The division operation handles division by zero gracefully.

Extending the Calculator
To add a new operation (e.g., exponentiation), follow these steps:

Create a new subclass of Operation:

python
Copy
class Power(Operation):
    def perform(self, a, b):
        return a ** b
Use the new operation with the calculator:

python
Copy
power = Power()
calculator = Calculator(power)
print("2 ^ 3 =", calculator.calculate(2, 3))  # Output: 8
Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request. All contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Connect with Me
GitHub:https://github.com/hadi95383
Email: hadikhan95383@gmail.com
