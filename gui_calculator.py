import tkinter as tk
from tkinter import messagebox
import math

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Extensive Calculator")
        self.root.geometry("400x600")
        self.expression = ""

        # Display Screen
        self.display_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.display_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Number Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row, column=col)
            col += 1
            if col == 4:
                col = 0
                row += 1

        # Function Buttons
        functions = [
            ('C', 1, 0), ('sqrt', 1, 1), ('^', 1, 2), ('log', 1, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('M+', 5, 3)
        ]

        for (text, row, col) in functions:
            action = lambda x=text: self.on_button_click(x)
            tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=row, column=col)

        # Memory Storage
        self.memory = 0

    def on_button_click(self, char):
        try:
            if char == 'C':
                self.expression = ""
                self.display_var.set("")
            elif char == '=':
                result = str(eval(self.expression))  # Warning: eval() can be unsafe for untrusted input.
                self.display_var.set(result)
                self.expression = result
            elif char == 'sqrt':
                result = str(math.sqrt(float(self.expression)))
                self.display_var.set(result)
                self.expression = result
            elif char == 'sin':
                result = str(math.sin(math.radians(float(self.expression))))
                self.display_var.set(result)
                self.expression = result
            elif char == 'cos':
                result = str(math.cos(math.radians(float(self.expression))))
                self.display_var.set(result)
                self.expression = result
            elif char == 'tan':
                result = str(math.tan(math.radians(float(self.expression))))
                self.display_var.set(result)
                self.expression = result
            elif char == '^':
                self.expression += '**'
                self.display_var.set(self.expression)
            elif char == 'log':
                result = str(math.log10(float(self.expression)))
                self.display_var.set(result)
                self.expression = result
            elif char == 'M+':
                self.memory = float(self.expression)
                messagebox.showinfo("Memory", f"Stored {self.memory} in memory.")
            else:
                self.expression += str(char)
                self.display_var.set(self.expression)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
