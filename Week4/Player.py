class Player:

    def __init__(self, turn, symbol):
        self.turn = turn
        self.symbol = symbol

    def get_next_input(self):
        print("Player", self.turn, "turn")
        string_input = input("Enter point coordinate: ").split(',')
        x = int(string_input[0])
        y = int(string_input[1])
        return x, y
