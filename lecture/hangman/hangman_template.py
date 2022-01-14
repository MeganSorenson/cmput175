import random


class Gallows:
    def __init__(self):
        self.step = 0

    def increment(self):
        self.step = self.step + 1

    def show(self):
        l1 = l2 = l3 = l4 = l5 = l6 = ''
        if self.step > 0:
            l2 = l3 = l4 = l5 = l6 = ' |'
        if self.step > 1:
            l1 = '  _____'
        if self.step > 2:
            l6 = '/|\\'
        if self.step > 3:
            l2 = ' |/    |'
        if self.step == 5:
            l3 = ' |     o'
            l4 = ' |    /|\\'
            l5 = ' |    / \\'
        print(l1, l2, l3, l4, l5, l6, sep='\n')

    def get(self):
        return self.step


class Template:
    def __init__(self, size):
        # initializes the templates as a list of dashes
        self.dashes = ['_'] * size

    def show(self):
        # prints the template as a string
        print(' '.join(self.dashes))

    def update(self, word, guess):
        # updates the template
        # returns True if guess is found in word
        # False otherwise
        i = 0
        found = False
        while i < len(word):
            if guess == word[i]:
                self.dashes[i] = guess
                found = True
            i = i + 1
        return found

    def isComplete(self):
        # return True if template is complete
        # False otherwise
        if '_' not in self.dashes:
            return True
        else:
            return False

    def existsIn(self, guess):
        # returns True if guess exists in Template
        # False otherwise
        if guess in self.dashes:
            return True
        else:
            return False


def main():
    # words.txt is a file that contains a list of word and hint

    # Choose a random entry

    # Separate the word and the hint

    # Display the hint

    # Initialization

    # Start  one round of the game


main()
