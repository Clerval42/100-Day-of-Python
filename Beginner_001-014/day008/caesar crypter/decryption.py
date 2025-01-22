alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    textNew = ""
    for x in plain_text:
        indexNew = alphabet.index(x) + shift_amount
        if indexNew > 25:
            indexNew = indexNew-26
        textNew += alphabet[indexNew]
    print("The encoded text is " + textNew)

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


def decrypt(cipher_text, shift_amount):
    textOld = ""
    for x in cipher_text:
        indexOld = alphabet.index(x) - shift_amount
        if indexOld <0:
            indexOld = 26+indexOld 
        textOld += alphabet[indexOld]
    print(f"The decoded text is {textOld}")
    # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
    
if direction =="e":
    encrypt(text,shift)
elif direction=="d":
    decrypt(text,shift)
else:
    print("error")