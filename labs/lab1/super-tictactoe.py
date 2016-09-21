#!/usr/bin/env/ python -3 tt

""" Write a program that, when run, prints out a SUPER tic-tac-toe board.

  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
========+========+========
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
========+========+========
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
--+--+--H--+--+--H--+--+--
  |  |  H  |  |  H  |  |  
"""

TICTACTOE_LINES = [
"  |  |  ",
"--+--+--",
"  |  |  ",
"--+--+--",
"  |  |  ",
] 

TEMP_ROW = "  |  |  "
HORIZONTAL_SEP = "========"
VERT_SEP = 'H'
board_rows = []
BOARD_SIZE = 3


row_sep = "+".join([HORIZONTAL_SEP]*3) + "\n"

if __name__ == "__main__":
    for _ in range(BOARD_SIZE):
        row = ''
        for line in TICTACTOE_LINES:
             row += VERT_SEP.join([line] * BOARD_SIZE) + "\n"
        board_rows.append(row)
    board = row_sep.join(board_rows)
print(board)
