print('Enter a list of numbers, type 0 when finished.')

number_list = []

while True:
    number = int(input("Enter number: "))
    if number == 0:
        break
    number_list.append(number)
print()


'''
===============
Finding the SUM
===============
'''

total_sum = 0
for number in number_list:
    total_sum += number
print(f'The sum is: {total_sum}' )

'''
==============================================
Getting the AVERAGE of the numbers in the list
==============================================
'''
count = len(number_list)

average = total_sum / count
print(f"The average is: {average:.3f}")
print()





'''
==========================
Finding the LARGEST number
==========================
'''
largest_number = -1

for number in number_list:
    if number > largest_number:
        largest_number = number
print(f'The largest number is: {largest_number}')





'''
=============================================
Finding the SMALLEST positive number 
(the positive number that is closest to zero)
=============================================
'''
# We need to start with something large
smallest_so_far = 99999999999

for number in number_list:
    if number > 0 and number < smallest_so_far:
        # We have a new smallest number
        smallest_so_far = number
print(f"The smallest positive number is: {smallest_so_far}")



'''
===================
SORTING the numbers
===================
'''
sorted_list = sorted(number_list)
print('The Sorted List is:')
for number in sorted_list:
    print(number)