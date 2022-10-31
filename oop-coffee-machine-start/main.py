from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = MenuItem("", "", "", "", "")
# menu_item = MenuItem()
menu = Menu()
make_order = CoffeeMaker()
money = MoneyMachine()

is_machine_on = True

while is_machine_on:
    my_order = input(f"what would you like: {menu.get_items()} ")
    if my_order == "off":
        is_machine_on = False
    elif my_order == "report":
        make_order.report()
        money.report()
    else:
        drink = menu.find_drink(my_order)
        if make_order.is_resource_sufficient(drink):
            # menu_item.cost = menu.
            if money.make_payment(drink.cost):
                make_order.make_coffee(drink)
                money.report()








# print(make_order.report())
# print(make_order.is_resource_sufficient(my_order))
# money.make_payment(1.5)
# print(make_order.make_coffee(my_order))
# print(money.report())
# print(make_order.report())



# print(drinks.get_items())


# print(my_order)