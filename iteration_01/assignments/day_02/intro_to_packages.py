"""
Python Lab Activity: Packages, Documentation, and a Complex Number Guesser Game

Objective:
- Practice importing and using Python packages
- Learn how to read and explore package documentation
- Use input, loops, and conditionals
- Build a Complex Number Guesser Game

Instructions:
Work through each level in order. Follow the comments, read documentation
with help(), and fill in the TODOs. Test your code after each level.
"""

# ---------------------------------------------------
# Level 1 – Importing a Package
# Task:
# 1. Import the `random` module
# 2. Use help(random) to explore documentation
# 3. Print 3 random integers between 1 and 10
# ---------------------------------------------------

import random
# TODO: Generate and print 3 random integers between 1 and 10
#for _ in range(1,4):
   # print(random.randint(1, 10))

# ---------------------------------------------------
# Level 2 – Complex Numbers with cmath
# Task:
# 1. Import `cmath`
# 2. Use help(cmath) to explore its functions
# 3. Compute and print the square root of -1
# ---------------------------------------------------

import cmath
# TODO: Print the square root of -1 using cmath
#sqrt_neg1 = cmath.sqrt(-1)
#print(sqrt_neg1)

# ---------------------------------------------------
# Level 3 – User Input Basics
# Task:
# 1. Ask the user to type their name
# 2. Print a welcome message
# ---------------------------------------------------

# TODO: Ask for the user’s name and print a greeting
#name = input("Please enter your name: ")
#print(f"Hello, {name}! Welcome to the Python Lab!")

# ---------------------------------------------------
# Level 4 – Converting Input to Numbers
# Task:
# 1. Ask the user to enter a number
# 2. Convert it to an integer
# 3. Multiply it by 2 and print the result
# ---------------------------------------------------

# TODO: Ask for a number, convert it to int, double it, and print
#num = input("Please enter a number: ")
#num = int(num)
#result = num * 2
#print(f"The result is: {result}")

# ---------------------------------------------------
# Level 5 – Random Complex Numbers
# Task:
# 1. Generate a random integer (-10 to 10) for the real part
# 2. Generate a random integer (-10 to 10) for the imaginary part
# 3. Construct a complex number and print it
# ---------------------------------------------------

# TODO: Generate a random complex number with integer real and imaginary parts
#randreal = random.randint(-10, 10)
#randimag = random.randint(-10, 10)
#randcomplex = complex(randreal, randimag)
#print(randcomplex)

# ---------------------------------------------------
# Level 6 – Complex Number Guesser Game
# Rules:
# 1. Computer picks a random complex number (real and imaginary parts between -5 and 5)
# 2. User must guess both parts correctly
# 3. After each guess, provide feedback:
#    - "Too high" or "Too low" for each part
#    - If both are correct, the game ends
# 4. Repeat until correct
# ---------------------------------------------------

target_real = random.randint(-5, 5)
target_imag = random.randint(-5, 5)
target = complex(target_real, target_imag)

print("Welcome to the Complex Number Guesser Game!")
print("I have chosen a complex number with real and imaginary parts between -5 and 5.")

# TODO: Write a loop where the user keeps guessing until correct
# Hints:
# - Ask separately for real and imaginary guesses
# - Convert inputs to integers
# - Use if/else to give “too high” / “too low” feedback
# - Use a while loop to repeat until correct
while True:
    guess_real = int(input("Guess the real part: "))
    guess_imag = int(input("Guess the imaginary part: "))
    guess = complex(guess_real, guess_imag)

    if guess == target:
        print("Congratulations! You guessed correctly.")
        break
    else:
        if guess_real < target_real:
            print("Too low for the real part.")
        elif guess_real > target_real:
            print("Too high for the real part.")
        if guess_imag < target_imag:
            print("Too low for the imaginary part.")
        elif guess_imag > target_imag:
            print("Too high for the imaginary part.")

# ---------------------------------------------------
# Extensions (Optional)
# - Limit the number of guesses
# - Give hints about magnitude (abs(z)) or angle (cmath.phase(z))
# - Let the user guess in the format "a+bj" and parse it as complex
# ---------------------------------------------------