# I added drinks appetizers and a tip percentage

# Getting the data from the user
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
num_of_children = int(input('How many children are there? '))
num_of_adult = int(input('How many adults are there? '))

# Drinks and Appetizers 
drinks = float(input('What is the price of the drink? '))
appetizer = float(input('What is the price of the appetizer? '))

num_of_person_drinks = int(input('How many persons are getting the drinks?' ))
num_of_person_appetizer = int(input('How many persons are getting the appetizers?' ))


# Getting the price of each meal
children_meal_price = num_of_children * child_meal
adult_meal_price = num_of_adult * adult_meal
meal_total = children_meal_price + adult_meal_price


# Drink and Appetizer Total
drink_total = num_of_person_drinks * drinks
appetizer_total = num_of_person_appetizer * appetizer
sides_attractions = drink_total + appetizer_total


# Adding the values together to determine subtotal
meal_subtotal = meal_total + sides_attractions

print(f'This is the subtotal of the meal ordered: ${meal_subtotal: .2f}')

# SALES TAX
tax_rate = float(input('What is the sales tax rate? '))

# Subtotal with tax inclusive
sub_total_with_tax = (meal_subtotal * tax_rate) / 100
sales_tax = sub_total_with_tax
print(f'Sales tax is ${sales_tax: .2f}')


total_meal_price = meal_subtotal + sales_tax

# TIP CALCULATION at 2% of total cost
tip_percent = 2
tip_decimal = (tip_percent / 100)
tip_amount =  total_meal_price * tip_decimal

print(f'Tip is ${tip_amount: .2f}')

# Adding the tax and the tip to the subtotal to get the total
total_meal_price = total_meal_price + tip_amount
print(f'This is the Total of the meal ordered: ${total_meal_price: .2f}')



# Payment amount validation
payment_amount = float(input('What is the payment amount? '))

change = payment_amount - total_meal_price

print(f'Your Change is ${change: .2f}')