# Secret word to guess
secret_word = "heaven"

# Initialize the number of guesses
guess_count = 0

while True:
    guessed_word = input("What is your guess? ")

    # Keeping counts of how many times the user tried to guess the word
    guess_count += 1

    # Check if the guess is correct
    if guessed_word.lower() == secret_word:
        print("Congratulations! You've guessed it ")
        print(f'it took you {guess_count} guesses.')
        break
    else:
        print("Your guess was not correct.")