'''
from datetime import datetime


# Function to print current date and time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Heaven'
print_time('Printed First Name')


for x in range(0, 10):
    print(x)
print_time('Loop Completed')
'''


def get_initials(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

# Using named notation in calling functions
first_name_initial = get_initials(name= first_name, force_uppercase = True)
last_name_initial = get_initials(name= last_name, force_uppercase = False)


print ('Your initial is: ' + first_name_initial + last_name_initial)
