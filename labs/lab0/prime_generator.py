#!/usr/bin/env python -3 tt

def is_palindrome(s):

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    bound = input("Enter a number as upper limit: ")
    for n in range(2, int(bound)):
        if is_prime(n):
            print(n, " is prime")
        else:
            print(n, " is not prime")
