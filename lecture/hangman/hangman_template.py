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
    infile = open('words.txt')
    alist = infile.readlines()
    infile.close()

    play_again = True
    while play_again:
        # Choose a random entry
        entry = random.choice(alist)
        entry = entry.strip()

        # Separate the word and the hint
        word, hint = entry.split(',')

        # Display the hint
        print(hint)

        # Initialization
        template = Template(len(word))
        template.show()
        hangman = Gallows()
        incorrect = []
        gameOver = False

        # Start  one round of the game
        while not gameOver:
            guess = input('Enter a letter : ').lower()
            # input validation
            while guess in incorrect or template.existsIn(guess):
                guess = input('Enter a letter : ').lower()
            # processing
            # attempting to update the template
            result = template.update(word, guess)
            template.show()
            if result == False:
                hangman.increment()
                hangman.show()
                incorrect.append(guess)
                incorrect.sort()
                print(';'.join(incorrect))
            if template.isComplete() or hangman.get() == 5:
                gameOver = True
                if template.isComplete():
                    print('Congratulations')
                else:
                    print('R.I.P')
                    print('The word was ', word)
        reply = input('Play again ? y/N ').lower()
        if reply != 'y':
            play_again = False


main()
