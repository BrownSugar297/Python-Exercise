import random

RandomNumber = random.randrange(1,5)
userInput = int(input("Guess the number: "))

if userInput > RandomNumber :
    print("The number is",RandomNumber)
    print("Your number is high..FUCK YOU")
elif RandomNumber > userInput:
    print("The number is",RandomNumber)
    print("Your number is low..FUCK YOU")
else:
    print("Congratulations")