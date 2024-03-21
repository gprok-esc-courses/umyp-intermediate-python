from tkinter import Tk, Canvas

window = Tk()

canvas = Canvas(window, bg="cyan", width=400, height=400)
canvas.grid(row=0, column=0)

canvas.create_line(10, 10, 100, 100)
canvas.create_oval(120, 120, 200, 200)

window.mainloop()

