import random

secret_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        
        guess = int(input("Enter your guess: "))

        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("You got it! 🎉")
            break

    except ValueError:
        
        print("Please enter a valid number.")
