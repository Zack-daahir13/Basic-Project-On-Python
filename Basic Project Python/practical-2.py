import tkinter as tk

def open_file():
    print("Open file")

def save_file():
    print("Save file")

def exit_program():
    print("Exit program")
    root.quit()

# Create the main window
root = tk.Tk()
root.geometry("400x300")  # Set window size

# Create a menu bar
menubar = tk.Menu(root)

# Create a "File" menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)

# Add the "File" menu to the menu bar
menubar.add_cascade(label="File", menu=file_menu)

# Configure the root window to use the menu bar
root.config(menu=menubar)

# Create a checkbox
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Enable", variable=checkbox_var)

# Pack the checkbox
checkbox.pack(pady=10)

# Start the main event loop
root.mainloop()




exit()
class artirist:
    def __init__(self, firstnum1=0, secondnum2=0):
        self.firstnum1=firstnum1
        self.secondnum2=secondnum2
        
        
    def getaddition(self):
        result = self.firstnum1 + self.secondnum2
        return result
    
    def substraction (self, first, second):
        self.first= first
        self.second = second
    
add = artirist(2, 4)
print(add.getaddition())
add.substraction(8, 6)
print(add.getaddition())


class studentregistration:
  def __init__(self, name, job, age, town, education):
    self.name = name
    self.job = job
    self.age = age
    self.tow = town
    self.education = education

person = studentregistration("sakariye", "student", "19", "london", "computer science" )
print(person.name)
print(person.job)
print(person.age)
print(person.town)
print(person.education)
        
        
        