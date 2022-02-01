# Wordle175 Word Dictionary Generator
# reads a text file with 5 letter words
# generates a new file where each line is a word from the input file
# Author: Megan Sorenson

def main():
    input_filename = 'word5Dict.txt'
    output_filename = 'scrabble5.txt'

    # read input file
    input_file = open(input_filename, 'r')
    unsplit_lines = input_file.readlines()
    input_file.close()

    # split lines from input file into words and write words to output file
    output_file = open(output_filename, 'w')
    for line in unsplit_lines:
        words = line.split('#')
        for word in words:
            output_file.write('{word}\n'.format(word=word))
    output_file.close()


main()
