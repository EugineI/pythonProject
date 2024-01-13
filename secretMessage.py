alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
message = input("Enter your message:").upper()
newMessage = ""
counter = 0
mesIndex = 0
while counter < len(message):
    if message[mesIndex] in alphabets:
        index = alphabets.index(message[mesIndex])
        newMessage = newMessage + alphabets[(index+1)*-1]
    else:
        newMessage = newMessage + message[mesIndex]
    counter += 1
    mesIndex += 1
print(newMessage.lower())
