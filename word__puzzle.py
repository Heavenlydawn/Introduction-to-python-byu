'''
I used the random library
I saved some words in a list for every time the user plays the word puzzle game the word is different 
I limited the amount of times the user can try to guess the word before game is over

'''

import random

# List of possible secret words
secret_words = ["heaven", "temple", "bishop", "alma", "celestial", "covenant"]

# Select a random word from the list
secret_word = random.choice(secret_words)

# Initializing the number of guesses and limiting the number of allowed guesses
guess_count = 0
max_guesses = 7

print("Welcome to the Word Guessing Game!")
print("The secret word has the following letters:")

# Display initial hint
for _ in range(len(secret_word)):
    print("_", end=" ")
print("\n")

# Loop until the user guesses correctly or runs out of the maximum attempts
while guess_count < max_guesses:
    guessed_word = input("What is your guess? ").lower()
    
    # Increment the guess count for every attempt, regardless of length
    guess_count += 1
    
    # Checking if the guessed word has the correct length
    if len(guessed_word) != len(secret_word):
        print(f"Sorry, the guess must be {len(secret_word)} letters long.")
        remaining_attempts = max_guesses - guess_count
        print(f"Incorrect guess length. You have {remaining_attempts} attempts left.\n")
        continue
    
    # Initializing a hint for this guess
    hint = []
    
    # Generating hints
    for i in range(len(secret_word)):
        if guessed_word[i] == secret_word[i]:
            # Correct letter and position
            hint.append(guessed_word[i].upper())  
        elif guessed_word[i] in secret_word:
            # Correct letter, wrong position
            hint.append(guessed_word[i].lower())  
        else:
            # Letter not in the word at all
            hint.append('_')  
    
    # Display the hint
    hint_letter = ''.join(hint)
    print(f"Hint: {hint_letter}")
    
    # Check if the guess is correct
    if guessed_word == secret_word:
        print("Congratulations! You've guessed it!")
        print(f'It took you {guess_count} guesses.')
        break
    else:
        remaining_attempts = max_guesses - guess_count
        print(f"Incorrect guess. You have {remaining_attempts} attempts left.\n")

# If max guess is exhausted.
if guess_count == max_guesses:
    print(f"Sorry, you've reached the maximum number of guesses. The secret word was '{secret_word}'.")