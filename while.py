from random import *

hardlevel = 5
easylevel = 10

def randomshuffler():
    number = randint(1,100)
    return number


def choice():
    difficulty = input('Would you prefer "easy" or "hard"? ')
    print(f'Great! You chose {difficulty}.')
    if difficulty == 'easy':
        return easylevel
    elif difficulty == 'hard':
        return hardlevel

    else:
        print('please use "easy" or "hard"')
    

def restart():
    again = input('again? ')
    if again == 'yes':
        game()
    else:
        print('goodbye')

def game():   
    turns = 0
    number = randomshuffler()
    print(number)
    print('Welcome to number guesser!')
    print('Rules are simple. Guess the number we are thinking of. It will be between 1-100.')
    print('Before we start....')
    chances = choice()
    print(f'You have {chances} amount of chances')
    while turns < chances:
        response = int(input('WHat is your guess? '))
        if response == number:
            print('wow you got it')
            restart()
        elif response > number:
            turns +=1
            if turns == chances:
                print('you lose')
            else:
                print('try again....but lower this time')
        elif response <number:
            turns +=1
            if turns == chances:
                print('you lose')
            else:
                print('try again....but higher this time')
            

game()




