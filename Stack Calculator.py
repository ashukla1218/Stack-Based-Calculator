import tkinter as tk
from tkinter import messagebox

priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
operators = {'+', '-', '*', '/', '(', ')', '^'}


def infixToPostfix(expression):
    stack, output = [], ''

    for char in expression:
        if char not in operators:
            output += char
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[char] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return False if output == expression else output


def calculate():
    exp = entry.get()
    postfix_expression = infixToPostfix(exp)

    if postfix_expression == False:
        messagebox.showerror("Error", "INVALID INPUT")
        result_label.config(text="Result: ", fg="#FF5733")
    else:
        result_label.config(text="Result: " + postfix_expression, fg="#2ECC71")


app = tk.Tk()
app.title("Infix to Postfix Calculator")
app.configure(bg='#3c3f41')
app.geometry("400x600")

expression_label = tk.Label(
    app, text="Enter an infix expression:", bg='#3c3f41', fg='white', font=('Helvetica', 14)
)
expression_label.place(x=10, y=10)

entry = tk.Entry(app, width=35, bg='#323232', fg='white', font=('Helvetica', 14))
entry.place(x=10, y=50)

buttons_frame = tk.Frame(app, bg='#323232')
buttons_frame.place(x=50, y=100)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '^', '+',
    'C', '⌫', '(', ')'
]

row_val, col_val = 0, 0


def on_button_click(key):
    if key == "C":
        entry.delete(0, tk.END)
    elif key == "⌫":
        entry.delete(len(entry.get()) - 1, tk.END)
    else:
        entry.insert(tk.END, key)


for button in buttons:
    if button:
        tk.Button(
            buttons_frame, text=button, padx=20, pady=15, font=('Helvetica', 14),
            bg='#4e5254', fg='white', relief="flat", command=lambda b=button: on_button_click(b)
        ).grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1




result_label = tk.Label(
    app, text="Result:", bg='#3c3f41', fg='#6a8759', font=('Helvetica', 14)
)
result_label.place(x=10, y=550)

calculate_button = tk.Button(
    app, text="Calculate", command=calculate, bg='#4e5254', fg='white', font=('Helvetica', 14)
)
calculate_button.place(x=160, y=500)


app.mainloop()



















