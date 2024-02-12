import random

# Set up options
options = ["Rock", "Paper", "Scissors"]

# Start the game loop
while True:
  # Get user input
  user_choice = input("Rock, Paper, or Scissors? (or 'q' to quit): ").lower()

  # Check for quit
  if user_choice == 'q':
    break

  # Validate user input
  if user_choice not in options:
    print("Invalid choice. Please try again.")
    continue

  # Get computer choice
  computer_choice = random.choice(options)

  # Print choices
  print("You chose:", user_choice)
  print("Computer chose:", computer_choice)

  # Determine winner
  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
  else:
    print("You lose.")

  # Ask to play again
  play_again = input("Play again? (y/n): ").lower()
  if play_again != 'y':
    break

print("Thanks for playing!")
