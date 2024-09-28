# price = float(input('How much did you pay? '))
# if price >= 1.00:
#         tax = .07
# else:
#         tax = 0
# print(f'Tax rate is: {tax}')

country = input('What country do you live in? ')
tax = 0


'''
USING THE IN FUNCTION
'''

if country.lower() == 'Canada':
    province = input('What province / state do you live in? ')
    if province.lower() in('Alberta', \
        'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0


print(f'Your Tax rate is {tax}')



'''
USING THE OR FUNCTION
'''