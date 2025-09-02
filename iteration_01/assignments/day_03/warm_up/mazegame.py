import random

### Starting Conditions
#- Player begins with **10 energy points**.
#- The game continues as long as **energy > 0** and ends when:
 # - Energy reaches **20** → Player escapes and wins
  #- Energy drops to **0** → Player loses

#---

### Actions Per Turn
#1. **Move**
 #  - Try to move through the maze.
  # - Random outcomes:
     #- 50% chance: lose 2 energy
    # - 30% chance: nothing happens
   #  - 20% chance: find food, gain 3 energy

#2. **Rest**
#   - Stay in place and regain **2 energy**.
#   - Always succeeds but wastes a turn.

#3. **Guess**
#   - Program generates a random number between 1 and 5.
#   - Player guesses the number:
#     - Correct guess → gain 5 energy
#     - Wrong guess → lose 2 energy

#4. **Invalid input**
 #  - If the player enters an invalid action, they lose 1 energy.

 # - The game continues as normal.
#---

def main():
    # Initialize the player's energy and position
    energy = 10
    position = 0

    # Game loop
    while energy > 0:
        # Display the current state of the game
        print(f"You are at position {position}. You have {energy} energy.")

        # Get the player's action
        action = input("What would you like to do? (move, rest, guess, quit): ").lower()

        # Handle the player's action
        if action == "move":
            # Move the player
            move_result = random.choices(["lose 2 energy", "nothing happens", "find food"], weights=[0.5, 0.3, 0.2])[0]
            if move_result == "lose 2 energy":
                energy -= 2
                print("You stumbled and lost 2 energy!")
            elif move_result == "nothing happens":
                print("You moved forward safely.")
            elif move_result == "find food":
                print("You found food!")
                energy += 3

            # Move the player forward
            position += 1

        elif action == "rest":
            # Rest: gain 2 energy
            energy += 2
            print("You rested and gained 2 energy.")

        elif action == "guess":
            # Guess a number between 1 and 5
            try:
                guess = int(input("Guess a number between 1 and 5: "))
                target = random.randint(1, 5)
                if guess == target:
                    energy += 5
                    print(f"Correct! The number was {target}. You gained 5 energy!")
                else:
                    energy -= 2
                    print(f"Wrong! The number was {target}. You lost 2 energy.")
            except ValueError:
                print("Invalid input. You lose 1 energy.")
                energy -= 1

        elif action == "quit":
            # Quit the game
            print("Thanks for playing!")
            break

        else:
            # Invalid action
            print("Invalid action. You lose 1 energy.")
            energy -= 1

        # Check if the player has won or lost
        if energy >= 20:
            print("Congratulations! You have enough energy to escape the maze and won!")
            break
        elif energy <= 0:
            print("Game over! You ran out of energy.")
            break

if __name__ == "__main__":
    main()
