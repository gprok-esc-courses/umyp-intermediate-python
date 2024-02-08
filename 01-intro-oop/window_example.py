# I don't expect to learn windows programming, YET.

from tkinter import Tk, Button, Label, Entry
import random


def button_clicked():
    r = random.randint(1, 1000)
    message = "Hello " + entry.get() + " you won $" + str(r)
    label.configure(text=message)


window = Tk()

window.geometry("600x400")

button = Button(window, text="Click me!", command=button_clicked)
button.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=1, column=0)

label = Label(window, text="-")
label.grid(row=2, column=0)

window.mainloop()