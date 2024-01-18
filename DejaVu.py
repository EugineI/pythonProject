phrase = input("Enter the phrase:")
check = len(phrase)
counter = 0
index = 0
newPhrase = ""
while counter < check:
    if phrase[index] in newPhrase and phrase[index] != " ":
        newPhrase += ""
    else:
        newPhrase += phrase[index]
    counter += 1
    index += 1
print("Phrase without repeated characters is ", newPhrase)
if newPhrase == phrase:
    print("Unique")
else:
    print("Deja Vu")
