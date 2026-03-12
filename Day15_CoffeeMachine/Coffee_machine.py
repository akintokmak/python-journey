from menu_and_resources import MENU,resources


def user_input():
    """ Keeps asking until the user types something we actually understand.
    Report and Off are handled here too so the main loop stays clean."""
    while True:
        user_choose = input("What would you like? (Espresso/Latte/Cappuccino): ").title().strip()
        if user_choose in ('Espresso', 'Latte', 'Cappuccino'):
            return user_choose
        elif user_choose == 'Report':
            coffee_report()
            continue
        elif user_choose == 'Off':
            return  user_choose
        else:
            print("Invalid input! Please choose (Espresso/Latte/Cappuccino)")

def coffee_report():
    """ Quick snapshot of what's left in the machine."""
    print(f"Water : {resources['water']}ml")
    print(f"Milk  : {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${resources['money']}")

def check_resources(user_choice):
    user = user_choice.lower().strip()
    milk_of_coffee = 0
    water_of_coffee = MENU[user]['ingredients']['water']
    if user != 'espresso':
        milk_of_coffee = MENU[user]['ingredients']['milk']
    coffee_of_coffee = MENU[user]['ingredients']['coffee']
    if resources['water'] < water_of_coffee:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < milk_of_coffee:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < coffee_of_coffee:
        print("Sorry there is not enough coffee")
        return False
    return True

def process_coins():
    """Collect coins one by one and calculate the total.
        If the user types something weird, just ask again."""
    print("Please insert coin")
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_amount = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01,2)
            print(f"${total_amount}")
            return total_amount
        except ValueError:
            print("Invalid Input!")

def check_transaction(user_money,user_choice):
    """Three cases: not enough, too much, or exact.
    Either way, only the drink's cost goes into the machine — not the full amount."""
    user = user_choice.lower().strip()
    money_of_coffee = MENU[user]['cost']
    if user_money < money_of_coffee:
        print("Sorry that's not enough money.")
        return False
    elif user_money > money_of_coffee:
        resources['money'] += money_of_coffee
        user_money = round(user_money - money_of_coffee, 2)
        print(f"Here is ${user_money} in change.")
        return True
    else:
        print("Money is ok.")
        resources['money'] += money_of_coffee
        return True

def make_coffee(user_choice):
    """Deduct ingredients and hand over the drink.
    Espresso skips milk since it's not in its recipe."""
    user = user_choice.lower().strip()
    resources['water'] -= MENU[user]['ingredients']['water']
    if user != 'espresso':
        resources['milk']  -= MENU[user]['ingredients']['milk']
    resources['coffee'] -= MENU[user]['ingredients']['coffee']
    print(f"Here is your {user_choice}. Enjoy!")

def coffee_machine():
    """Main loop. Keeps the machine running until someone types 'Off'.
    Order matters here: check ingredients → take money → verify → serve."""
    while True:
        user_choice=user_input()
        if user_choice == 'Off':
            break
        if  not check_resources(user_choice=user_choice):
            continue
        user_money = process_coins()
        if check_transaction(user_money=user_money, user_choice=user_choice):
            make_coffee(user_choice)

coffee_machine()


