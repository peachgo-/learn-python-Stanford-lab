#!/usr/bin/env python -3 tt

# using recursion
def collatz(n):
    """
    Return the collatz sequence starting at `n `.

    a collatz sequence is an iterative sequence defined on the positive
    integers by
        n -> n / 2  if n is even
        n -> 3n + 1 if n is odd

    for example, collatz(13) should yield the following sequence:
        13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

    """
    collatz_seq = [n]
    def collatz_helper(n):
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        collatz_seq.append(n)
        if n != 1: collatz_helper(n)
    collatz_helper(n)
    return collatz_seq

# using iteration
def collatz_len(n):
    """
    Return the length of the Collatz sequence starting at `n`

    """
    length = 1
    while n > 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        length += 1
    return length

def max_chain_len(n):
    """
    Return the length of the longest collatz sequence lenght for numbers below n

    A more pythonic way,
        
    return max(map(collatz_len, range(1, n)))
    """
    return max([len(collatz(n)) for n in range(1, n)])

if __name__ == '__main__':
    starting_num = int(input("Please enter a starting number: "))
    seq_str = [str(num) for num in collatz(starting_num)]
    print( 'The Collatz sequence starting at {} is: '.format(starting_num), 
            '->'.join(seq_str))
    print( 'The longest chain length \
for starting numbers less than {} \
is: '.format(starting_num), 
        max_chain_len(starting_num))



