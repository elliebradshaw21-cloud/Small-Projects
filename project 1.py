import random

def play():
    secret = random.randint(1, 20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts.")
            break

play()