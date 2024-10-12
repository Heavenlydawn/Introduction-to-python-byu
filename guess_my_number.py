import random
# guessed_number = -1
# magic_number = random.randint(1 , 100)

# while guessed_number != magic_number:
#     guessed_number = int(input('What is the Magic Number? '))
#     if guessed_number < magic_number:
#         print('Higher')
#     elif guessed_number > magic_number:
#         print('Lower')
#     else:
#         print('You guessed it!')

keep_playing = "yes"

while keep_playing == 'yes':
    magic_number = random.randint(1, 100)
    
    # Keeping counts of how many times the user tried to guess the number
    guess_count = 0
    
    guessed_number = -1
    while guessed_number != magic_number:
        guessed_number = int(input('What is the Magic Number? '))
        guess_count = guess_count + 1
        if guessed_number < magic_number:
            print('Higher')
        elif guessed_number > magic_number:
            print('Lower')
        else:
            print('You guessed it!')
    print(f"It took you {guess_count} guesses")

    keep_playing = input('Would you like to play agin (yes/no)? ')
print('Thank you for playing. Goodbye!. ')