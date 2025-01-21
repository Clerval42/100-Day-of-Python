import random
import hm_art
import words
word_list = words.word_lists

chosen_word = random.choice(word_list)
lives = 6
isFinished = False
print(chosen_word)

print(hm_art.logo)
display = []
for n in chosen_word:
    display += "_"

while not isFinished:
    counter = 0
    guess = input("guess a letter: ").lower()

    for x in range(len(chosen_word)):
        letter = chosen_word[x]
        if letter == guess:
            display[x] = guess
            counter += 1
    if counter == 0:
        lives -= 1
    print(display)
    print(hm_art.stages[lives])
    if display.count("_") == 0 or lives == 0:
        isFinished = True
if lives>0:
    print("YOU FOUND THE WORD")
else:
    print("YOU LOSE")