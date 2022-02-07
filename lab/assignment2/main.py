# Wordle175 Game
# asks user to guess a word of a certain length
# gives feedback on which letters are correct
# user has 6 guesses to correctly input the word from a word dictionary
# otherwise, game over

# Author: Megan Sorenson

# import ScrabbleDict class from Task 2
from Wordle175 import ScrabbleDict
import random


def main():
    '''
    Main function of the wordle game that asks for user input, gives feedback, and checks the win conditions
    Using user-defined functions
    Inputs: None
    Returns: None
    '''
    # intial conditions
    attempt = 1
    attempted_words = []
    win = False
    word_size = 5
    word_dict = ScrabbleDict(word_size, 'scrabble5.txt')
    # CHANGE THIS LATER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    target_word = 'TIMER'.upper()
    feedback = []

    # play wordle until the user is out of attempts or has guessed the word
    while attempt <= 6 and not win:
        # prompt user to attempt a word guess until it is valid
        word_attempt = get_valid_guess(attempt, attempted_words, word_dict)
        # compare word_attempt to target_word and display appropriate feedback
        give_feedback(word_attempt, target_word, feedback)
        # check win
        win = is_win(word_attempt, target_word)
        if not win:
            # update conditions if game not over
            attempt += 1
            attempted_words.append(word_attempt)

    display_result(target_word, attempt, win)


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
            number=attempt, size=word_dict.getWordSize())).upper()
        # check if valid
        if check_length(word_attempt, word_dict):
            if check_existence(word_attempt, word_dict):
                if check_not_guessed(word_attempt, attempted_words):
                    valid = True

    return word_attempt


def check_length(word, word_dict):
    '''
    Checks if a word attempt is of the right length based on a word dictionary
    Prints error message is word is not the right length
    Inputs: word (str) rep. a user word guess and word_dict (dict) rep. a dictionary of valid words
    Returns: True if the word is the right length, otherwise False (bool)
    '''
    if len(word) == word_dict.getWordSize():
        return True
    elif len(word) > word_dict.getWordSize():
        print('{word} is too long'.format(word=word))
        return False
    else:
        print('{word} is too short'.format(word=word))
        return False


def check_existence(word, word_dict):
    '''
    Checks if a word attempt exists in a given word dictionary
    Prints error message is word does not exist
    Inputs: word (str) rep. a user word guess and word_dict (dict) rep. a dictionary of valid words
    Returns: True if the word exists, otherwise False (bool)
    '''
    if word_dict.check(word.lower()):
        return True
    else:
        print('{word} is not a recognized word'.format(word=word))
        return False


def check_not_guessed(word, attempted_words):
    '''
    Checks if a word attempt has already been guessed or not
    Prints error message is word has already been guessed
    Inputs: word (str) rep. a user word guess and attempted_words (list) rep. list of already guessed words and
    Returns: True if the word has not been guessed, otherwise False (bool)
    '''
    if word not in attempted_words:
        return True
    else:
        print('{word} was already entered'.format(word=word))


def give_feedback(attempt_word, target_word, previous_feedback):
    '''
    Evaluates and displays feeedback about letters in a user guess
    Based on the letetr and it's position in the word
    Inputs: attempt_word (str) rep. a word that feedback is given for and
    target_word (str) rep. the word used to give feedbck about attempt_word and
    previosu feedback (list) rep. all the hitorical feedback given for previosu user attempts
    '''
    # initial empty feedback dictionary with 3 categories
    new_feedback = {'Green': [], 'Orange': [], 'Red': []}

    # numerically label letters with multiple occurrences
    word = label_letters(attempt_word)
    # split target word into list
    target = list(target_word)

    # for each feedback category, find the correpsonding letters from the word by comparing it to the target
    for category in new_feedback.keys():
        # categorize letters into the right category
        categorized_letters = categorize_letters(
            word, target, category)
        # add sorted categorized letters to dictionary value
        categorized_letters.sort()
        new_feedback[category] = categorized_letters

    # update feedback history
    update_feedback(attempt_word, previous_feedback, new_feedback)
    # display feedback to user
    display_feedback(previous_feedback)


def label_letters(word_attempt):
    '''
    Checks if a letter occurs more than once in a word and numerically labels it if so
    Inputs: word_attempt (str) rep. the word whose letetrs are being labeled
    Returns: a list representing containing the labeled letters of word
    '''
    # split word into list of letters
    word = list(word_attempt)
    # if letters occur more than once, label numerically in order
    for letter in word:
        if word.count(letter) > 1:
            label = 1
            for i in range(word.count(letter)):
                index = word.index(letter)
                word[index] = letter + str(label)
                label += 1

    return word


def categorize_letters(word, target, category):
    '''
    Evaluates which category a letter should be in based on its letter and position
    Inputs: word (list) containing letters being categorized and
    target (list) containing letters used to categorize the word letters and
    category (str) rep. which category we are avaluating the letters for
    Returns: a list containing the categorized letetrs for the specified category
    '''
    categorized_letters = []
    # iterate over letters and categorize the letters that are into the right spot
    for i in range(len(word)):
        # word[i][0] accounts for numerically labeled letters
        letter = word[i][0]
        if letter != ' ':
            if category == 'Green' and letter == target[i]:
                categorized_letters.append(word[i])
                word[i] = ' '
                target[i] = ''
            elif category == 'Orange' and letter in target:
                categorized_letters.append(word[i])
                word[i] = ' '
                target.remove(letter)
            elif category == 'Red':
                # add the remaining letters in the word list
                categorized_letters.append(word[i])
    return categorized_letters


def update_feedback(word, previous_feedback, new_feedback):
    '''
    Formats and updates feedback for the user's word attempts
    Inputs: word (str) representing the last word attempt by the user and
    previous_feedback (list) containing the histroical formatted feedback for previous word attempts and
    new_feedback (dict) of category:letters rep. the non-formatted feedback for word
    Returns: None
    '''
    # initial strings
    feedback_string = '{word} '.format(word=word)
    category_strings = []
    # format strings for each category and append to list of category strings
    for category, feedback in new_feedback.items():
        category_strings.append('{category}={{{letters}}}'.format(
            category=category, letters=', '.join(feedback)))
    # concatenate category trings to feedback string
    feedback_string += ' - '.join(category_strings)

    # append new feedback to previous feedback
    previous_feedback.append(feedback_string)


def display_feedback(previous_feedback):
    '''
    Displays all the feedback for the user's word attempts
    Inputs: previous_feedback (list) containing all the historical formatted feedback for the user's word attempts
    Returns: None
    '''
    for feedback in previous_feedback:
        print(feedback)


def is_win(word, target):
    '''
    Checks if the user has won the game by guessing the correct word
    Inputs: word (str) rep. the last word attempt and target (str) rep. the word that shoudl be guessed
    Returns: True if the user won by guessing the target word, otherwise False (bool)
    '''
    if word == target:
        return True
    else:
        return False


def display_result(target, attempt, win):
    '''
    Displays the results at the end of the game base on the win condition
    Inputs: target (str) rep. the word that needed to be guessed to win and
    attempt (int) rep. the turn that the player is on and
    win (bool) rep. whether the user won or not
    Returns: None
    '''
    if win:
        print('Found in {attempt} attempts. Well done.'.format(
            attempt=attempt), end=' ')
    else:
        print('Sorry you lose.', end=' ')
    print('The Word is {word}.'.format(word=target))


main()
