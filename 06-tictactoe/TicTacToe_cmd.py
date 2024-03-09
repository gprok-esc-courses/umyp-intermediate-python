from models import Player, Board


def display_board(board):
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=' ')
        print()


def update_score(p_x, p_o, winner, tie):
    p_x.games_played += 1
    p_o.games_played += 1
    if tie:
        p_x.ties += 1
        p_o.ties += 1
    else:
        if p_x.symbol == winner:
            p_x.wins += 1
        else:
            p_o.wins += 1


player_x = Player('X')
player_o = Player('O')
board = Board()

while True:
    board.new_game()
    current_player = player_x
    while True:
        display_board(board.cells)
        try:
            row = int(input("Row: "))
            col = int(input("Col: "))
        except ValueError:
            print("Numbers only please")
            continue
        result = board.play(row, col, current_player)
        if not result:
            print("Wrong row or col")
        else:
            winner = board.winner()
            if winner is not None:
                display_board(board.cells)
                print(winner, " WINS!")
                update_score(player_x, player_o, winner, False)
                break
            if board.is_tie():
                display_board(board.cells)
                print("IT'S A TIE!")
                update_score(player_x, player_o, None, True)
                break
            current_player = player_o if current_player == player_x else player_x
    print("X: " + str(player_x.wins) + " O: " + str(player_o.wins))
    answer = input("Play again? (y/n): ")
    if answer == 'n':
        break
