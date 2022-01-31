# ----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
# uses a list and a variable representing index
# to enable the functionality of the forward and back buttons of a web browser
#
# Author: Megan Sorenson
# ----------------------------------------------------

def getAction():
    '''
    prompts the user to enter an action for the web browser
    Inputs: none
    Returns: a str representing the valid character entered by the user
    '''
    # TO DO: delete pass and write your code here

    # possible user actions
    user_actions = ('=', '<', '>', 'q')

    # get user action based on user input until user inputs valid action
    invalid_entry = True
    while invalid_entry:
        user_action = input("Enter {new_site} to enter a URL, {go_back} to go back, {go_forward} to go forward, {quit_program} to quit: ".format(
            new_site=user_actions[0], go_back=user_actions[1], go_forward=user_actions[2], quit_program=user_actions[3]))

        if user_action in user_actions:
            invalid_entry = False
        else:
            print("Invalid entry.")

    return user_action


def goToNewSite(current, pages):
    '''
    prompts the user to enter a new website address 
    updates the list of pages and current index as necessary
    Inputs: current (int) representing index of current website and pages (list) representing the websites of the browser
    Returns: an int representing the index to the current site
    '''
    # TO DO: delete pass and write your code here

    # get user input for website
    new_page = input("URL: ")

    # add new website to the end of pages
    # as long as your current index is the last website in pages
    if current == len(pages) - 1:
        pages.append(new_page)
    # otherwise, remove the trailing websites in pages
    # and add the website to the end of pages
    else:
        for i in range(len(pages) - 1 - current):
            pages.pop()
        pages.append(new_page)
    # update website index by one
    current += 1

    return current


def goBack(current, pages):
    '''
    functions as the back button of a web browser by going back one index in the list of websites
    displays an error message is there are no websites in the back history
    Inputs: current (int) representing index of current website and pages (list) representing the websites of the browser
    Returns: an int representing the index to the current site
    '''
    # TO DO: delete pass and write your code here

    # go back one website if there are websites in the back history
    if len(pages) > 1:
        current -= 1
    else:
        print('Cannot got back.')

    return current


def goForward(current, pages):
    '''
    functions as the forward button of a web browser by going forward one index in the list of websites
    displays an error message is there are no websites in the forward history
    Inputs: current (int) representing index of current website and pages (list) representing the websites of the browser
    Returns: an int representing the index to the current site
    '''
    # TO DO: delete pass and write your code here

    # go forward one website if there are websites in the forward history
    if current != len(pages) - 1:
        current += 1
    else:
        print('Cannot go forward.')

    return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False

    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()

        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True

    print('Browser closing...goodbye.')


if __name__ == "__main__":
    main()
