import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create menu options
home_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Home", menu=home_menu)

about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=about_menu)

contact_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Contact", menu=contact_menu)

# Configure the menu bar background color
menu_bar.configure(bg="red")
exit()
#hiding DATA fields 

#this first code is unhide code data
class mango:
    __count = 20
    def __init__(self):
        print("this is unhide data field")
object = mango()
print(object._mango__count)


#hide data
class fruit:
    __count= 10
    def __init__(self):
        print("creat object data hide")

obj=fruit()
print(obj.__count)

#How do you define a private method?

class MyClass:
    def public_method(self):
        # Public method accessible from outside the class
        pass

    def _private_method(self):
        # Private method intended for internal use within the class
        pass


    