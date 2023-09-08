import random


name = input("Tell your name.. ")
print(f"\nHello, {name}!")
print("I have got a random number between 1 to 100. make a guess!\n")
target = random.randint(1, 100)
guesses = 0
guessed_it = False

while guesses < 10 and not guessed_it:
    print(f"{10 - guesses} guesses left")
    guess = input("Make a guess: ")

    if guess.isdigit():
        guess=int(guess)
    else:
        print("It is not a number! Enter a number next time.")
        quit()

    guesses += 1

    if guess < target:
        print("Your guess is LOW")
    elif guess > target:
        print("Your guess is HIGH")
    elif guess == target:
        print(f"\nGood Job, {name}!")
        print(f"You guessed the number in  {guesses} guess!")
        guessed_it = True

if not guessed_it:
    print(f"You didn't get my number. It was {target}.")

