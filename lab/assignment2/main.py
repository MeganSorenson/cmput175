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
    target_word = 'TIMER'  # CHANGE THIS LATER !!!!!!!!!!!!!!!!!!!!!!!
    feedback = []

    # get user word attempt
    while attempt <= 6:
        # prompt user to attempt a word guess until it is valid
        word_attempt = get_valid_guess(attempt, attempted_words, word_dict)
        # compare word_attempt to target_word and display appropriate feedback
        give_feedback(word_attempt, target_word, feedback)
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
    if word_dict.check(word):
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


def give_feedback(attempt, target, previous_feedback):
    '''
    Compares the attemted word to the target word
    Displays appropriate new and previous feedback
    Inputs: attempt (str) rep. the word attempt by the user and
    target (str) rep. the answer that attempt is being compared to and
    previous_feedback (list) which contains all the previosuly given feedback
    Returns: None
    '''
    # create empty new feedback dictionary with the three categories
    new_feedback = {'Green': [], 'Orange': [], 'Red': []}

    for i in range(len(target)):
        # get feedback category by comapring attempted letter to target word letters
        feedback_category = get_feedback_category(attempt, target, i)
        # check if the attempt has more than one occurrence of the letter and number letter appropriately
        feedback_letter = deal_with_letter_multiples(
            attempt[i], attempt, new_feedback)
        # add (potentially numbered) letter to appropriate feedback category within new_feedback
        new_feedback[feedback_category].append(feedback_letter)

    # add new feedback to previous feedback
    update_feedback(new_feedback, previous_feedback, attempt)

    display_feedback(previous_feedback)


def get_feedback_category(word, target_word, letter_index):
    '''
    Checks a letter against a target word and determines which feedback category it corresponds to
    Inputs: letter (str) rep. the letter being checked against the target solution and
    word (str) rep. the word containiing letters and
    target_word (str) rep. the entire target word to compare the word to and
    letter_index (int) rep. the index of the letter in word being compared to target_word
    Returns: the category (str) of feedback for the given letter
    '''
    # check if the lettter is in the right place
    if word[letter_index] == target_word[letter_index]:
        category = 'Green'
    # check if the letter is in the target but not in the right place
    elif word[letter_index] in target_word:
        category = 'Orange'
        if letter_multiple(word, word[letter_index]):
            max_occurrences = list(target_word).count(word[letter_index])
            previous_word_letters = list(word[0:letter_index])
            used_occurrences = previous_word_letters.count(word[letter_index])
            if used_occurrences >= max_occurrences:
                category = 'Red'
    # check is the letter is not in the target
    else:
        category = 'Red'

    return category


def deal_with_letter_multiples(letter, word, feedback):
    '''
    Checks if a letter occurs multiple times in a word and if the letter is already in feedback
    Responds by appropriately numbering letters that occur in multiples
    Inputs: letter (str) rep. the letter to be checked within the word and
    word (str) rep. the word with letters and 
    feedback (dict) rep. a dictionary of feedback whose values are being checked
    Returns: the letter (str) that should be added to the new feedback
    '''
    # check if the attempt has more than once occurrence of the letter
    # if yes, number the letter and add to the appropriate feedback
    # otherwise, just add the letter to the appropriatefeedback
    if not letter_multiple(word, letter):
        return letter
    elif not in_feedback(letter, feedback):
        return letter + '1'
    else:
        return letter + '2'


def letter_multiple(word, letter):
    '''
    Checks if there are more than one instance of a letter in a word
    Inputs: word (str) rep. the word with letters and letter (str) rep. the letter to be checked within the word
    Returns: True if there are multiples, otherwise Falkse (bool)
    '''
    word_letters = list(word)
    if word_letters.count(letter) == 1:
        return False
    else:
        return True


def in_feedback(letter, feedback):
    '''
    Checks if a letter is already in the feedback
    Inputs: letter (str) rep. the letter being searched for in the feedback and 
    feedback (dict) rep. a dictionary of feedback whose values are being checked
    Returns: True if the letter is already in the feedback, otherwise False
    '''
    in_feedback = False
    for feedback_list in feedback.values():
        for feedback_letter in feedback_list:
            if feedback_letter[0] == letter:
                in_feedback = True

    return in_feedback


def update_feedback(new_feedback, previous_feedback, word_attempt):
    '''
    Adds the new feedback to the previosu feedback as a formatted string
    Inputs: new_feedback (dict) rep. the category: letter feedback list that is new and
    previous_feedback (list) rep. all the formatted and previously given feedback given to the user and
    word_attempt (str) rep. the word that was given feedback for
    Returns: None
    '''
    # intial feedback with word attempt
    new_feedback_string = '{word} '.format(word=word_attempt)

    # concatenate the all the catgeories' feedback to the feedback string
    new_feedback_string += formatted_feedback(new_feedback)

    # append the new feedbck to the previous feedback list
    previous_feedback.append(new_feedback_string)


def formatted_feedback(new_feedback):
    '''
    String formats feedback using dictionary items
    Inputs: new_feedback (dict) rep. category:feedback for a word
    Returns: a formatted string of all  the feedback
    '''
    # initial empty feedback list
    all_new_feedback = []

    # for each item in the feedback dictionary, format the contents and add to all_new_feedback list
    for category, feedback in new_feedback.items():
        # aplhabeticize feedback
        feedback.sort()
        # format feedback
        formatted_feedback = '{category}={{{letters}}}'.format(
            category=category, letters=', '.join(feedback))
        all_new_feedback.append(formatted_feedback)

    # join all the category string together
    feedback_string = ' - '.join(all_new_feedback)

    return feedback_string


def display_feedback(feedback_list):
    '''
    Displays the feedback for any particular point in the wordle game
    Inputs: feedback_list (list) rep. strings of all the given feedback to date
    Returns: None
    '''

    for feedback in feedback_list:
        print(feedback)


main()
