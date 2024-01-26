"""
CSE212 
(c) BYU-Idaho
05-Teach - Problem 1 

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

from typing import Text


def unique_letters(text):
    """ 
    Determine if there are any duplicate letters in the text provided
    for O(n) add every letter into a set. and if the letter is in the set already then something is wrong
    """
    text2 = set()

    for i in text:
        if i not in text2:
            text2.add(i)
        else:
            return False
        


    return True

test1 = "abcdefghjiklmnopqrstuvwxyz"  # Expect True because all letters unique
print(unique_letters(test1))

test2 = "abcdefghjiklanopqrstuvwxyz"  # Expect False because 'a' is repeated
print(unique_letters(test2))

test3 = "" 
print(unique_letters(test3))          # Expect True because its an empty string