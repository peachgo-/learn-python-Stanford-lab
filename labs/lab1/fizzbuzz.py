#!/usr/bin/env/ python -3 tt

# find all numbers |3 or | 5 under 41, and calculate the sum.

## Iterative apporoach in one line
def fizzbuzz_2(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

## more pythonic way
def fizzbuzz_3(n):
    return sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, range(n)))

## using generator
def fizzbuzz(n):
    '''
    Return a  generator that generates all multiples of 3 or 5 below n

    '''
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            yield i

if __name__ == '__main__':
    up_bound = int(input("Please enter a upper limit for FizzBuzz: "))
    sum_of_multiples = sum(i for i in fizzbuzz(up_bound))
    print(sum_of_multiples)



