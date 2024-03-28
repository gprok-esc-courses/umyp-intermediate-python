from tkinter import Tk, Canvas

def key_event(event):
    global pos_x, pos_y
    key = event.keysym
    if key == 'Up':
        pos_y = pos_y - 10
    elif key == 'Down':
        pos_y = pos_y + 10
    elif key == 'Left':
        pos_x = pos_x - 10
    elif key == 'Right':
        pos_x = pos_x + 10
    canvas.delete('all')
    canvas.create_rectangle(pos_x, pos_y, pos_x + size, pos_y + size, fill="black")



window = Tk()

pos_x = 190
pos_y = 190
size = 20

canvas = Canvas(window, bg="cyan", width=400, height=400)
canvas.grid(row=0, column=0)

canvas.create_rectangle(pos_x, pos_y, pos_x + size, pos_y + size, fill="black")

window.bind('<Key>', key_event)

window.mainloop()