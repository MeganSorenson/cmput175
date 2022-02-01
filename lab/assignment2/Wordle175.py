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
                self.word_dict[word] = line.strip()

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
        word_list.sort()

        return word_list

    def getWordSize(self):
        '''
        Gets the length of the words from a word dictionary
        Inputs: None
        Returns: an int rep. the length of words stored in the dictionary
        '''
        return self.size


if __name__ == '__main__':
    # tests the ScrabbleDict class and its methods

    # create test file
    test_file = open('test.txt', 'w')
    lines = ['apple is a fruit', 'amber is a color',
             'attic is a room', 'basil is a herb']
    for line in lines:
        test_file.write('{line}\n'.format(line=line))
    test_file.close()

    # create dictionary
    word_size = 5
    s = ScrabbleDict(word_size, 'test.txt')
    # view initialized dictionary
    print('initialized dictionary: ', end='')
    print(s.word_dict)

    # TEST 1: check if word size is the same as initialized
    print('\nTEST 1: check getWordSize()')
    if s.getWordSize() == word_size:
        print('test1: word size same as initialized')
        print('test1: PASSED')
    else:
        print('test1: word size not the same as initialized')
        print("test1: FAILED")

    # TEST 2: check getWords()
    print('\nTEST 2: check getWords() for the letter a')
    letter = 'a'
    number_a_words = 3  # determined from when test.txt was created
    word_list = s.getWords(letter)
    print('test2: words starting with a: {word_list}'.format(
        word_list=word_list))
    if len(word_list) == number_a_words:
        print('test2: expected number of {letter} words in dictionary'.format(
            letter=letter))
        print('test2: PASSED')
    else:
        print('test2: unexpected number of {letter} words in dictionary'.format(
            letter=letter))
        print('test2: FAILED')

    # TEST 3: check getSize()
    print('\nTEST 3: check getSize()')
    if s.getSize() == len(lines):
        print('test3: expected number of words in dictionary')
        print('test3: PASSED')
    else:
        print('test3: unexpected number of words in dictionary')
        print('test3: FAILED')

    # TEST 4: check check()
    print('\nTEST 4: check check() using known word in dictionary')
    known_word = 'basil'
    if s.check(known_word):
        print('test4: known word in dictionary')
        print('test4: PASSED')
    else:
        print('test4: known word not in dictionary')
        print('test4: FAILED')
