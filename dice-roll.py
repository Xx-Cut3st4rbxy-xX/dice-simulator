from random import randint
from time import sleep
def fate():
    loop = 0
    while not loop == 1:
        print("Generating your number...")
        fate = randint(1, 6)
        sleep(2)
        print("Your number is: ", fate)
        print("Do you want me to do it again? (yes/no)")
        answer2 = input()
        if answer2 == 'no' or answer2 == 'No':
            loop = 1
print("Hello! Welcome to Dice Simulator!")
sleep(2)
print("If you want to proceed, enter 'yes' or 'Yes'")
answer = input()
if answer == "yes" or answer == "Yes":
    fate()
