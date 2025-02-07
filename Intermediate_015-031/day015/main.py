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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def printReport():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money:  {money}$")
    
def makeCoffee(input):
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["milk"] -= milk
    print(f"Here is your {input}. Enjoy!")
    printReport()
    

def isEnough(total, input):
    coffeeCost = MENU[input]["cost"]
    global money

    if coffeeCost > total:
        print("Sorry that's not enough money. Money refunded")
    else:
        money += coffeeCost
        if coffeeCost < total:
            remainderMoney = round(total - coffeeCost, 2)
            print(f"Here is ${remainderMoney} dollars in change")
        makeCoffee(input)

def inputMoney():
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))*0.25
    dimes = int(input("how many dimes?: "))*0.10
    nickles = int(input("how many nickles?: "))*0.05
    pennies = int(input("how many pennies?: "))*0.01
    total = quarter + dimes + nickles + pennies
    return total


def checkResources(input):
    global water
    global coffee
    global milk
    water = MENU[input]["ingredients"]["water"]
    coffee = MENU[input]["ingredients"]["coffee"]
    if input == "latte" or input == "cappuccino":
        milk = MENU[input]["ingredients"]["milk"]
    else:
        milk = 0

    if water > resources["water"]:
        print("Sorry there is not enough water.")
    elif coffee > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    elif milk > resources["milk"]:
        print("Sorry there is not enough milk.")


def check(input):
    if input == "off":
        return
    elif input == "report":
        printReport()
        return
    elif input in MENU:
        checkResources(input)
        isEnough(inputMoney(), input)


def work():
    prefer = input("What would you like? (espresso/latte/cappuccino): ")
    check(prefer)


work()
