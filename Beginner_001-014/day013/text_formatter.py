text = input("Give me a title ")
textLower = text.lower()
text_with_snake_case = textLower.replace(" ", "_")+".py"
print(text_with_snake_case)

textList = list(textLower)
textWithCamelCase =""

for x in textList:
    if x == " ":
        index = textList.index(x) + 1
        textList[index] = textList[index].upper()
    textWithCamelCase +=x
textWithCamelCase = textWithCamelCase.replace(" ", "")+".py"

print(textWithCamelCase)