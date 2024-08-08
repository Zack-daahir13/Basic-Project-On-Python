import tkinter as tk
from tkinter import ttk
def message():
    label.config(text = "hello somalia")
root = tk.Tk()
label = tk.Label(root, text="welcome to new label and open window")
root.title("hello tkinter")
root.config(background="green")
root.geometry("400x400")
lbl = tk.Label(root, text="click me")
lbl1 = tk.Label(root, text="home")
lbl2 = tk.Label(root, text="about")
lbl3 = tk.Label(root, text="contac")
lbl1.pack(side="left", expand=True, fill="y")
lbl.pack(side="left")
lbl2.pack(side="left")
lbl3.pack(side="left")

Treeview = ttk.Treeview(root, coloumns=("coloum1", "coloum2", "coloumn3", "coloumn4"))

label.pack()
btn = tk.Button(root, text="Sve me", command=message).pack()
root.mainloop()