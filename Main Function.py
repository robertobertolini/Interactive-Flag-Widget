
# coding: utf-8

# In[12]:

# Roberto Bertolini and Tiffany Roberti

# This program creates the graphical user interface that allows the user to
# input the name of a flag and the program will open the respective py file
# to draw the flag using Turtle graphics.

# DIRECTIONS:

# Please note that you only need to run this program in order for the remaining files to execute.
# For best quality, it must be run in Jupyter notebooks!
# Please make sure the all five files (the four python files) and the "Flag.gif" image are saved
# in the same folder on your computer. we have been running the program using Jupyer notebook.

# After the program is run, type in the name of one of the three countries from the list. You must 
# type it exactly as shown or a dialogue box with prompt you to correct your input. You can only
# run one flag at a time. If you have drawn one flag and you want to draw another one, you must close 
# the current flag window before proceeding to typing another flag.

# Please note you have to click twice on the buttons for them to run.

import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from contextlib import closing

# Creates the Toplevel window, the background color for the window, and
# prints the introductory text and hides the root window.

root = tkinter.Tk()
root.withdraw()
window = tkinter.Toplevel()
window.configure(background="#a1dbcd")
window.title("Welcome to the Flag Generator")

# Adds the flag photograph to the graphical user interface

image = Image.open("Flag.gif")
image = image.resize((800,300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
w = tkinter.Label(window, image=photo)
w.pack()

# Creates an entry box so the user can input the country name so the flag can be generated

lblFlag = tkinter.Label(window,text = "Select a Country: 'USA', 'China', 'Bulgaria'", fg = "#383a39", bg="#a1dbcd", font=("Times New Roman",16))
entFlag = tkinter.Entry(window)
lblFlag.pack()
entFlag.pack()

# The action function calls the respective py file based upon the user input. If the name that the user inputs
# is incorrect, the program prints a statement telling them to correct their input.

def Action():
    entry1 = entFlag.get()
    if entry1=="USA":
        get_ipython().magic('run American.py')
        window.protocol("WM_DELETE_WINDOW", close_window)
    if entry1=="China":
        get_ipython().magic('run Chinese.py')
        window.protocol("WM_DELETE_WINDOW", close_window)
    if entry1=="Bulgaria":
        get_ipython().magic('run Bulgaria.py')
        window.protocol("WM_DELETE_WINDOW", close_window)
    else:
        messagebox.showinfo("Flag Generator", "Input is not correct. Please correct it!")

# Quits out of the program when the user presses the exit button

def close_window(): 
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
    else:
        root.destroy()
        
# Creates the generate flag button
    
button = tkinter.Button(window,text = "Generate Flag",fg = "#383a39", bg="#a1dbcd",command = Action)
button.pack()

# Creates the frame and the exit button

frame = tkinter.Frame(window)
frame.pack()

button = tkinter.Button(frame, text = "Exit", fg = "#383a39", bg="#a1dbcd",command = close_window)
button.pack()

window.protocol("WM_DELETE_WINDOW", close_window)
window.mainloop()

