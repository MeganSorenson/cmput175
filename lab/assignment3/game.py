from abacko_stack_class import AbackoStack
from bounded_stack import BStack
from card_class import Card


def main():
    '''
    Main function of the program that runs the AbackoStack game
    '''
    continue_game = True
    # game loop for the game
    while continue_game:
        # get user input for their desired game size
        # assumes that user inputs an integer
        number_of_colours = 0
        while number_of_colours < 2 or number_of_colours > 5:
            number_of_colours = int(input(
                'Please enter your desired number of colours for the game (2-5) !must be integer! > '))
        depth_of_stacks = 0
        while depth_of_stacks < 2 or depth_of_stacks > 4:
            depth_of_stacks = int(input(
                'Please enter your desired depth of stack for the game (2-4) !must be integer! >'))

        # generate card and abackostack
        card = Card(number_of_colours, depth_of_stacks)
        abacko = AbackoStack(number_of_colours, depth_of_stacks)

        end_game = False
        abacko.show(card)
        # action loop for the game
        # get user input for actions and act accordingly
        # continue to do so until player wins or decides to quit
        while not end_game:
            # get user input for action(s)
            action = input(
                'Enter your move(s) (separated by spaces) [Q for quit and R to reset] >')
            # reset or quit if  user asks
            if action.upper() == 'R':
                abacko.reset()
            elif action.upper() == 'Q':
                end_game = True
                continue_game = False
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
                            print('\nInvalid Move... stopped here...', end='')
                            error = True

            # display game state
            print('\nCurrent Game State:')
            abacko.show(card)
            # display moves
            print('Moves:', str(abacko.get_moves()))

            # check if game is won and ask to play again
            if abacko.isSolved(card) and action.upper() != 'Q':
                print('Congratulations! You have Solved the Abacko Stack!')
                play_again = input(
                    'Would you like to play another round? Y/n > ')
                if play_again.upper() != 'Y':
                    continue_game = False  # ends game loop
                end_game = True  # ends action loop


main()
