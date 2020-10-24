class PositionError(Exception):
    pass


class IncorrectInput(Exception):
    pass


class TicTacGame:
    NUMBER_OF_CELLS = 9
    SEPARATOR = '---+---+---'

    def __init__(self):
        self.cells = [' '] * self.NUMBER_OF_CELLS
        self.winning_positions = [[0, 1, 2], [3, 4, 5],
                                  [6, 7, 8], [0, 3, 6],
                                  [1, 4, 7], [2, 5, 8],
                                  [0, 4, 8], [2, 4, 6]
                                  ]
        self.current_player = 'X'
        self.winner = ''

    def show_board(self):
        line_1 = ' {} | {} | {} '.format(*self.cells[0:3])
        line_2 = ' {} | {} | {} '.format(*self.cells[3:6])
        line_3 = ' {} | {} | {} '.format(*self.cells[6:9])

        print(line_1)
        print(self.SEPARATOR)
        print(line_2)
        print(self.SEPARATOR)
        print(line_3)
        print()

    def validate_input_start(self):
        """считывает и проверяет ввод, который перед партией"""
        inp = input()
        if inp in ('start', 'quit'):
            return inp
        else:
            raise IncorrectInput()

    def validate_input_game(self):
        """считывает и проверяет ввод, который происходит во время партии"""
        inp = int(input())  # raise ValueError

        actual_position = inp - 1

        if actual_position not in range(self.NUMBER_OF_CELLS):
            raise IndexError

        if self.cells[actual_position] != ' ':
            raise PositionError()

        return inp

    def introduction(self):
        """запускает игру и проверяет на выход"""
        print('Hello! It is a TicTacToe Game.\n'
              'If you would like to play this game, please, enter "start"\n'
              'Or if you would like to quit - enter "quit"\n')

        while True:
            if self.start_game() == 'quit':
                break

    def start_game(self):
        """возвращает "quit", если выходишь"""
        self.__init__()

        while True:
            try:
                inp = self.validate_input_start()
                break
            except IncorrectInput:
                print('Please, enter "start" or "quit"\n')

        if inp == 'quit':
            return inp
        if inp == 'start':
            self.start_round()

        print('If you would like to play again, please, enter "start" again')

    def start_round(self):
        res = 'continue'
        while res == 'continue':
            self.show_board()
            print('{} next move'.format(self.current_player))
            self.move()
            self.change_player()
            res = self.win_status()

        self.print_results(res)

    def print_results(self, res):
        """выводит результаты игры в читаемой форме"""
        self.show_board()
        if res == 'winner':
            print('{} win a game!\n'.format(self.winner))
        elif res == 'draw':
            print('A draw!\n')

    def move(self):
        """считывает из ввода и делает ход текущим игроком"""
        while True:
            try:
                pos = self.validate_input_game()
                break
            except ValueError:
                print('Please, type a number from 1 to 9, not a string or a float number\n')
            except PositionError:
                print('This cell is not free. Please, choose another position\n')
            except IndexError:
                print('Please, type a number from 1 to 9\n')

        self.make_move(pos - 1)

    def make_move(self, position):
        """делает ход в указанную позицию текущим игроком"""
        self.cells[position] = self.current_player

    def change_player(self):
        """меняет текущего игрока"""
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def win_status(self):
        for position in self.winning_positions:
            if self.cells[position[0]] == \
               self.cells[position[1]] == \
               self.cells[position[2]] \
           and self.cells[position[0]] != ' ':
                self.winner = self.cells[position[0]]
                return 'winner'

        if ' ' not in self.cells:
            return 'draw'

        return 'continue'

