# Hint Giver
# reads a template from a user and validates it
# optional for user to input extra letters to narrow down their hints
# provides the words from the dictionary that abide by this template and the letters entered
# also gives letter stats for the entire word dictionary to aid in user guessing

# Author: Megan Sorenson

from Wordle175 import ScrabbleDict


def main():
    '''
    Main function of the hint giver that take user inputs and evaluates them
    Using user-defined functions
    Inputs: None
    Returns: None
    '''
    # initial conditions
    word_size = 5
    word_dict = ScrabbleDict(5, 'scrabble5.txt')
    template_valid = False
    letters_valid = False

    # ask user to input template until they enter a valid one
    while not template_valid:
        template = input('Please enter a template of {word_size} characters (ex: T***R): '.format(
            word_size=word_size)).lower()
        template_valid = check_template_validity(template, word_size)
    # ask user to input additional letters until they enter a valid entry
    while not letters_valid:
        letters = get_letters()
        letters_valid = check_letter_validity(letters, template)
    # display appropriate hints
    display_hints(template, letters, word_dict)

    # get and display stats for all of the word in the dictionary
    letter_stats = get_dict_stats(word_dict)
    display_stats(letter_stats)


def check_template_validity(template, word_size):
    '''
    Checks if a template is valid based on length and characters
    Inputs: template (str) rep. a user inputted template of letters and asterisks and
    word_size (int) rep. the required length of the template
    Returns: True is the template is valid, otherwise False (bool)
    '''
    if len(template) == word_size:
        for letter in template:
            if not letter.isalpha() and letter != '*':
                print('Invalid characters in template.')
                return False
    else:
        print('Invalid length of template.')
        return False

    return True


def get_letters():
    '''
    Gets user input on additional letters
    Inputs: None
    Returns: a list of letters
    '''
    letters = input(
        'Please enter any additional letters (optional, ex: abc): ')
    letters = list(letters.strip())
    for i in range(len(letters)):
        letters[i] = letters[i].lower()
    return letters


def check_letter_validity(letters, template):
    '''
    Checks if letters are valid based on characters and number of letters
    Inputs: letters (list) containing letters from a user input and
    and template (str) rep. a user inputted template of letters and asterisks
    Returns: True is the letters are valid, otherwise False (bool)
    '''
    # check if no user input
    if len(letters) == 0:
        return True

    for letter in letters:
        # check if only one letter was inputted per comma separation
        if len(letter) != 1:
            print('Invalid multiple letter inputs.')
            return False
        # check if all letter inputs
        if not letter.isalpha():
            print('Invalid non letter inputs.')
            return False
        # check if the right length of letters based on widcards in template
        if len(letters) > list(template).count('*'):
            print('Inalid length of letters. Only {max} allowed.'.format(
                max=list(template).count('*')))
            return False
    return True


def display_hints(template, letters, word_dict):
    '''
    Displays hints based on user input and a word dictionary
    Inputs: template (str) rep. a word of letters and asterisks and
    leters (list) containing additional letters that could be the asterisks of template and
    word_dict (ScrabbleDict) rep. a word dictionary
    Returns: None
    '''
    # get constrained words if there were letter inputs
    # otherwise just get masked words
    if len(letters) == 0:
        hints = word_dict.getMaskedWords(template)

    else:
        hints = word_dict.getConstrainedWords(template, letters)

    print('\nHints:')
    for hint in hints:
        print(hint)


def get_dict_stats(word_dict):
    '''
    Traverses the list of words in a dictionary and counts the appearance of each letter
    Inputs: word_dict (ScrabbleDict) rep. a word dictionary
    Returns: a dictionary of letter:count rep. stats for all words in word_dict
    '''
    # create initial empty dictionary with a key for each letter in the alphabet
    letter_stats = create_letter_dict()

    # for each letter in the alphabet, get the words from the dictionary and add to the letter_stats dictionary
    for letter in letter_stats.keys():
        words = word_dict.getWords(letter)
        get_letter_stats(words, letter_stats)

    return letter_stats


def create_letter_dict():
    '''
    Creates a dictionary with keys being the letters of the alphabet and values are all the int 0
    Inputs: None
    Returns: the dictionary described
    '''
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letter_dict = {}
    # fill dictionary
    for letter in alphabet:
        letter_dict[letter] = 0

    return letter_dict


def get_letter_stats(words, letter_dict):
    '''
    Tallies the appearance of each letter of the alphabet for all the words in a dictionary
    Inputs: words (list) containing words all starting with the same letter and
    letter_dict (dict) of letter:count rep. the to-be updated occurrence stats
    Returns: None
    '''

    # iterate through words, then iterate through letters of each word
    # update dictionary accordingly
    for word in words:
        for letter in list(word):
            letter = letter.upper()
            letter_dict[letter] += 1


def display_stats(letter_stats):
    '''
    Displays letter stats using a dictionary and a symbolic histogram
    Inputs: letter_stats (dict) of letter:key rep. the stats for each letter of the alphabet
    Returns: None
    '''
    # denominator for stats
    total_sum = sum(letter_stats.values())
    # display stats for each letter
    print('\nStats:')
    for letter, count in letter_stats.items():
        percent = count / total_sum * 100
        rounded_percent = round(percent)
        histogram = '*' * rounded_percent
        print('{letter}:{count:>5}{percent:>7.2f}%  {histogram:<}'.format(
            letter=letter, count=count, percent=percent, histogram=histogram))


main()
