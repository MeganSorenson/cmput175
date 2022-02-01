# Scrabble Dictionary Class

# Author: Megan Sorenson

class ScrabbleDict:
    def __init__(self, size, filename):
        '''
        Initializes a dictionary based on lines in a file
        (keys = first word in line, and values = full line)
        Only inclides lines whose first word is of a specified length
        Inputs: size (int) rep. specified word length and filename (str) rep. txt file with lines
        Returns: None
        '''
        self.size = size

        # read file lines
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()

        # add word : line to dictionary if word is specified size
        self.word_dict = {}
        for line in lines:
            word = line.split(' ')[0]
            if len(word) == size:
                self.word_dict[word] = line

    def check(self, word):
        '''
        Checks if a word is in the word dictionary
        Inputs: word (str) rep. the word being checked
        Returns: True if the word is in the dictionary, otherwise False (bool)
        '''
        if self.word_dict.get(word, False) != False:
            return True
        else:
            return False

    def getSize(self):
        '''
        Gets the size of the word dictionary
        Inputs: None
        Returns: an int rep. the number of words in the dictionary
        '''
        return len(self.word_dict)

    def getWords(self, letter):
        '''
        Sorts a list of words alphabetically from a word dictionary starting with a letter
        Inputs: letter (str) rep. the letter that the words will start with
        Returns: a sorted list of words
        '''

        # iterate through dictionary keys checking first letter
        # add key (word) to new list of words if the first letter is the specified letter
        word_list = []
        for word in self.word_dict.keys():
            if word[0] == letter:
                word_list.append(word)

        return word_list.sort()

    def getWordSize(self):
        '''
        Gets the length of the words from a word dictionary
        Inputs: None
        Returns: an int rep. the length of words stored in the dictionary
        '''
        return self.size


if __name__ == '__main__':
    # tests the ScrabbleDict class and its methods
    pass
