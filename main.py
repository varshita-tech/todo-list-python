from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x400")

def hello():
    label.config(text="My First Python Project")

button = Button(root, text="Click Me", command=hello)
button.pack(pady=20)

label = Label(root, text="")
label.pack()

root.mainloop()