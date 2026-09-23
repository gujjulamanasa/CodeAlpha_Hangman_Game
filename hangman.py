import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "software"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print()

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with guessed letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print()
        print("Congratulations!")
        print("You guessed the word:", word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        print()
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check whether guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    print()

# If player uses all six wrong guesses
if wrong_guesses == max_wrong_guesses:
    print("Game Over!")
    print("The correct word was:", word)