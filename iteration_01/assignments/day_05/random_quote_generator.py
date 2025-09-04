# Starter file for students to create a Random Quote Generator

# Step 1: Import any necessary modules
# Step 2: Define a function to load quotes from a file when called
# Step 3: Define a function that returns a random quote when called
# Step 4: Define a main function that runs the program. Make sure to call the function.

from pathlib import Path
import random

BASE_DIR = Path(__file__).parent
quotes_path = BASE_DIR / "quotes.txt"


# Functions takes in filename parameter and returns list of strings with lines from file
def load_quotes(filename):
    with open (filename, 'r') as file:
        quotes = file.readlines()
        quotes = [quote.strip("\n") for quote in quotes]
    return quotes

# Function takes in list of strings and randomly chooses one to return
def get_random_quote(quotes):
    return random.choice(quotes)

# Runs program. Main() is the only function called so that it calls the other functions appropriately and controls logic flow.
def main():
    quotes = load_quotes(quotes_path)
    while True: 
        user_input = input("Enter Quote to get a random quote, enter Exit to exit.")
        if user_input == "Exit":
            break
        elif user_input == "Quote":
                random_quote = get_random_quote(quotes)
                print(random_quote)
        else :
            print("Invalid input. Please enter 'Quote' or 'Exit'.")
    return None

main()