#!/usr/bin/env python -3 tt

def is_palindrome(s):
    if not s or len(s) <= 1:
        return True

    reversed_word = s[::-1]
    if s != reversed_word:
        return False
    else:
        return True

def is_palindrome_recursive(s):
    if not s or len(s) <= 1:
        return True

    s = s.replace(' ', '')

    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome_recursive(s[1:-1])

        

if __name__ == "__main__":
    word = input("Please enter a word: ")
    if is_palindrome_recursive(word):
        print("Yay, you just entered a palindrome!!!")
    else:
        print("Oops, It is not a palindrome!")
