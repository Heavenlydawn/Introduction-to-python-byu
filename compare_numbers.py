first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

if first_number > second_number:
    print(f'The first number is greater')
elif first_number < second_number:
    print(f'The first number is not greater')
if first_number == second_number:
    print(f'The two numbers are equal')
elif first_number != second_number:
    print(f'The numbers are not equal')
if second_number > first_number:
    print(f'The second number is greater')
elif second_number < first_number:
    print(f'The second number is not greater')