
import random

def main():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        attempts = 0

        print("\nI have chosen a number between 1 and 100. Can you guess it?")

        while True:
            try:
                # Take user input
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
