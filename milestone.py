# Getting the data from the user
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
num_of_children = int(input('How many children? '))
num_of_adult = int(input('How many adults? '))


# Getting the price of each meal
children_meal_price = num_of_children * child_meal
adult_meal_price = num_of_adult * adult_meal


# Adding the values together to determine subtotal
meal_subtotal = children_meal_price + adult_meal_price

print(f'This is the subtotal of the meal ordered: {meal_subtotal: .2f}')
