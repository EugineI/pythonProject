print("Your password must be at least 8 characters long and contain at least numbers and two 2 special characters")
password = input("Enter your password:")
print("Password:", password)
numberCounter = 0
specialCharacterCounter = 0
counter = 0
index = 0
passLength = len(password)

while counter < passLength:
    if (password[index] == "0" or password[index] == "1" or password[index] == "2" or password[index] == "3"
            or password[index] == "4" or password[index] == "5" or password[index] == "6" or password[index] == "7"
            or password[index] == "8" or password[index] == "9"):
        numberCounter += 1
    elif (password[index] == "!" or password[index] == "@" or password[index] == "#"
          or password[index] == "$" or password[index] == "%" or password[index] == "&"
          or password[index] == "*"):
        specialCharacterCounter += 1
    counter += 1
    index += 1
if passLength >= 8 and numberCounter >= 2 and specialCharacterCounter >= 2:
    print("Output:", "\nStrong")
else:
    print("Output:", "\nWeak")
