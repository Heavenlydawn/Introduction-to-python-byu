"""
Author: Brother Burton

Purpose: Display text to the screen.
"""

# color = input('What is your favorite color? ')
# print('Your favorite color is')
# print(color)

# Please note that you can use either single quotes: 'Your favorite color is' or double
# quotes: "Your favorite color is" in your print and inputs statements and it will work
# just fine. It is completely a programmer preference.

# Lines that start with a "#" like this one are called "comments" and don't have
# code that actually runs. Instead, they allow us to make notes in our programs
# for other programmers to see.

"""
For large blocks of comments, we can start them with three "'s.
then we can type many lines of comments, and finish with three more "'s.
These are a special kind of comment that you'll learn more about later on.
"""


first_name = input('What is your first name?')
last_name = input('What is your last name?')

output = 'Your name is {1}, {0} {1}.' .format(first_name, last_name)
print(output.title())