# implementing a function that picks a or an automatically based on the word starting letter.
def word_search(word):
#This converts all the words to lower case and checks if the word starts with the A E I O U then it uses 'an' else it uses 'a' 
     return 'an' if word.lower().startswith(('a', 'e', 'i', 'o', 'u')) else 'a'

# This program takes user input to complete a story. The exclamation is automatically capitalized.
adjective = input('Type in an Adjective')
animal = input('Type in the name of an animal')
verb_1= input('Type in a verb')
exclamation= input('Type in an exclamation').capitalize()
verb_2 = input('Type in a verb')
verb_3 = input('Type in a verb')

#Additional Input
noun = input("Enter a noun: ")
place = input("Enter a place: ") 

# Use 'a' or 'an' based on the animal and noun
word_search_noun = word_search(noun)

#Mad Libs output
clever_story = f""" 
The other day, I was really in trouble.
It all started when I saw a very {adjective} {animal} {verb_1} down the hallway. 
"{exclamation}!" I yelled, But all I could think to do was to {verb_2} over and over. 
Miraculously, that caused it to stop, but not before it tried to {verb_3} right in front of my family.
Then I found {word_search_noun} {noun} at {place}, making the day even more strange.
"""

print()
print('Your Story is:')
# Outputs the Mad Libs story with the user's input.
print(clever_story)  