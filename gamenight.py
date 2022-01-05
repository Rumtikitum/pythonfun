import random

compoptions = ['rock', 'paper', 'scissor']

compchoice = random.randint(0, 2)

compdec = compoptions[compchoice]

print('Welcome to my game!')
print('We will play rock, paper, scissors.')
selection = input('Choose one of the options by typing: "rock", "paper" or "scissor"....')
print('Seems as though you chose ' + selection)
print('The computer chose ' + compdec)

if compdec == selection:
    print ('We got a tie!')
elif compdec == 'paper' and selection == 'rock':
    print ('Damn. You Lose')
elif compdec == 'rock' and selection == 'paper':
    print ('You won!')
elif compdec == 'rock' and selection == 'scissor':
    print ('Damn. You Lose')
elif compdec == 'scissor' and selection == 'rock':
    print ('You won!')
elif compdec == 'scissor' and selection == 'paper':
    print ('Damn. You Lose')
elif compdec == 'paper' and selection == 'scissor':
    print ('You won!')
else:
    print('invalid input. Inputs must either be "rock", "paper" or "scissor"')