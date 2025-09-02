from tkinter import *
from util import *
from math import pi

#Main window
root = Tk()
root.title("Basic calculator")
root.geometry("400x500")  # Set a default size

#4 columns
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

#6 rows
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

#Input field
entry = Entry(root, bg="white", fg="black", borderwidth=5, font=('Arial', 15))
entry.grid(columnspan=4, row=0, column=0, sticky="nsew", pady=20, padx=20)

#Entering numbers / operators clicked in the input field
def button_click(char):
    cur = entry.get()
    entry.delete(0, END)
    entry.insert(0,cur + str(char))


def get_pi():
    cur = entry.get()
    entry.delete(0, END)
    entry.insert(0,cur + str(pi))

#Clearing input field
def button_clear():
    entry.delete(0, END)
    
#evaluate expression entered in the input field
def button_equals(expression):
    try:
        result = evaluate(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except (ValueError, ZeroDivisionError):
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button colors
OPERATOR_COLOR = "#E1E566"
NUMBER_COLOR = "#FF2DD1"

# Define buttons
# First row
btn_percent = Button(root, text="%", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click("%"))
btn_power = Button(root, text="xⁿ", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click("^"))
btn_clear = Button(root, text="C", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=button_clear)
btn_add = Button(root, text="+", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click("+"))

# Second row
btn_7 = Button(root, text="7", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(7))
btn_8 = Button(root, text="8", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(8))
btn_9 = Button(root, text="9", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(9))
btn_subtract = Button(root, text="-", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click("-"))

# Third row
btn_4 = Button(root, text="4", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(4))
btn_5 = Button(root, text="5", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(5))
btn_6 = Button(root, text="6", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(6))
btn_divide = Button(root, text="÷", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click("/"))

# Fourth row
btn_1 = Button(root, text="1", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(1))
btn_2 = Button(root, text="2", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(2))
btn_3 = Button(root, text="3", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(3))
btn_multiply = Button(root, text="×", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click("*"))

# Fifth row
btn_sqrt = Button(root, text="𝜋", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=get_pi)
btn_0 = Button(root, text="0", bg=NUMBER_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click(0))
btn_decimal = Button(root, text=".", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_click("."))
btn_equals = Button(root, text="=", bg=OPERATOR_COLOR, fg="white", font=('Arial', 15), command=lambda: button_equals(entry.get()))

# Place buttons in grid
# First row
btn_percent.grid(row=1, column=0, sticky="nsew")
btn_power.grid(row=1, column=1, sticky="nsew")
btn_clear.grid(row=1, column=2, sticky="nsew")
btn_add.grid(row=1, column=3, sticky="nsew")

# Second row
btn_7.grid(row=2, column=0, sticky="nsew")
btn_8.grid(row=2, column=1, sticky="nsew")
btn_9.grid(row=2, column=2, sticky="nsew")
btn_subtract.grid(row=2, column=3, sticky="nsew")

# Third row
btn_4.grid(row=3, column=0, sticky="nsew")
btn_5.grid(row=3, column=1, sticky="nsew")
btn_6.grid(row=3, column=2, sticky="nsew")
btn_divide.grid(row=3, column=3, sticky="nsew")

# Fourth row
btn_1.grid(row=4, column=0, sticky="nsew")
btn_2.grid(row=4, column=1, sticky="nsew")
btn_3.grid(row=4, column=2, sticky="nsew")
btn_multiply.grid(row=4, column=3, sticky="nsew")

# Fifth row
btn_sqrt.grid(row=5, column=0, sticky="nsew")
btn_0.grid(row=5, column=1, sticky="nsew")
btn_decimal.grid(row=5, column=2, sticky="nsew")
btn_equals.grid(row=5, column=3, sticky="nsew")

root.mainloop()