__all__ = ['TicTacToe']


class TicTacToe:
    def __init__(self):
        self._board = [None for _ in range(9)]
        self._o_turn = True

    def _index(self, x, y):
        return (y * 3) + x

    @property
    def board(self):
        return list(self._board)

    @property
    def winner(self):
        return self._check_winner()

    @property
    def turn(self):
        return 'O' if self._o_turn else 'X'

    def _check_winner(self):
        sequences = [
            ((0,0), (1,1), (2,2)),
            ((0,2), (1,1), (2,0)),
        ]
        rows = [tuple((x,y) for x in range(3)) for y in range(3)]
        columns = [tuple((x,y) for y in range(3)) for x in range(3)]

        sequences.extend(rows)
        sequences.extend(columns)

        winners = [self._check_seq(s) for s in sequences]
        for w in winners:
            if w is not None:
                return w
        else:
            return None

    def _check_seq(self, seq):
        if len(seq) < 3:
            return None

        values = [self._board[self._index(*s)] for s in seq]

        if values[0] is None:
            return None
        if values[::1] != values[::-1]:
            return None
        if values != [values[0] for _ in range(3)]:
            return None

        return values[0]

    def play_point(self, x, y=None):
        if y is None:
            index = x
        else:
            index = self._index(x, y)

        if self._board[index] is not None:
            raise ValueError(f'Cannot play on point that has already been claimed by {self._board[index]}')

        if self._o_turn:
            self._board[index] = 'O'
        else:
            self._board[index] = 'X'

        self._o_turn = not self._o_turn

    def clear(self):
        self._board = [None for _ in range(9)]
        self._o_turn = True


def test_tic_tac_toe():
    test_model = TicTacToe()

    assert test_model.winner is None

    test_model.play_point(1, 1)
    test_model.play_point(0, 1)
    test_model.play_point(0, 0)
    test_model.play_point(1, 0)
    test_model.play_point(2, 2)
    assert test_model.winner == 'O'

    test_model.clear()
    assert test_model.board == [None for _ in range(9)]

    test_model.play_point(1,0)
    test_model.play_point(0,0)
    test_model.play_point(1,1)
    test_model.play_point(0,1)
    test_model.play_point(1,2)
    assert test_model.winner == 'O'

    test_model.clear()

    test_model.play_point(1)
    test_model.play_point(0)
    test_model.play_point(2)
    test_model.play_point(4)
    test_model.play_point(6)
    test_model.play_point(8)
    assert test_model.winner == 'X'
