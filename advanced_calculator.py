import math


class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    # Basic operations
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self.history.append(f"{a} / {b} = Error (Division by Zero)")
            return "Error: Division by zero"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    # Advanced operations
    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def sqrt(self, a):
        if a < 0:
            self.history.append(f"sqrt({a}) = Error (Negative number)")
            return "Error: Cannot take square root of a negative number"
        result = math.sqrt(a)
        self.history.append(f"sqrt({a}) = {result}")
        return result

    # Trigonometric functions
    def sin(self, a):
        result = math.sin(math.radians(a))
        self.history.append(f"sin({a}) = {result}")
        return result

    def cos(self, a):
        result = math.cos(math.radians(a))
        self.history.append(f"cos({a}) = {result}")
        return result

    def tan(self, a):
        result = math.tan(math.radians(a))
        self.history.append(f"tan({a}) = {result}")
        return result

    # Logarithmic functions
    def log(self, a, base=10):
        if a <= 0:
            self.history.append(f"log({a}, base {base}) = Error (Non-positive number)")
            return "Error: Logarithm of a non-positive number"
        result = math.log(a, base)
        self.history.append(f"log({a}, base {base}) = {result}")
        return result

    # Memory functions
    def memory_store(self, value):
        self.memory = value
        return f"Stored {value} in memory."

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0
        return "Memory cleared."

    # History of calculations
    def show_history(self):
        if not self.history:
            return "No calculations in history."
        return "\n".join(self.history)

    def clear_history(self):
        self.history = []
        return "Calculation history cleared."


# CLI for calculator
def main():
    calc = Calculator()

    while True:
        print("\n--- Extensive Calculator ---")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: Power")
        print("6: Square Root")
        print("7: Sin")
        print("8: Cos")
        print("9: Tan")
        print("10: Log")
        print("11: Memory Store")
        print("12: Memory Recall")
        print("13: Memory Clear")
        print("14: Show History")
        print("15: Clear History")
        print("16: Exit")

        choice = input("Choose an operation: ")

        if choice == "16":
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input, please enter numeric values.")
                continue

            if choice == "1":
                print("Result:", calc.add(a, b))
            elif choice == "2":
                print("Result:", calc.subtract(a, b))
            elif choice == "3":
                print("Result:", calc.multiply(a, b))
            elif choice == "4":
                print("Result:", calc.divide(a, b))
            elif choice == "5":
                print("Result:", calc.power(a, b))

        elif choice == "6":
            try:
                a = float(input("Enter number: "))
                print("Result:", calc.sqrt(a))
            except ValueError:
                print("Invalid input, please enter a numeric value.")

        elif choice in ["7", "8", "9"]:
            try:
                a = float(input("Enter angle in degrees: "))
                if choice == "7":
                    print("Result:", calc.sin(a))
                elif choice == "8":
                    print("Result:", calc.cos(a))
                elif choice == "9":
                    print("Result:", calc.tan(a))
            except ValueError:
                print("Invalid input, please enter a numeric value.")

        elif choice == "10":
            try:
                a = float(input("Enter number: "))
                base = input("Enter base (default 10): ")
                base = float(base) if base else 10
                print("Result:", calc.log(a, base))
            except ValueError:
                print("Invalid input, please enter valid numeric values.")

        elif choice == "11":
            try:
                value = float(input("Enter value to store in memory: "))
                print(calc.memory_store(value))
            except ValueError:
                print("Invalid input, please enter a numeric value.")

        elif choice == "12":
            print("Memory Recall:", calc.memory_recall())

        elif choice == "13":
            print(calc.memory_clear())

        elif choice == "14":
            print("Calculation History:")
            print(calc.show_history())

        elif choice == "15":
            print(calc.clear_history())

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
