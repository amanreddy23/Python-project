
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Generator!")

    while True:
        # Roll the dice
        input("Press Enter to roll the dice...")
        dice_result = roll_dice()
        print(f"You rolled a {dice_result}!")

        # Ask if the user wants to roll again
        roll_again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if roll_again != 'yes':
            print("Thank you for using the Dice Rolling Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
