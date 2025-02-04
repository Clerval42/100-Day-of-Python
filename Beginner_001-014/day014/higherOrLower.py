import gameData
import random
print(gameData.logo)

dictionary = gameData.data
followerA = 0
followerB = 0
score = 0


def selectA():
    global followerA
    rangeDataA = random.randint(0, 49)
    nameA = dictionary[rangeDataA]["name"]
    followerA = dictionary[rangeDataA]["follower_count"]
    descriptionA = dictionary[rangeDataA]["description"]
    countryA = dictionary[rangeDataA]["country"]
    print(f"Compare A: {nameA}, a {descriptionA}, from {countryA}.")


def randIntExcept(followerA):
    while True:
        num = random.randint(0, 49)
        if num != followerA:
            return num


def selectB():
    global followerB
    rangeDataB = random.randint(0, 49)
    rangeDataB == randIntExcept(followerA)
    nameB = dictionary[rangeDataB]["name"]
    followerB = dictionary[rangeDataB]["follower_count"]
    descriptionB = dictionary[rangeDataB]["description"]
    countryB = dictionary[rangeDataB]["country"]
    print(f"Compare B: {nameB}, a {descriptionB}, from {countryB}.")


def compare():
    global score
    choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choose == "a" and followerA > followerB:
        score += 1
        print(f"Correct, your score is {score}")
        return game()
    elif choose == "b" and followerA < followerB:
        score += 1
        print(f"Correct, your score is {score}")
        return game()
    else:
        return print(f"Game Over. Your score is {score}")


def game():
    selectA()
    print(gameData.vs)
    selectB()
    compare()


game()
