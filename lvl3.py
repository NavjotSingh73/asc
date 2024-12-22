import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000.")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 1000)
    attempts = 0

    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 1000:
                print("Please enter a number between 1 and 1000.")
                continue

            # Compare the guess to the target number
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
