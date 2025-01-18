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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "amount": 0
}

def drink(user_order):
    """This function extracts the ingredients and cost for a particular drink."""
    if user_order == "espresso":
        return MENU[user_order]
    elif user_order == "latte":
        return MENU[user_order]
    else:
        return MENU[user_order]

def sufficient_resources(check_resources, user_choice):
    """This function checks whether there are sufficient resources in the coffee machine for a particular drink."""
    if len(check_resources) == len(user_choice):
        for i in check_resources:
            if check_resources[i] < user_choice["ingredients"][i]:
                print(f"Sorry there is not enough {i}")
                return False
    else:
        for i in ["water","coffee"]:
            if check_resources[i] < user_choice["ingredients"][i]:
                print(f"Sorry there is not enough {i}")
                return False
    return True

def process_coins():
    """This function takes the user's coins as inputs and returns the total sum of coins inserted in the machine."""
    total = int(input("How many quarters?")) * 0.25 # 0.25
    total += int(input("How many dimes?")) * 0.10 # 0.10
    total += int(input("How many nickles?")) * 0.05 # 0.05
    total += int(input("How many pennies?")) * 0.01 # 0.01
    return total

def coffee_machine(resources, coffee_order, money, user_order):
    """This function makes the coffee and updates the resources for the coffee machine."""
    if user_order != "espresso":
        resources["water"] -= coffee_order["ingredients"]["water"]
        resources["milk"] -= coffee_order["ingredients"]["milk"]
        resources["coffee"] -= coffee_order["ingredients"]["coffee"]
        money["amount"] += coffee_order["cost"]
        print(f"Here is your {user_order}!")
        return resources, money
    else:
        resources["water"] -= coffee_order["ingredients"]["water"]
        resources["coffee"] -= coffee_order["ingredients"]["coffee"]
        money["amount"] += coffee_order["cost"]
        print(f"Here is your {user_order}!")
        return resources, money

def coffee_maker():

    coffee_function = True

    while coffee_function:

        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        user_choice = drink(order)
        print(user_choice)

        current_resources = input("Do you want to see the current resources of the coffee machine? Type 'report' for yes and 'n' for no.").lower()

        if current_resources == "report":
            print(f"Water: {resources["water"]}ml\nMilk : {resources["milk"]}ml\nCoffee : {resources["coffee"]}g\nMoney : ${money["amount"]}")

        if sufficient_resources(resources, user_choice):
            print("Please insert coins.")
            money_for_drink = process_coins()

            if money_for_drink < user_choice["cost"]:
                print("Sorry that is not enough money. Money refunded.")
            elif money_for_drink > user_choice["cost"]:
                residual = money_for_drink - user_choice["cost"]
                print(f"Here is ${round(residual, 2)} in change")
                coffee_machine(resources, user_choice, money, order)

        turn_off_machine = input("Do you want to turn of the coffee machine? Type 'off' for yes or 'continue' for no.").lower()

        if turn_off_machine == "off":
            coffee_function = False

coffee_maker()