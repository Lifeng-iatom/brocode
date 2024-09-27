# Python number guessing game
import random

low_number = 1
high_number = 100
answer = random.randint(low_number, high_number)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low_number} and {high_number}")

while is_running:
      guess = input("Enter your guess: ")
      if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < low_number or guess > high_number:
                  print("That number is out of range")
                  print(f"Please select a number between {low_number} and {high_number}")
            elif guess < answer:
                  print("Too low! Try again!")
            elif guess > answer:
                  print("Too high! Try again!")
            else:
                  print(f"CORRECT! The answer was {answer}")
                  print(f"Number of guesses: {guesses}")
                  is_running = False
      else:
            print("Invalid guess")
            print(f"Please select a number between {low_number} and {high_number}")