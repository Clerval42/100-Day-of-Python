import Art

print(Art.logo)
print("Welcome to the secret auction program.")

bidAndNames = {}
isCont = True

while isCont:
    names = input("What is your name? ")
    bids = int(input("What's your bid? "))
    cont = input("Are there any other bidders? y or n:")
    if cont == "n":
        isCont = False
    elif cont =="y":
        continue
    else:
        print("ERROR INVLAID TEXT")
        break
    bidAndNames.update({names: bids})


if isCont == False:
    keyInlist = list(bidAndNames.keys())
    valueInList = list(bidAndNames.values())
    winBid = max(valueInList)
    winName = keyInlist[valueInList.index(winBid)]

    print(f"The winner is {winName} with a bid of ${winBid}")
