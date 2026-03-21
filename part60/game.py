import random

def play_game():
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("Select Difficulty Level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        attempts = 10
        level = "Easy"
    elif choice == "2":
        attempts = 7
        level = "Medium"
    elif choice == "3":
        attempts = 5
        level = "Hard"
    else:
        print("Invalid choice! Defaulting to Easy.")
        attempts = 10
        level = "Easy"

    number = random.randint(1, 100)
    score = 0

    print(f"\nYou selected {level} level.")
    print("Guess the number between 1 and 100")

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            score = attempts * 10
            print("\n🎉 Congratulations! You guessed the number!")
            print("Your Score:", score)
            return

        attempts -= 1

    print("\n❌ Game Over!")
    print("The correct number was:", number)


# Main program loop for replay
while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! 👋")
        break