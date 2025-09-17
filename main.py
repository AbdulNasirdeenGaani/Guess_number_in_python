# imports
import random
# title
print("=== Number Guess Game ===")

# variables
secret_number = random.randint(1, 10)
attempts = 5
max_attempts = 5
print(secret_number)

while attempts > 0:
    guess_number = int(input("Please enter your guess: "))
    attempts -= 1

    if secret_number == guess_number:
        print("Wow your guess is right")
        print(f"You guess at attempt {max_attempts - attempts}")
        break
    else:
        if attempts == 0:
            print("you are done \nNo more chances for you! \nRestart the game again \nAnd try all your might")
        else:
            if secret_number > guess_number:
                print("Low")
            else:
                print("High")
            print(f"You are left with {attempts} attempts")
