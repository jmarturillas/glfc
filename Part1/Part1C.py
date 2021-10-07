

"""
Problem : You are given a word. Now using your favorite programming language, write a code to test if the word that is
given to you is a palindrome.
"""


def is_palindrome(value):
    # A palindrome is a word with the same reading even when reversed.
    # Now, we reverse the given value and check if the value is the same as prior to reversing.

    word = value[::-1]

    if word == value:
        return f"{value} : is a palindrome"
    else:
        return f"{value} : is not a palindrome"


if __name__ == '__main__':
    print(is_palindrome("civic"))
    print(is_palindrome("daddy"))
