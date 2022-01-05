print('So you wanna tip? ')

bill = input('What is your bill amount? ')
tip = input('What is your desired tip amount?  (percentage without "%") ')

amount = float(bill) * (1 + (.01 * float(tip)))
final = round(amount, 2)
print('Here is how much you should pay ' + str(final) + '.')