'''
WHILE LOOP

'''


# tip = float(input('What is the tip amount? '))

# while tip < 0:
#     print('Sorry, Tip can not be a negative')
#     tip = float(input('What is the tip amount? '))

# print(f'YOu have tipped ${tip: .2f} amount')

# number = 0
# while number < 10:
#     number = int(input('What is the number? '))

# print('Finished with the loop')

# number = 1

# # Keep looping as long as the number is less than or equal to 5
# while number <= 5:
#     # Display the number
#     print(f'The Number is {number}')
#     # Update the number to be one more than it was
#     number += 1   


# number = int(input('Please type in a positive number '))

# while number < 0:
#     print(f'Sorry, that is a negative number. Please try again' )
#     number = int(input('Please type in a positive number '))
    
    
# print(f'You have entered a positive number {number}')


# candy_request = input('May I have a piece of candy? ').lower()

# while candy_request == 'no':
#     candy_request = input('May I have a piece of candy? ')
#     if candy_request == 'yes':
#         print('Thank you')

# while candy_request != "yes":
#     candy_request = input('May I have a piece of candy? ').lower()

# print('Thank you')


'''
FOR LOOP

'''

# items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

# for item in items:
#     print(f'The item is: {item}')


# numbers = range(10)
# for each_num in numbers:
#     print(f'The number is: {each_num}')

# for each_num in range (10):
#     print(f'The number is: {each_num}')


# for number in range(100, 200, 10):
#     print(f'{number}')

# for i in range(5):
#     print(i)
#     for j in range(10, 13):
#         print(f'--{j}')
'''
Notice how the inner loop is run every time 
the outer loop displays it's number.
Inner loops can be very helpful in iterating through a 
two-dimensional structure, such as the pixels in an image.

'''

# colors = ["red", "blue", "green", "yellow"]
# for color in colors:
#     print(f'{color}')

# for i in range(1, 9):
#     print(f'{i}')

# for i in range(2, 21, 2):
#     print(f'{i}')

# first_name = "HEAVEN"
# for letter in first_name:
#     print(f'The letter is: {letter} ')

# fourth_letter = first_name[3]
# print(fourth_letter)

# word = "book"
# number_of_letters = 4

# for index in range(number_of_letters):
#     print(f'The letter at index {index} is: {word[index]}')


# word = "book"
# number_of_letters = len(word)

# for index in range(number_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")


# dog_name = input('What is your dog name? ')
# letter_count = len(dog_name)

# print(f'Your name has {letter_count} letters')



'''
Enumerate 
This is a little different than the standard for loop, 
because it returns two variables.

'''
# first_name = "Brigham"

# Notice by using enumerate, we specify both i and letter

# for i, letter in enumerate(first_name):
    # print(f"The letter {letter} is at position {i}")


# programmed_word = "Commitment and Perseverance"
# favorite_letter = input('What is your favorite letter? ').upper()

# for letter in programmed_word:
#     if letter.lower() == favorite_letter.lower():
#         print(letter.upper(), end='')
#     else:
#         print(letter.lower(), end='')
# print()
# for letter in programmed_word:
#     if letter.lower() == favorite_letter.lower():
#         print("_", end='')
#     else:
#         print(letter.lower(), end='')
# print()

value = 20
while value < 20:
   value = value + 1
print(value)