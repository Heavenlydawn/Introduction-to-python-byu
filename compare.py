first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

if first_number > second_number:
    print(f'The first number is greater')
else:
    print(f'The first number is not greater')
if first_number == second_number:
    print(f'The numbers are equal')
else:
    print(f'The numbers are not equal')
if second_number > first_number:
    print(f'The second number is greater')
else:
    print(f'The second number is not greater')

print()

favorite_animal = input('What is your favorite animal? ')

my_favorite_animal = 'Dove'

if favorite_animal.lower() == my_favorite_animal.lower():
    print("That's my favorite animal too")
else:
    print('That one is not my favorite')