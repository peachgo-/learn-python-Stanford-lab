#!/usr/bin/env python -3 tt

# using `\` at the end of one line in a multiline string removes the implicit
# newline

tictac = """\
  |  |
--------
  |  |
--------
  |  |  \
"""

def tictac2():
    row = '|'.join(['  '] * 3)
    div = '\n{}\n'.format('-' * 8)
    print(row, row, row, sep=div)

if __name__ == "__main__":
    print("Using string literal\n")
    print(tictac)
    print("Using list mult, string mult, and .join module")
    tictac2()

