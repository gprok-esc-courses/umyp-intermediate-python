from typing import List


class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.games_played = 0
        self.wins = 0
        self.ties = 0


class Board:
    def __init__(self):
        self.cells = self.get_empty_board()

    def get_empty_board(self) -> List[List]:
        """
        Creates and return a list of 3 rows x 3 columns containing '-' characters
        """
        return [['-']*3 for i in range(3)]

    def new_game(self) -> None:
        """
        Initialises a new game by creating an empty board of cells
        """
        self.cells = self.get_empty_board()

    def play(self, row: int, col: int, player: Player) -> bool:
        """
        Marks the board with the symbol of the player who played
        :param row: The row (0-2)
        :param col: The column (0-2)
        :param player: A player object
        :return: True if succeeded, False otherwise
        """
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        if self.cells[row][col] == '-':
            self.cells[row][col] = player.symbol
            return True
        else:
            return False

    def winner(self) -> str:
        """
        Checks each row and column, then the 2 diagonals for same values
        :return: The symbol of the winner, None otherwise if no winner found
        """
        for i in range(3):
            if self.cells[i][0] == self.cells[i][1] == self.cells[i][2] and self.cells[i][0] != '-':
                return self.cells[i][0]
            if self.cells[0][i] == self.cells[1][i] == self.cells[2][i] and self.cells[0][i] != '-':
                return self.cells[0][i]
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] and self.cells[1][1] != '-':
            return self.cells[1][1]
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] and self.cells[1][1] != '-':
            return self.cells[1][1]
        return None

    def is_tie(self) -> bool:
        """
        Check every cell to find '-' which means empty cells still exist.
        If no empty cells, this means it's a tie.
        :return: True if it is a tie, False otherwise
        """
        for row in range(3):
            for col in range(3):
                if self.cells[row][col] == '-':
                    return False
        return True
