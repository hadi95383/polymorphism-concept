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