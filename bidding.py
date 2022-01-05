bid = {}
still_bidding = True

def find_high(bid):
    highest_bid = 0
    for name in bid:
        current_number = int(bid[name])
        if current_number > int(highest_bid):
            highest_bid = current_number
            winner = name
    print(f'Your winner is {winner} with a bid of ${highest_bid}')


while still_bidding is True:
    name = input('Input your name. ')
    dollar_amount = input('Input your bid. ')

    bid[name] = dollar_amount

    next_person = input('Is there another person after you? ')
    if next_person == 'no':
        find_high(bid)
        still_bidding = False

