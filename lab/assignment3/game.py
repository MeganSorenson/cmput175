from abacko_stack_class import AbackoStack
from bounded_stack import BStack
from card_class import Card

# user-defined functions


def get_game_specs():
    '''
    Asks user to input game specs for the abacko board
    Asks until user inputs valid entry
    Returns a tuple of integers representing number of colours then depth of stacks
    '''
    # get number of colours input until valid entry
    number_of_colours = 0
    while number_of_colours < 2 or number_of_colours > 5:
        number_of_colours = input(
            'Please enter the number of stacks between 2 and 5: ')
        # check if integer entry and don't end program if not
        try:
            number_of_colours = int(number_of_colours)
        except:
            print('Invalid entry: must be an integer')
            number_of_colours = 0

    # get depth of stacks input until valid entry
    depth_of_stacks = 0
    while depth_of_stacks < 2 or depth_of_stacks > 4:
        depth_of_stacks = input(
            'Please enter the depth of stacks between 2 and 4: ')
        # check if integer entry and don't end program if not
        try:
            depth_of_stacks = int(depth_of_stacks)
        except:
            print('Invalid entry: must be an integer')
            depth_of_stacks = 0

    return (number_of_colours, depth_of_stacks)


def get_user_action(abacko, win, continue_game):
    '''
    Gets a user action and changes the board accordingly
    abacko is na object type AbackoStack which represents the game board
    returns a tuple of boolean variable representing win, continue_game
    '''
    action = input(
        'Enter your move(s) (separated by spaces) [Q for quit and R to reset]:')
    # reset or quit if  user asks
    if action.upper() == 'R':
        abacko.reset()
    elif action.upper() == 'Q':
        win = True
        continue_game = False
        print('Quit game, goodbye...')
    # otherwise, collect actions
    # for each action, check if there has already been an error in the sequenc of actions
    #   (no more actions of that sequence will then be run)
    # if no error in the sequence has happened, continue to move the beads according to the user input
    else:
        actions = action.split(' ')
        error = False
        for action in actions:
            if not error:
                try:
                    abacko.moveBead(action)
                except:
                    print('Invalid move')
                    error = True

    return (win, continue_game)


def check_win(abacko, card, win, continue_game):
    '''
    Checks for game win and chnages game variables accordingly
    Also asks if user wants to play again if they won
    abacko is an object type AbackoStack that represents the game board
    card is an object type Card that represents the winning configuration for the abacko board
    returns a tuple representing game variables of win, continue_game (bool)
    '''
    if abacko.isSolved(card) and not win:
        print('Congratulations! Well done.')

        ask_play_again = True
        while ask_play_again:
            play_again = input('Would you like another game? [Y/N]: ')
            if play_again.upper() == 'N':
                continue_game = False  # ends game loop
                ask_play_again = False
            elif play_again.upper() != 'Y':
                print('Invalid input:', play_again)
                print()
            else:
                ask_play_again = False

            win = True  # ends action loop

    return (win, continue_game)

# main function


def main():
    '''
    Main function of the program that runs the AbackoStack game
    '''
    # initial game variables
    continue_game = True
    win = False
    # game loop for the game
    while continue_game:
        # get user input for their desired game size
        # first item is number of colours, second is depth of stacks
        specs = get_game_specs()

        # generate card and abackostack
        card = Card(specs[0], specs[1])
        abacko = AbackoStack(specs[0], specs[1])
        # show initial abacko with card
        abacko.show(card)
        print()

        # action loop for the game
        # get user input for actions and act accordingly
        # continue to do so until player wins or decides to quit
        while not win:
            # get user input for action(s) and respond accordingly
            # game_variables is a tuple of win, continue_game
            game_variables = get_user_action(abacko, win, continue_game)
            win = game_variables[0]
            continue_game = game_variables[1]

            # display game state
            if continue_game:
                abacko.show(card)
                print()

            # check if game is won and ask to play again
            # game_variables is a tuple of win, continue_game
            game_variables = check_win(abacko, card, win, continue_game)
            win = game_variables[0]
            continue_game = game_variables[1]


main()
