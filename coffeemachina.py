MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


functional_machine = True


def print_menu():
    print('=================================================================')
    print('CURRENT RESOURCES')
    print(f'>> Water: {resources["water"]}')
    print(f'>> Milk: {resources["milk"]}')
    print(f'>> Coffee: {resources["coffee"]}')
    print('=================================================================')
    print('RECIPES')
    print(f'Espresso >> Ingredients: {MENU["espresso"]["ingredients"]}')
    print(f'Latte >> Ingredients: {MENU["latte"]["ingredients"]}')
    print(f'Cappuccino >> Ingredients: {MENU["cappuccino"]["ingredients"]}')
    print('=================================================================')



def print_resources():
    print(f'>> Water: {resources["water"]}ml')
    print(f'>> Milk: {resources["milk"]}ml')
    print(f'>> Coffee: {resources["coffee"]}grams')


def make_espresso(): 
    print('Making now.')
    esp_water = int(MENU['espresso']['ingredients']['water'])
    esp_coffee = int(MENU['espresso']['ingredients']['coffee'])
    base_water = int(resources['water'])
    base_coffee = int(resources['coffee'])
    new_base_coffee = base_coffee - esp_coffee
    if new_base_coffee < 1:
        print('not enough coffee')
    else:
        (resources['coffee']) = new_base_coffee
        current_coffee = (resources['coffee'])
        print(f'Machine now has {current_coffee}grams of coffee grinds left.')
    new_base_water = base_water - esp_water
    if new_base_water < 1:
        print('not enough water')
    else:
        (resources['water']) = new_base_water
        current_water = (resources['water'])
        print(f'Machine now has {current_water}ml of water left.')
        print('Enjoy your espresso!')



def make_cappuccino(): 
    print('Making now.')
    cap_water = int(MENU['cappuccino']['ingredients']['water'])
    cap_coffee = int(MENU['cappuccino']['ingredients']['coffee'])
    cap_milk = int(MENU['cappuccino']['ingredients']['milk'])
    base_water = int(resources['water'])
    base_coffee = int(resources['coffee'])
    base_milk = int(resources['milk'])
    new_base_coffee = base_coffee - cap_coffee
    if new_base_coffee < 1:
        print('not enough coffee')
    else:
        base_coffee = new_base_coffee
        print(f'Machine now has {base_coffee}grams of coffee grinds left.')
    new_base_water = base_water - cap_water
    if new_base_water < 1:
        print('not enough coffee')
    else:
        (resources['water']) = new_base_water
        current_water = (resources['water'])
        print(f'Machine now has {current_water}ml of water left.')
    new_base_milk = base_milk - cap_milk
    if new_base_milk < 1:
        print('not enough coffee')
    else:
        (resources['milk']) = new_base_milk
        current_milk = (resources['milk'])
        print(f'Machine now has {current_milk}ml of milk left.')
        return (resources['milk'])
    print('Enjoy your cappuccino!')



def make_latte(): 
    print('Making now.')
    latte_water = int(MENU['latte']['ingredients']['water'])
    latte_coffee = int(MENU['latte']['ingredients']['coffee'])
    latte_milk = int(MENU['latte']['ingredients']['milk'])
    base_water = int(resources['water'])
    base_coffee = int(resources['coffee'])
    base_milk = int(resources['milk'])
    new_base_coffee = base_coffee - latte_coffee
    if new_base_coffee < 1:
        print('not enough coffee')
    else:
        base_coffee = new_base_coffee
        print(f'Machine now has {base_coffee}grams of coffee grinds left.')
    new_base_water = base_water - latte_water
    if new_base_water < 1:
        print('not enough coffee')
    else:
        (resources['water']) = new_base_water
        current_water = (resources['water'])
        print(f'Machine now has {current_water}ml of water left.')
    new_base_milk = base_milk - latte_milk
    if new_base_milk < 1:
        print('not enough coffee')
    else:
        (resources['milk']) = new_base_milk
        current_milk = (resources['milk'])
        print(f'Machine now has {current_milk}ml of milk left.')
        return (resources['milk'])
    print('Enjoy your latte!')


def refill():
    print('=================================================================')
    print_resources()
    print('=================================================================')
    which_resource = input('Which resource would you like to refill?: water, coffee, milk... ')
    if which_resource == 'water':
        base_water = int(resources['water'])
        add_limit = 500 - base_water
        add_water = int(input(f'The machine cannot handle more than 500ml of water. Currently you can only add {add_limit}. How much water are you adding? '))
        if add_water < add_limit:
            new_water_amt = base_water + add_water
            resources["water"] = new_water_amt
            print(f'Thanks for the refill. Water is now at {resources["water"]}ml')
        else:
            print('That is too much water. Refill denied.')
    elif which_resource == 'milk':
        base_milk = int(resources['milk'])
        add_limit_milk = 500 - base_milk
        add_milk = int(input(f'The machine cannot handle more than 500ml of water. Currently you can only add {add_limit}. How much water are you adding? '))
        if add_milk < add_limit_milk:
            new_milk_amt = base_milk + add_milk
            resources["milk"] = new_milk_amt
            print(f'Thanks for the refill. Milk is now at {resources["milk"]}ml')
        else:
            print('That is too much Milk. Refill denied.')
    if which_resource == 'coffee':
        base_coffee = int(resources['coffee'])
        add_limit_coffee = 500 - base_coffee
        add_coffee = int(input(f'The machine cannot handle more than 500ml of water. Currently you can only add {add_limit_coffee}. How much water are you adding? '))
        if add_coffee < add_limit_coffee:
            new_coffee_amt = base_coffee + add_coffee
            resources["coffee"] = new_coffee_amt
            print(f'Thanks for the refill. Coffee is now at {resources["coffee"]}ml')
        else:
            print('That is too much coffee. Refill denied.')
    else:
        print('This is not an option available')    
        print('=================================================================')
    anymore = input('Would you like to refill anything else? y or n? ')
    if anymore == 'y':
        refill()
    else:
        print('Ok!')


def make_coffee():
    print('WELCOME TO COFFEE MAKER EXPRESS 4000')
    resources
    is_on = True
    while is_on:
        print('What would you like to do? ')
        print('>> Make Coffee')
        print('>> Check Resources')
        print('>> Refill')
        print('>> Turn Off')
        choice = input('Please choose one of the following functions... ').lower()
        if choice == 'turn off':
            password = input('Please input password: ')
            if password == 'terror':
                print('>> Turning off systems. This may take a few minutes')
                is_on = False
            else:
                print('Incorrect password. Function denied. ')
        elif choice == 'refill':
            refill()
        elif choice == 'check resources':
            print_resources()
            input('Press "Enter" when ready. ')
        elif choice == 'make coffee':
            print('What coffee would you like to make?')
            print('Not enough resources to make your cup? Would you like to refill the machine? Press "Refill". ')
            print('"Cancel" to cancel order. ')
            print_menu()
            what_coffee = input('').lower()
            if what_coffee == 'cancel':
                print('Ok.')
            elif what_coffee == 'espresso':
                make_espresso()
            elif what_coffee == 'latte':
                make_latte()
            elif what_coffee == 'cappuccino':
                make_cappuccino()
            elif what_coffee == 'refill':
                refill()
            else:
                print('Invalid input. Try again. ')
        else:
            print('Invalid input. Try again. ')





while functional_machine:
    on_button = input('This machine is currently off. Press "Turn On" to turn machine on. ').lower()
    if on_button == 'turn on':
        admin_password = input('Please input admin password to begin operating device. ')
        if admin_password == 'cheeky':
            make_coffee()
        else:
            print('Invalid Password. We are sorry!')

