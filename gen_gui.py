from tkinter import *

import pyperclip

import random

# Initializing tkinter
root = Tk()

# Setting the width and height of GUI
root.geometry("400x400") 

# declaring variable of string type and this variablle will be 
# used to store the password generated
passStr = StringVar()

# Declaring a variable of integer type which will be used to 
# store the length of the password entered by the user
passLen = IntVar()

# Setting the length of the password to zero initially
passLen.set(0)

# Function to generate the password
def generate():
    # storing the keys in a list which will be used to generate password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    
    password = ""
    
    for x in range(passLen.get()):
        password = password + random.choice(pass1)
        
    passStr.set(password)

def copytoClipboard():
    random_password = passStr.get()
    pyperclip.copy(random_password)
    
Label(root, text="Password Generator", font="calibri 20 bold").pack()

Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable=passLen).pack(pady=3)

Button(root, text="Generate Password", command=generate).pack(pady=7)

Entry(root, textvariable=passStr).pack(pady=3)

Button(root, text="Copy to clipboard", command=copytoClipboard).pack(pady=3)

root.mainloop()