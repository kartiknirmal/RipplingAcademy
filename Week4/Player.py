class Player:

    def __init__(self, turn, symbol):
        self.turn = turn
        self.symbol = symbol

    def get_next_input(self):
        print("Player", self.turn, "turn")
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        return x, y
