# ============================================
# Hangman Game
# Author: Internship Project
# Description: A simple hangman game where
# the player guesses letters to find the word
# ============================================

import random

# --- List of words the game can pick from ---
word_list = ["python", "keyboard", "monitor", "science", "football"]

# --- Randomly pick one word from the list ---
secret_word = random.choice(word_list)

# --- Create a list of underscores to represent hidden letters ---
# For example, if the word is "python", this becomes ['_', '_', '_', '_', '_', '_']
guessed_word = []
for letter in secret_word:
    guessed_word.append("_")

# --- Set up the game variables ---
wrong_guesses = 0         # counts how many wrong guesses the player has made
max_wrong = 6             # player is allowed 6 wrong guesses before losing
guessed_letters = []      # keeps track of all letters the player has tried

print("==================================")
print("   Welcome to the Hangman Game!   ")
print("==================================")
print("Try to guess the word letter by letter.")
print("You have 6 incorrect guesses before you lose.")
print()

# --- Main game loop ---
# The game keeps going as long as the player hasn't used all wrong guesses
# and hasn't fully guessed the word yet
while wrong_guesses < max_wrong and "_" in guessed_word:

    # Show how many attempts are left
    attempts_left = max_wrong - wrong_guesses
    print("Attempts remaining:", attempts_left)

    # Show the current progress of the word (e.g. p _ t h _ n)
    print("Word so far:", " ".join(guessed_word))

    # Show which letters the player has already tried
    print("Letters you guessed:", guessed_letters)
    print()

    # --- Ask the player to enter a letter ---
    guess = input("Guess a letter: ")

    # Make the letter lowercase so it works even if player types uppercase
    guess = guess.lower()

    print()

    # --- Check if the player entered exactly one letter ---
    if len(guess) != 1:
        print("Please enter only one letter at a time!")
        print()
        continue   # skip the rest and ask again

    # --- Check if the player already guessed this letter ---
    if guess in guessed_letters:
        print("You already tried the letter '" + guess + "'. Try a different one!")
        print()
        continue   # skip the rest and ask again

    # --- Add the guessed letter to the list of tried letters ---
    guessed_letters.append(guess)

    # --- Check if the guessed letter is in the secret word ---
    if guess in secret_word:
        print("Good guess! '" + guess + "' is in the word.")

        # Go through each position in the word and reveal matching letters
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess   # replace underscore with the correct letter

    else:
        # The letter is not in the word, so count it as a wrong guess
        wrong_guesses = wrong_guesses + 1
        print("Oops! '" + guess + "' is NOT in the word.")
        print("Wrong guesses so far:", wrong_guesses)

    print()

# -----------------------------------------------
# --- Game Over: Check if the player won or lost ---
# -----------------------------------------------

# If there are no more underscores, the player guessed the full word
if "_" not in guessed_word:
    print("==================================")
    print("  Congratulations! You WON!  ")
    print("  The word was:", secret_word)
    print("==================================")

# Otherwise, the player ran out of attempts
else:
    print("==================================")
    print("  Game Over! You LOST.")
    print("  The word was:", secret_word)
    print("==================================")
