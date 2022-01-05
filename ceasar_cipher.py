alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def questionaire():
    word = input('What would you like to encode/ decode? ')
    shift = input('How many spaces will you like to shift the letters? ')
    direction = input('Would you prefer to encode or decode? ')

    def encrypt(word, shift, direction):
        cipher_text = ''
        if direction == 'decode':
            shift = int(shift) * -1
        for letters in word:
            letter_index = alphabet.index(letters)
            new_index = letter_index + int(shift)
            new_letter = alphabet[new_index]
            cipher_text += new_letter
        print(cipher_text)
        loop = input('encrypt something else? ')
        if loop == "yes":
            questionaire()
        else:
            print('goodbye')

    encrypt(word, shift, direction)


questionaire()