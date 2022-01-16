# Ceaser Cipher Decrypter
# reads a user-inputted text file with a cipher and an encrypted message
# decrypts the message and prints the result

def main():
    '''
    -main function of the Ceaser Ciper Decryption program
    -read file and decrypts message using user-defined functions
    -returns NoneType
    '''

    # ask user for the name of a text file
    filename = getInputFile()

    # decrypt the encrypted message in the file and print the message
    decrypt(filename)


def getInputFile():
    '''
    -asks user for the name of a text file
    -ask until the user gives a filename with a .txt extension
    -give error message if wrong file extension
    -returns the valid name of the text file as a str
    '''
    filename = input("Enter the input filename: ")
    while filename[-4:] != ".txt":
        print("Invalid filename extension.", end="\t")
        filename = input("Please re-enter the input filename: ")
    return filename


def decrypt(filename):
    ''' 
    -decrpyts a Ceasar cipher incripted message from a file
    -filename is a str representing the file with the info
    -file is assumed to have two lines
    -first line is a positive int representing the cipher key
    -second line is series of encrypted words (using Ceasar cipher)
    -returns NoneType
    '''

    # open and read file
    file = open(filename, "r")
    cipher = int(file.readline().strip())
    encrypted_message = file.readline().strip().lower()
    file.close()

    decrypted_message = []
    # keep in mind that unicode are represented as base 10 not hexidecimal
    for character in encrypted_message:
        # deal with lowercase alphabet letters
        if character.islower():
            # get encrypted unicode of character
            encrypted_unicode = ord(character)
            # go backwards in unicode cipher number of times to find original unicode
            #   modulo 26 accounts for ciphers larger than 26
            unicode_shift = cipher % 26
            decrypted_unicode = encrypted_unicode - unicode_shift
            # if the decrypted unicode is outside of the lowercase alphabet range,
            # go forward instead of backwards using the new formula (accounts for wrapping around alphabet)
            if decrypted_unicode < ord("a"):
                decrypted_unicode = encrypted_unicode + (26 - unicode_shift)
            # add decrypted character to new message
            decrypted_message.append(chr(decrypted_unicode))
        # deal with non alphabet letters
        else:
            # add inital space to new message
            # only if there hasn'y already just been a space appended
            # accounts for inconsistent spacing between words
            if encrypted_message[-1] != " ":
                decrypted_message.append(" ")

    # print decrypted message
    print("The decrypted message is:")
    print("".join(decrypted_message))


main()
