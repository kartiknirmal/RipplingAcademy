class Player:

    def __init__(self, turn, symbol):
        self.turn = turn
        self.symbol = symbol

    def get_next_input(self):
        print("Player", self.turn, "turn")
        string_input = input("Enter point coordinate: ").split(',')
        x = int(string_input[0])
        y = int(string_input[1])
        while x < 0 or x > 2 or y < 0 or y > 2:
            print("Coordinates out of range. Please enter valid coordinates!!!")
            string_input = input("Enter point coordinate: ").split(',')
            x = int(string_input[0])
            y = int(string_input[1])
        return x, y
