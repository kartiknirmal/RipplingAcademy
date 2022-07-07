import Player as m

class Game:

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __show(self):
        for x in self.board:
            print("|", x[0], "|", x[1], "|", x[2], "|")

    def __check_row(self) -> bool:                # return if game should continue.
        for x in self.board:
            if ' ' in x:
                pass
            else:
                if x[0] == x[1] and x[1] == x[2]:
                    return True

        return False

    def __check_col(self) -> bool:
        for x in range(3):
            if self.board[0][x] == ' ':
                pass
            else:
                if self.board[0][x] == self.board[1][x] and self.board[1][x] == self.board[2][x]:
                    return True
        return False

    def __check_diagonal(self) -> bool:
        if self.board[0][0] == ' ':
            pass
        else:
            if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                return True

        if self.board[0][2] == ' ':
            pass
        else:
            if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
                return True

        return False

    def __check_result(self):
        return self.__check_row() or self.__check_col() or self.__check_diagonal()

    def start(self, p1, p2):
        turn = 1
        # game_on = True
        game_win = False
        while not game_win:
            if turn % 2 == 1:
                (x, y) = p1.get_next_input()
                if self.board[x][y] == ' ':
                    self.board[x][y] = p1.symbol
                    turn += 1
                else:
                    print("Cell occupied!!! Select another cell")

            else:
                (x, y) = p2.get_next_input()
                if self.board[x][y] == ' ':
                    self.board[x][y] = p2.symbol
                    turn += 1
                else:
                    print("Cell occupied!!! Select another cell")

            game_win = self.__check_result()
            if game_win:
                print("Player", 2 if turn % 2 else 1, "wins.")
                self.__show()
                break

            game_end = True  # flag to check if there are empty cells in the grid.
            for x in self.board:
                for y in x:
                    if y == ' ':
                        game_end = False

            if game_end:
                print("Game draw")
                self.__show()
                break

            self.__show()


sym1 = input("Symbol for Player 1: ")
sym2 = input("Symbol for Player 2: ")

while sym1 == sym2:                         # loops till player 2 selects different symbol.
    print(sym1, " is taken.")
    sym2 = input("Please select another symbol: ")

player1 = m.Player(1, sym1)
player2 = m.Player(2, sym2)

# print(player1.symbol)
# print(player2.symbol)

game1 = Game()
game1.start(player1, player2)

