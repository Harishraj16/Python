import random

name=input("tell your name... ")
print(f"\nhello,{name}!")
print("Welcome to Stone/Paper/Scissor")

USER_SCORE = 0
COMPUTER_SCORE = 0

options=["rock","paper","scissor"]

while True:
    user_input = input("Type Stone/Paper/Scissor or Q to quit: ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    computer_input = options[random_number]
    
    if user_input == "stone" and computer_input == "scissor":
        print("You won!")
        USER_SCORE += 1
        
    elif user_input == "scissor" and computer_input == "paper":
        print("You won!")
        USER_SCORE += 1
        
    elif user_input == "paper" and computer_input == "stone":
        print("You won!")
        USER_SCORE += 1
        
    else:
        print("Computer Won!")
        COMPUTER_SCORE += 1
        

print("You won", USER_SCORE , "times.")


    