# Importing necessary libraries
from tkinter import *
from tkinter import ttk
import random

# Charactors for random password
CHARACTORS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '^', '&', '*', '/', '?'
    ]

# Setting up the window
root = Tk()

root.geometry("330x150")
root.title("PW Generator")
root.resizable(0, 0)

# IntVar() for Radiobutton Value
myInt = IntVar()

# Password Generator
def pwGenerator():
    choice = myInt.get()
    pw = ''
    if choice == 1:
        for _ in range(12):
            pw += random.choice(CHARACTORS)
        result.delete(0, END)
        result.insert(0, pw)
    elif choice == 2:
        for _ in range(16):
            pw += random.choice(CHARACTORS)
        result.delete(0, END)
        result.insert(0, pw)
    else:
        result.delete(0, END)
        result.insert(0, "Chosse One")

# Header
title = ttk.Label(root, text="Password Generator")
title.grid(row=0, column=1, padx=5, pady=5)

# Label
radioLabel = ttk.Label(root, text="Choose Number")
radioLabel.grid(row=1, column=0, padx=5, pady=5)

# Radiobutton1
radio1 = ttk.Radiobutton(root, text="12 Characters", variable=myInt, value=1)
radio1.grid(row=1, column=1, padx=5, pady=5)

# Radiobutton2
radio2 = ttk.Radiobutton(root, text="16 Characters", variable=myInt, value=2)
radio2.grid(row=1, column=2, padx=5, pady=5)

# Button to trigger pwGenerator
button = ttk.Button(root, text="Generate", command=pwGenerator)
button.grid(row=3, column=1, padx=5, pady=5)

# Entry to show Password
result = ttk.Entry(root)
result.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
