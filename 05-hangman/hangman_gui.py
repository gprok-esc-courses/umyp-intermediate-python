from tkinter import Tk, Label, Entry, Button
from hangman import Hangman

def play_event():
    letter = letter_field.get()
    hangman.play(letter)
    secret_label.configure(text=hangman.secret)
    if hangman.is_hanged():
        result_label.configure(text="HANGED :(")
        play_button['state'] = "disabled"
    if hangman.found():
        result_label.configure(text="FOUND :)")
        play_button['state'] = "disabled"
    letter_field.delete(0, 'end')

def play_again_event():
    hangman.start_new_game()
    secret_label.configure(text=hangman.secret)
    result_label.configure(text="-")
    play_button['state'] = "normal"

window = Tk()
hangman = Hangman()

hangman.start_new_game()

window.geometry("300x400")
window.title("HANGMAN")

secret_label = Label(window, text=hangman.secret)
secret_label.grid(row=0, column=0)
letter_field = Entry(window)
letter_field.grid(row=1, column=0)
play_button = Button(window, text="PLAY", command=play_event)
play_button.grid(row=2, column=0)
result_label = Label(window, text='-')
result_label.grid(row=3, column=0)
play_again_button = Button(window, text="Play Again", command=play_again_event)
play_again_button.grid(row=4, column=0)

window.mainloop()


