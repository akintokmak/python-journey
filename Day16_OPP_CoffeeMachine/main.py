from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

def user_input():
    """
    Keeps asking until we get a valid drink name, 'report', or 'off'.
    Special commands are checked first so find_drink() never sees them.
    """
    while True:
        user_choose = input(f"What would you like? ({menu_list.get_items()}): ").lower().strip()
        if user_choose == "report":
            coffee_maker.report()
            money.report()
            continue
        elif user_choose == "off":
            return user_choose
        elif menu_list.find_drink(user_choose):
            return user_choose

def coffee_machine():
    """
    Main loop — keeps the machine running until 'off' is entered.
    Order matters: check ingredients → take payment → make coffee.
    """
    while True:
        user_choice = user_input()
        if user_choice == "off":
            break
        drink = menu_list.find_drink(user_choice)
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        if money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

coffee_machine()

