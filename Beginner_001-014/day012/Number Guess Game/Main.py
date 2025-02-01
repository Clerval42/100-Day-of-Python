import random

print("Welcome to Number Guess Game")
print("I'm thinking of a number between 1 and 100.")
targetNumber = random.randint(0, 100)
print(targetNumber)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guess():
    global live
    guessedNumber = 0
    while live >0 and guessedNumber != targetNumber:
        print(f"You have {live} attempts remaining to guess the number.")
        guessedNumber = int(input("Make a guess: "))
        if guessedNumber > targetNumber:
            print("Too high")
            live -= 1
        elif guessedNumber < targetNumber:
            print("Too low")
            live -= 1
    if live ==0:
        print("You've run out of guesses, you lose.")
    elif guessedNumber == targetNumber:
            print(f"You got it! The answer was {targetNumber}.")


def setDifficulty():
    global live
    if difficulty == "easy":
        live = 10
    elif difficulty == "hard":
        live = 5

setDifficulty()
guess()