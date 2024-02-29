from hangman import Hangman

hangman = Hangman()

while True:
    print("PLAY HANGMAN")
    hangman.start_new_game()

    while True:
        print(hangman.secret)
        letter = input("Enter Letter: ")
        hangman.play(letter)
        if hangman.is_hanged():
            print("HANGED :(")
            break
        if hangman.found():
            print("CONGRATS FOUND!")
            break

    answer = input("Play again? (y/n): ")
    if answer == 'n':
        break