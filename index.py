# name = input('What is your name?')
# print('Hello')
# print(name)


# print('Adding Numbers')
# x = 200 * 2
# print('Dividing Numbers')
# y = x / 100




# first_name = input ('Please Enter Your First Name')
# last_name = input ('Please Enter Your Last Name')
# print(first_name + last_name)
# print ('Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize())
# print(f'Hello, {first_name} {last_name}')


# first_name = 'Heaven'
# last_name = 'Gabriel'

# # output = 'Hello, ' + first_name + ' ' + last_name
# # output = 'Hello, {} {}'.format(first_name, last_name)
# # output = 'Hello, {0} {1}'.format(first_name, last_name)
# output = f'Hello, {first_name} {last_name}'
# print(output)

# quantity = input('Please type in how many items you have')

# double_quantity = int(quantity) * 2
# print(f'You have {double_quantity} items')


# Function to calculate tip
def calculate_tip(total_cost, tip_percentage=2):
    # Convert the tip percentage to a decimal (e.g., 2% -> 0.02)
    tip_decimal = tip_percentage / 100
    # Calculate the tip amount
    tip_amount = total_cost * tip_decimal
    # Return the tip amount
    return tip_amount

# Example usage
total_cost = 100  # Total cost of the service
tip = calculate_tip(total_cost)
print(f"Tip amount: ${tip:.2f}")
