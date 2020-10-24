import io
import re
from random import shuffle
from unittest import TestCase
from unittest.mock import patch
from unittest import main

import TicTacToe

CELLS = TicTacToe.TicTacGame.NUMBER_OF_CELLS


class TicTacToeTest(TestCase):

    def setUp(self):
        self.game = TicTacToe.TicTacGame()

    @staticmethod
    def str_to_cells(s, replace=False):
        if replace:
            s = s.replace('X', 'T')
            s = s.replace('O', 'X')
            s = s.replace('T', 'O')
        assert len(s) == CELLS
        return [c for c in s]


class SwitchUserTestCase(TicTacToeTest):
    """смена пользователя"""
    def test_x_to_o(self):
        self.assertEqual(self.game.current_player, 'X')
        self.game.change_player()
        self.assertEqual(self.game.current_player, 'O')

    def test_o_to_x(self):
        self.game.change_player()
        self.assertEqual(self.game.current_player, 'O')
        self.game.change_player()
        self.assertEqual(self.game.current_player, 'X')


class MovesGameTest(TicTacToeTest):
    """как бы интеграционные тесты"""

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('TicTacToe.input', create=True)
    def test_start(self, mocked_input, mocked_output):
        mocked_input.side_effect = ['ffdsa', '', 'quit']
        self.game.introduction()
        regexp = re.compile(r'''.*Hello!.*Please.*Please.*''',
                            re.DOTALL)
        self.assertRegex(mocked_output.getvalue(), regexp)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('TicTacToe.input', create=True)
    def test_end_draw(self, mocked_input, mocked_output):
        """тест, проверяющий корректность завершения игры вничью"""
        mocked_input.side_effect = ['start', '1', '5', '2', '3', '7',
                                    '4', '6', '8', '9', 'quit']
        self.game.introduction()
        regexp = re.compile(r'''.*Hello(.*next move){8}.*A draw!.*enter.*''',
                            re.DOTALL)
        self.assertRegex(mocked_output.getvalue(), regexp)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('TicTacToe.input', create=True)
    def test_end_win_x(self, mocked_input, mocked_output):
        """выигрыш X"""
        mocked_input.side_effect = ['start', '1', '2', '5', '3', '9', 'quit']
        self.game.introduction()
        regexp = re.compile(r'''.*Hello(.*next move){4}.*X win a game!.*''',
                            re.DOTALL)
        self.assertRegex(mocked_output.getvalue(), regexp)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('TicTacToe.input', create=True)
    def test_end_win_o(self, mocked_input, mocked_output):
        """выигрыш O"""
        mocked_input.side_effect = ['start', '7', '1', '2', '5', '3', '9', 'quit']
        self.game.introduction()
        regexp = re.compile(r'''.*Hello(.*next move){5}.*O win a game!.*''',
                            re.DOTALL)
        self.assertRegex(mocked_output.getvalue(), regexp)


class ValidationInputTest(TicTacToeTest):
    """тесты validate_input_start"""
    @patch('TicTacToe.input', create=True)
    def test_input_start_incorrect(self, mocked_input):
        mocked_input.side_effect = ['fdashjk', '1', '0', '-1', '', '100']
        for _ in range(6):
            with self.assertRaises(TicTacToe.IncorrectInput):
                self.game.validate_input_start()

    @patch('TicTacToe.input', create=True)
    def test_input_start_correct_start(self, mocked_input):
        mocked_input.side_effect = ['start', 'start']
        for _ in range(2):
            self.assertEqual(self.game.validate_input_start(), 'start')

    @patch('TicTacToe.input', create=True)
    def test_input_start_correct_quit(self, mocked_input):
        mocked_input.side_effect = ['quit', 'quit']
        for _ in range(2):
            self.assertEqual(self.game.validate_input_start(), 'quit')

    @patch('TicTacToe.input', create=True)
    def test_input_start_random(self, mocked_input):
        mocked_input.side_effect = ['quit', 'bla', 'start', 'jkl;', 'quit']

        self.assertEqual(self.game.validate_input_start(), 'quit')

        with self.assertRaises(TicTacToe.IncorrectInput):
            self.game.validate_input_start()

        self.assertEqual(self.game.validate_input_start(), 'start')

        with self.assertRaises(TicTacToe.IncorrectInput):
            self.game.validate_input_start()

        self.assertEqual(self.game.validate_input_start(), 'quit')


class ValidationInputGame(TicTacToeTest):
    """тесты validate_input_game на пустом поле"""

    @patch('TicTacToe.input', create=True)
    def test_input_raises(self, mocked_input):
        lst = ['f1', '1e10', '32.14', '-', '1+2', '10-3', '5-1']
        mocked_input.side_effect = lst
        for _ in range(len(lst)):
            with self.assertRaises(ValueError):
                self.game.validate_input_game()

    @patch('TicTacToe.input', create=True)
    def test_input_raises_big(self, mocked_input):
        lst = [str(i) for i in range(CELLS + 1, 1000)]
        mocked_input.side_effect = lst

        for _ in range(len(lst)):
            with self.assertRaises(IndexError):
                self.game.validate_input_game()

    @patch('TicTacToe.input', create=True)
    def test_input_raises_negative(self, mocked_input):
        lst = [str(i) for i in range(0, -1000, -1)]
        mocked_input.side_effect = lst

        for _ in range(len(lst)):
            with self.assertRaises(IndexError):
                self.game.validate_input_game()

    @patch('TicTacToe.input', create=True)
    def test_input_ok(self, mocked_input):
        lst = [str(i) for i in range(1, CELLS + 1)]
        shuffle(lst)
        mocked_input.side_effect = lst

        for i in range(CELLS):
            self.assertEqual(self.game.validate_input_game(), int(lst[i]))


class ValidationInputNotEmptyTest(TicTacToeTest):
    """проверка, как парсится позиция знака на непустом поле"""
    def setUp(self):
        super().setUp()
        self.game.cells = [' '] * CELLS
        self.game.cells[1] = \
        self.game.cells[2] = \
        self.game.cells[5] = 'X'

        self.game.cells[4] = \
        self.game.cells[7] = \
        self.game.cells[8] = 'O'

    @patch('TicTacToe.input', create=True)
    def test_input_ok(self, mocked_input):
        """когда они могут поставиться"""
        mocked_input.side_effect = lst = ['1', '7', '4'] * 2
        for player in range(2):
            for i in range(len(lst) // 2):
                self.assertEqual(self.game.validate_input_game(), int(lst[i]))

            self.game.change_player()

    @patch('TicTacToe.input', create=True)
    def test_input_not_ok(self, mocked_input):
        """когда не могут поставиться"""
        mocked_input.side_effect = lst = ['2', '3', '5', '6', '8', '9'] * 2
        for player in range(2):
            for _ in range(len(lst) // 2):
                with self.assertRaises(TicTacToe.PositionError):
                    self.game.validate_input_game()


class WinTests(TicTacToeTest):
    """проверки функций, проверяющих состояние игры, выиграно или нет"""
    def test_continue(self):
        self.game.cells = [' '] * CELLS
        self.assertEqual(self.game.win_status(), 'continue')

        self.game.cells[1] = \
        self.game.cells[2] = \
        self.game.cells[5] = 'X'

        self.game.cells[4] = \
        self.game.cells[7] = \
        self.game.cells[8] = 'O'
        self.assertEqual(self.game.win_status(), 'continue')

        self.game.cells = [' '] * CELLS
        self.assertEqual(self.game.win_status(), 'continue')

        for i in range(CELLS):
            for player in ['X', 'O']:
                self.game.cells = [' '] * CELLS
                self.game.cells[i] = player
                self.assertEqual(self.game.win_status(), 'continue')

        self.game.cells = ['X', 'O', 'O',
                           'X', ' ', 'O',
                           'O', 'X', 'X']
        self.assertEqual(self.game.win_status(), 'continue')

        self.game.cells = ['X', 'X', ' ',
                           ' ', ' ', ' ',
                           ' ', ' ', ' ']
        self.assertEqual(self.game.win_status(), 'continue')

    def test_win(self):
        """проверка корректности выигрыша определения выигрыша"""
        def elementary_test(s):
            """запускает тест (на выигрыш) из строки, в двух вариантах
               с выигрывающим Х и инвертированный (с выигрывающим O)"""
            self.game.cells = self.str_to_cells(s)
            self.assertEqual(self.game.win_status(), 'winner')
            self.assertEqual(self.game.winner, 'X')

            self.game.cells = self.str_to_cells(s, True)
            self.assertEqual(self.game.win_status(), 'winner')
            self.assertEqual(self.game.winner, 'O')

        # все возможные линии
        elementary_test('XXX'
                        '   '
                        'OO ')
        elementary_test('   '
                        'XXX'
                        'OO ')
        elementary_test('   '
                        ' OO'
                        'XXX')
        elementary_test('XOO'
                        'X  '
                        'X  ')
        elementary_test('OXO'
                        ' X '
                        ' X ')
        elementary_test('OOX'
                        '  X'
                        '  X')
        elementary_test('X  '
                        ' X '
                        'OOX')
        elementary_test('OOX'
                        ' X '
                        'X  ')

        # более сложные ситуации
        elementary_test('OX '
                        ' OO'
                        'XXX')
        elementary_test('XXX'
                        'OOX'
                        'OOX')
        elementary_test('XOO'
                        'XXO'
                        'XOX')

    def test_draw(self):
        """проверка ничьей"""
        def elementary_test(s):
            self.game.cells = self.str_to_cells(s)
            self.assertEqual(self.game.win_status(), 'draw')

            self.game.cells = self.str_to_cells(s, True)
            self.assertEqual(self.game.win_status(), 'draw')

        elementary_test('OXO'
                        'XXO'
                        'XOX')

        elementary_test('OXO'
                        'OXX'
                        'XOX')

        elementary_test('XOX'
                        'OXX'
                        'OXO')

        elementary_test('OOX'
                        'XXO'
                        'OXX')


if __name__ == '__main__':
    main()
