# 24. Write a Python program to test whether a passed letter is a vowel or not.

vowels = ['a','e','i','o','u']

def check(letter):
    for vowel in vowels:
        if letter == vowel:
            return True
    return False

def test_vowel():
    assert check('a')

def test_not_vowel():
    assert not check('b')

