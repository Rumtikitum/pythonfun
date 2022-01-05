import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

password = []

print('Welcome to random password generator. Follow the questions to create your unique password')
amt_letters = int(input('How many letters do you want in your password?....'))
amt_numbers = int(input('How many numbers do you want in your password?....'))
amt_symbols = int(input('How many symbols do you want in your password?....'))

for char in range (1, amt_letters + 1):
    random_char = random.choice(letters)
    password += random_char
    
for char in range (1, amt_numbers + 1):
    random_char = random.choice(numbers)
    password += random_char

for char in range (1, amt_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char

random.shuffle(password)
final_pw = ''.join(map(str, password))


print('Your new random password is: ' + final_pw)