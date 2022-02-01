# Wordle175 Game

# Author: Megan Sorenson

# import ScrabbleDict class from Task 2
from Wordle175 import ScrabbleDict


def main():
    '''
    '''
    # intial conditions
    attempt = 1
    attempted_words = []
    word_size = 5
    word_dict = ScrabbleDict(word_size, 'scrabble5.txt')

    while attempt <= 6:
        # prompt user to attempt a word guess until it is valid
        word_attempt = get_valid_guess(attempt, attempted_words, word_dict)
        # update conditions
        attempt += 1
        attempted_words.append(word_attempt)


def get_valid_guess(attempt, attempted_words, word_dict):
    '''
    Prompts user to input a word guess
    Checks if guess is valid
    Inputs: attempt (int) rep. the attempt number the user is on and
    attempted_words (list) rep. list of already guessed words and 
    word_dict (dict) whose keys rep. the possible words
    Returns: valid word (str) guess by user
    '''
    # get user input
    valid = False
    while not valid:
        word_attempt = input('Attempt {number}: Please enter a {size} letter word: '.format(
            number=attempt, size=word_dict.getWordSize()))
        # check if valid
        if word_dict.check(word_attempt):
            if len(word_attempt) == word_dict.getWordSize():
                if word_attempt not in attempted_words:
                    valid = True

    return word_attempt


class Game:
    def __init__(self, word_size):
        # intial conditions
        attempt = 1
        attempted_words = []
        word_size = 5
        word_dict = ScrabbleDict(word_size, 'scrabble5.txt')


main()
