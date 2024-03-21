from tkinter import Tk, Button, Label, Frame
from models import Player, Board

def play_again():
    board.new_game()
    for btn in buttons:
        btn.configure(text='-')
    message.configure(text="Game in progress")

def button_clicked(event, row, column):
    global current
    print(row, column)
    if board.play(row, column, current):
        btn = event.widget
        btn.configure(text=current.symbol)
        current = player_x if current == player_o else player_o
        winner = board.winner()
        if winner is not None:
            msg = winner + " wins!"
            message.configure(text=msg)
        if board.is_tie():
            message.configure(text="It's a Tie")

player_x = Player('X')
player_o = Player('O')
current = player_x

board = Board()
board.new_game()

window = Tk()

frame = Frame(window)
buttons = []
for row in range(3):
    for col in range(3):
        button = Button(frame, text="-")
        button.bind("<Button-1>", lambda event, r=row, c=col: button_clicked(event, r, c))
        buttons.append(button)
        button.grid(row=row, column=col)

frame.grid(row=0, column=0)

play_btn = Button(window, text="Play Again", command=play_again)
play_btn.grid(row=1, column=0)

message = Label(window, text="Game in progress")
message.grid(row=2, column=0)

window.mainloop()

