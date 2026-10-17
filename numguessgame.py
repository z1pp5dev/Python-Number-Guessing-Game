import random #---Imports the random library
def check_guess(guess, secret_number): #---- Defines a custom function to check the players guess
    if guess == secret_number: #---- Conditionals to determine if player is correct or incorrect
        print("Congratulations! You guessed the number correctly.")
        return "correct"
    elif guess < secret_number:
        print("Too Low!, Try Again.")
        return "low"
    elif guess > secret_number:
        print("Too High!, Try Again.")
        return "high"

secret_number = random.randint(1, 100) #--- Defines the range of numbers to choose from
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True: #---Loops the main function untill player guesses correctly
    guess = int(input("Enter your guess: "))

    result = check_guess(guess, secret_number)

    if result == "correct":
     print("Congrats You Got It Right!")
     break
    elif result == "low":
        print("Good try, but too low!")
    elif result == "high":
        print("Good try, but too high!")