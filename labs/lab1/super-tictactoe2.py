#!/usr/bin/env python -3 tt

def board(size):
    '''
    Return a n * n board consists of n rows and n columns
    A row is n adjacent standard 3 x 3 tic-tac-tow boards in a row
    n is the given board size
    '''

    line = 'H'.join(['  |  |  '] * size) + '\n'
    line_sep = 'H'.join(['--+--+--'] * size) + '\n'
    row = line_sep.join([line] * 3)

    row_sep = '+'.join(['========'] * size) + '\n'
    board = row_sep.join([row] * size)

    return board

if __name__ == '__main__':
    size = int(input("Please enter the size of your tictactoe board: "))
    print("Here is the {0} * {0} board you asked for".format(size))
    print(board(size))
