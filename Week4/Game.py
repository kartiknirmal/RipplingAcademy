import Player as player

class Game:

    no_of_col = 3

    def __init__(self):
        self.board = self.Board()
        sym1 = input("Symbol for Player 1: ")
        sym2 = input("Symbol for Player 2: ")

        while sym1 == sym2:  # loops till player 2 selects different symbol.
            print(sym1, " is taken.")
            sym2 = input("Please select another symbol: ")

        self.player1 = player.Player(1, sym1)
        self.player2 = player.Player(2, sym2)

    def check_row(self) -> bool:                # return if game should continue.
        for x in self.board.cells:
            if ' ' in x:
                pass
            else:
                if x[0] == x[1] and x[1] == x[2]:
                    return True

        return False

    def check_col(self) -> bool:
        for x in range(self.no_of_col):
            if self.board.cells[0][x] == ' ':
                pass
            else:
                if self.board.cells[0][x] == self.board.cells[1][x] and self.board.cells[1][x] == self.board.cells[2][x]:
                    return True
        return False

    def check_diagonal(self) -> bool:
        if self.board.cells[0][0] == ' ':
            pass
        else:
            if self.board.cells[0][0] == self.board.cells[1][1] and self.board.cells[1][1] == self.board.cells[2][2]:
                return True

        if self.board.cells[0][2] == ' ':
            pass
        else:
            if self.board.cells[0][2] == self.board.cells[1][1] and self.board.cells[1][1] == self.board.cells[2][0]:
                return True

        return False

    def check_result(self):
        return self.check_row() or self.check_col() or self.check_diagonal()

    def start(self):
        turn = 1
        # game_on = True
        game_win = False
        while not game_win:
            if turn % 2 == 1:
                (x, y) = self.player1.get_next_input()
                if self.board.cells[x][y] == ' ':
                    self.board.cells[x][y] = self.player1.symbol
                    turn += 1
                else:
                    print("Cell occupied!!! Select another cell")

            else:
                (x, y) = self.player2.get_next_input()
                if self.board.cells[x][y] == ' ':
                    self.board.cells[x][y] = self.player2.symbol
                    turn += 1
                else:
                    print("Cell occupied!!! Select another cell")

            game_win = self.check_result()
            if game_win:
                self.board.show()
                print("Player", 2 if turn % 2 else 1, "wins.")
                break

            game_end = True  # flag to check if there are empty cells in the grid.
            for x in self.board.cells:
                for y in x:
                    if y == ' ':
                        game_end = False

            if game_end:
                self.board.show()
                print("Game draw")
                break

            self.board.show()
            
    class Board:
        def __init__(self):
            self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        def show(self) -> None:
            for x in self.cells:
                print("|", x[0], "|", x[1], "|", x[2], "|")



