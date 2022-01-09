class TicTacToe:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.divider = '_+_+_'
        self.playerX = 'x'
        self.playerO = 'o'

        self.prompt = ' turn to chose a square (1-9): '
        self.input = ''

        self.turns = 0

    def clear_input(self):
        self.input = ''

    def is_input_valid(self):
        try:
            if 1 > int(self.input) > 9:
                return False
            else:
                return True
        except ValueError:
            return False

    def get_user_input(self, turn):
        if turn == 'x':
            self.input = input(f'{self.playerX}\'s{self.prompt}')
        else:
            self.input = input(f'{self.playerO}\'s{self.prompt}')

    def display_game_interface(self):
        print(f'{self.numbers[0]}|{self.numbers[1]}|{self.numbers[2]}')
        print(self.divider)
        print(f'{self.numbers[3]}|{self.numbers[4]}|{self.numbers[5]}')
        print(self.divider)
        print(f'{self.numbers[6]}|{self.numbers[7]}|{self.numbers[8]}')

    def start_game(self):
        while self.turns < 9:
            turn = 'x' if self.turns % 2 == 0 else 'o'

            self.display_game_interface()
            self.get_user_input(turn)

            if self.is_input_valid():
                i = int(self.input)
                self.numbers[i - 1] = turn
                self.turns = self.turns + 1
            else:
                print(f'value {self.input} is not valid, try again')


if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()
