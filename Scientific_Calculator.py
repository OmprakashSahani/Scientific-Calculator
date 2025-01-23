# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:34:35 2025

@author: OMPRAKASH
"""

from tkinter import *
import math

def calculate():
    try:
        expression = input_field.get()
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# GUI setup
root = Tk()
root.title("Scientific Calculator")

# Input field
input_field = Entry(root, font=("Arial", 18), width=20, borderwidth=2)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    "7", "8", "9", "/", "sqrt",
    "4", "5", "6", "*", "pow",
    "1", "2", "3", "-", "log",
    "0", ".", "=", "+", "%",
    "(", ")", "clear", "!", "mod"
]

def button_click(btn):
    if btn == "=":
        calculate()
    elif btn == "clear":
        input_field.delete(0, END)
    elif btn == "sqrt":
        input_field.insert(END, "math.sqrt(")
    elif btn == "pow":
        input_field.insert(END, "")
    elif btn == "log":
        input_field.insert(END, "math.log(")
    elif btn == "!":
        input_field.insert(END, "math.factorial(")
    elif btn == "mod":
        input_field.insert(END, "%")
    else:
        input_field.insert(END, btn)

# Create buttons dynamically
row, col = 1, 0
for btn in buttons:
    Button(root, text=btn, font=("Arial", 14), width=5, height=2, command=lambda b=btn: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Result display
result_label = Label(root, text="", font=("Arial", 14))
result_label.grid(row=row+1, column=0, columnspan=5, pady=10)

root.mainloop()