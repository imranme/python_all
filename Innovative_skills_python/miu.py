# calculator_combined.py
# Contains both CLI Calculator & GUI Calculator

import tkinter as tk


# ======================
# CLI CALCULATOR SECTION
# ======================
def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    elif op == '**':
        return a ** b
    elif op == '%':
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero.")
        return a % b
    else:
        raise ValueError("Unknown operator.")

def read_operator():
    valid = ['+', '-', '*', '/', '**', '%']
    while True:
        op = input("Choose operator (+, -, *, /, **, %): ").strip()
        if op in valid:
            return op
        print("Invalid operator. Try again.")

def cli_calculator():
    print("=== Python CLI Calculator ===")
    print("Type 'q' to quit.\n")

    while True:
        a_in = input("First number (or q to quit): ").strip()
        if a_in.lower() == 'q':
            print("Goodbye!")
            break
        try:
            a = float(a_in)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        op = read_operator()

        b_in = input("Second number: ").strip()
        try:
            b = float(b_in)
        except ValueError:
            print("Invalid number. Try again.")
            continue

        try:
            result = calculate(a, op, b)
            print(f"Result: {a} {op} {b} = {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")


# ======================
# GUI CALCULATOR SECTION
# ======================
class ModernCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern Calculator")
        self.geometry("320x420")
        self.resizable(False, False)
        self.configure(bg="#2C3E50")

        self.expression = ""
        self.result_var = tk.StringVar()

        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24, "bold"),
                         bg="#34495E", fg="white", bd=0, relief="flat", justify="right")
        entry.pack(fill="both", ipadx=8, ipady=15, pady=10, padx=10)

        btn_frame = tk.Frame(self, bg="#2C3E50")
        btn_frame.pack()

        buttons = [
            ("C", "#E74C3C"), ("(", "#16A085"), (")", "#16A085"), ("/", "#F39C12"),
            ("7", "#1ABC9C"), ("8", "#1ABC9C"), ("9", "#1ABC9C"), ("*", "#F39C12"),
            ("4", "#3498DB"), ("5", "#3498DB"), ("6", "#3498DB"), ("-", "#F39C12"),
            ("1", "#9B59B6"), ("2", "#9B59B6"), ("3", "#9B59B6"), ("+", "#F39C12"),
            ("0", "#E67E22"), (".", "#E67E22"), ("**", "#16A085"), ("=", "#27AE60"),
        ]

        row = 0
        col = 0
        for (text, color) in buttons:
            btn = tk.Button(btn_frame, text=text, font=("Arial", 14, "bold"),
                            bg=color, fg="white", activebackground="#2C3E50",
                            activeforeground="white", bd=0, relief="flat",
                            width=6, height=2,
                            command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_click(self, char):
        if char == "C":
            self.expression = ""
            self.result_var.set("")
        elif char == "=":
            try:
                result = eval(self.expression, {"__builtins__": {}}, {})
                self.result_var.set(result)
                self.expression = str(result)
            except:
                self.result_var.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)


# ======================
# MAIN PROGRAM ENTRY
# ======================
if __name__ == "__main__":
    print("Choose mode:")
    print("1. CLI Calculator (text-based)")
    print("2. GUI Calculator (window-based)")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        cli_calculator()
    elif choice == "2":
        app = ModernCalculator()
        app.mainloop()
    else:
        print("Invalid choice. Exiting...")
