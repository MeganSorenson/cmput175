# ----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
# implements the functionality of a web browser back/forward button using stacks
# Author: Megan Sorenson
# ----------------------------------------------------

from stack import Stack


def getAction():
    '''
    Prompt user to eneter =, <, >, or q
    Raises an exception if the user enters anything other than this
    Inputs: None
    Returns: the valid character eneter by the user (str) if there are no raised exceptions
    '''
    # valid user actions
    user_actions = ('=', '<', '>', 'q')
    # get user action based on user input and raise exception is not valid
    try:
        user_action = input("Enter {new_site} to enter a URL, {go_back} to go back, {go_forward} to go forward, {quit_program} to quit: ".format(
            new_site=user_actions[0], go_back=user_actions[1], go_forward=user_actions[2], quit_program=user_actions[3]))
        # check if error by trying to find user_action in list of valid actions
        user_actions.index(user_action)

        return user_action
    except:
        # runs if ther user action was not valid
        raise Exception('Invalid entry.')


def goToNewSite(current, bck, fwd):
    '''
    Prompts the user to enter a new website address 
    Updates the two website stacks
    Inputs: current (str) rep. the current website and 
    bck (Stack) rep. a reference to the web addresses to go back and
    fwd (Stack) rep. a reference to the web addresses to go forward
    Returns: the prompted website (str)
    '''
    # get user input for website
    new_page = input("URL: ")

    # push current to back Stack
    bck.push(current)
    # clear forward Stack
    fwd.clear()

    return new_page


def goBack(current, bck, fwd):
    '''
    Goes back by one website 
    Handles exception that the back stack is empty by displaying an error
    Inputs: current (str) rep. the current website and
    bck (Stack) rep. a reference to the web addresses to go back and
    fwd (Stack) rep. a reference to the web addresses to go forward
    Returns: current website (str) if exception raises, otherwise previous webpage (str)
    '''
    try:
        # new current is top of the back Stack
        new_current = bck.pop()

        # only runs if no exception raised on pop
        # push old current to forward Stack
        fwd.push(current)
        return new_current
    except Exception as e:
        # could not pop, so display error and nothing changes
        print(e.args[0])
        return current


def goForward(current, bck, fwd):
    '''
    Goes forward one website
    Handles exception that forward stack is empty by displaying error
    Inputs: current (str) rep. the current website and
    bck (Stack) rep. a reference to the web addresses to go back and
    fwd (Stack) rep. a reference to the web addresses to go forward
    Returns: current website (str) if exception raises, otherwise next website (str)
    '''
    try:
        # peek to see if forward Stack is empty
        fwd.peek()

        # only runs if no exception raised on peek
        # new current is the top of the forward Stack
        new_current = fwd.peek()
        # push olf current to back Stack
        bck.push(current)
        return new_current
    except Exception as e:
        # could not go forward, so dispay error and nothing changes
        print(e.args[0])
        return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()

    current = HOME
    quit = False

    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()

        except Exception as actionException:
            print(actionException.args[0])

        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            # TO DO: add code for the other valid actions ('<', '>', 'q')
            # HINT: LOOK AT LAsB 4
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True

    print('Browser closing...goodbye.')


if __name__ == "__main__":
    main()
