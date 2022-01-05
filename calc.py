def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2



n1 = int(input('What is the first number? '))
operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
}

print('Available operations:')
for operation in operations:
    print(operation)

equation = input('What type of equation would you like to do? Type in one of the following: ')
print(equation)

n2 = int(input('What is the second number you would like to include in this equation? '))

answer = operations[equation](n1, n2)

print(f'The answer to {n1} {equation} {n2} is {answer}')

