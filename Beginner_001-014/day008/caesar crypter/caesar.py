import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
print(art.logo)
userCont = True

def caesar(textt, shiftt, directionn):
    textNew = ""
    if directionn == "d":
        shiftt *= -1
    for x in textt:
        if alphabet.count(x) == 0:
            textNew += x
        else:
            index = (alphabet.index(x) + shiftt) % 26
            textNew += alphabet[index]
    print(f"the direction is {directionn.upper()} and new text is {textNew}")
    

while userCont:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    userInput = input("Do you want to continue? y or n: ")
    if userInput == "n":
        userCont = False