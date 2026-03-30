import random

number = random.randint(1, 1001)

# print(number)

attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 1000: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        break