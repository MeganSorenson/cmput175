# Ceaser Cipher Encrypter

def main():
    '''
    -main function of the program
    -encrypts an inputted message using an inputted ceasar cipher
    -writes a new file with the cipher and encrypted message
    '''
    encrypt()


def encrypt():
    '''
    -asks user for the name of a text file (does not have to exist already)
    -user is asked to input a message to be encrypted and to provide an interger cipher
    -encodes entered mesage using the Ceasar cipher method and entered cipher key
    -resulting file has cipher on first line and encrypted message on second line
    '''
    # ask for file
    filename = input(
        'Enter the name of the text file you would like to write: ')
    while filename[-4:] != '.txt':
        print('Invalid file extension \t', end='')
        filename = input('Please re-enter the file name: ')

    # ask for message to be encrypted and cipher
    # make sure cipher is an integer
    message = input(
        'Enter the message (of lowercase and space characters only) to be encrypted: ')
    message = message.lower()
    cipher = input('Enter the integer cipher for encryption: ')
    while not cipher.isnumeric():
        print('Invalid cipher \t', end='')
        cipher = input('Please re-enter the integer cipher: ').strip()

    # encrypt message using cipher and base 10 representation of unicode
    encrypted_message = []
    for character in message:
        # if lowercse letter, encrypt letter
        if character.islower():
            initial_unicode = ord(character)
            encrypted_unicode = initial_unicode + (int(cipher) % 26)
            # account for wrapping around alphabet
            if encrypted_unicode > ord('z'):
                encrypted_unicode = initial_unicode - (26 - (int(cipher) % 26))
            # add encrypted letter to new message
            encrypted_message.append(chr(encrypted_unicode))
        # if space, just add space to new message
        elif character == ' ':
            encrypted_message.append(character)

    # open new file in write mode and add contents
    # overwrites file if it already exists
    file = open(filename, 'w')

    file.write('{}\n{}'.format(cipher, ''.join(encrypted_message)))

    file.close()


main()
