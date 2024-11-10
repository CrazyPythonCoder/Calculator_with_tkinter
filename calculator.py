from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

root = Tk()

# root.iconbitmap(default=r'python.ico')

# Icon of window
icon = PhotoImage(file="images/icon.ico")
root.iconphoto(False, icon)

# Configurations of the window
root.title('Calculator')
root.geometry('600x400')
root.resizable(False, False)
root.config(bg='#2BD4DC')

# Images
add_icon = PhotoImage(file="images/add.png")
subtract_icon = PhotoImage(file="images/minus.png")
multiply_icon = PhotoImage(file="images/multiply.png")
divide_icon = PhotoImage(file="images/division.png")

# Functions

def add_func():
    try:
        result_entry.delete(0, END)
        result_entry.insert(0, int(num1_entry.get()) + int(num2_entry.get()))
    except Exception:
        if str(num1_entry.get()) or str(num2_entry.get()):
            messagebox.showerror('Error', 'Please enter a number!')
        

def sub_func():
    try:
        result_entry.delete(0, END)
        result_entry.insert(0, int(num1_entry.get()) - int(num2_entry.get()))
    except Exception:
        if str(num1_entry.get()) or str(num2_entry.get()):
            messagebox.showerror('Error', 'Please enter a number!')


def multi_func():
    try:
        result_entry.delete(0, END)
        result_entry.insert(0, int(num1_entry.get()) * int(num2_entry.get()))
    except Exception:
        if str(num1_entry.get()) or str(num2_entry.get()):
            messagebox.showerror('Error', 'Please enter a number!')
            

def divi_func():
    try:
        result_entry.delete(0, END)
        result_entry.insert(0, int(num1_entry.get()) / int(num2_entry.get()))
    except Exception:
        if str(num1_entry.get()) or str(num2_entry.get()):
            messagebox.showerror('Error', 'Please enter a number!')

# Labels
num1 = Label(root,
             text="Enter your first number:",
             font="verdana 12",
             fg='#FF5D00',
             bg='#FFCA4B')
num1.place(x=25, y=25)

num2 = Label(root,
             text="Enter your second number:",
             font='Verdana 12',
             fg='#FF5D00',
             bg='#FFCA4B')
num2.place(x=25, y=70)

result_lab = Label(root, 
                   text="Result:",
                   font="Verdana 12",
                   pady=5,
                   fg='#FF5D00',
                   bg='#FFCA4B')
result_lab.place(x=60, y=250)

# Entries
num1_entry = Entry(root, font="Verdana 15", fg='#FFBD00')
num1_entry.place(x=270 , y=25)

num2_entry = Entry(root, font="Verdana 15", fg='#FFBD00')
num2_entry.place(x=270 , y=70)

result_entry = Entry(root, font="Verdana 15", fg='#FFBD00', width=30)
result_entry.place(x=150 , y=250)

# Buttons
add_button = Button(root,
                    text="Add", 
                    padx=18, 
                    pady=5, 
                    relief="ridge", 
                    command=add_func,
                    image=add_icon,
                    compound=BOTTOM)
add_button.place(x=70, y=125)

subtract_button = Button(root, 
                         text="Subtract", 
                         padx=15, 
                         pady=5, 
                         relief="ridge", 
                         command=sub_func,
                         image=subtract_icon,
                         compound=BOTTOM)
subtract_button.place(x=193, y=125)

multi_button = Button(root,
                      text="Multiply",
                      padx=15, 
                      pady=6, 
                      relief="ridge", 
                      command=multi_func,
                      image=multiply_icon,
                      compound=BOTTOM)
multi_button.place(x=330, y=125)

divi_button = Button(root,
                    text="Divide",
                    padx=18,
                    pady=6,
                    relief="ridge",
                    command=divi_func,
                    image=divide_icon,
                    compound=BOTTOM)
divi_button.place(x=470, y=125) 

# Ending the mainloop
root.mainloop()
