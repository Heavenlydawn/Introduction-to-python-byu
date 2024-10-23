# item quantities
# formatted  output for better readability.
# Each item has a quantity, which is stored and displayed alongside the item names and prices.

print('Welcome to the Shopping Cart Program!')

shopping_cart = []
prices = []
quantities = []

while True:
    print()
    print('Please select one of the following:')
    print('1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit')
    action = int(input('Please enter an action: '))

    if action == 5:
        break

    elif action == 1:
        product = input('What item would you like to add? ')
        price = float(input('Enter product price: '))
        quantity = int(input('Enter quantity: '))
        shopping_cart.append(product)
        prices.append(price)
        quantities.append(quantity)
        print(f"'{product}' has been added to cart with a price of ${price:.2f}.")

    elif action == 2:
        print('\nThe contents of the shopping cart are:')
        
        # Formatting the header
        print(f"{'Item':<20} {'Price':<10} {'Quantity':<10}")
        print('-' * 40)
        for i in range(len(shopping_cart)):
            # Displaying items starting from number 1
            print(f"{i + 1}. {shopping_cart[i]:<20} ${prices[i]:<9.2f} {quantities[i]:<10}")

    elif action == 3:
        print('\nThe contents of the shopping cart are:')
        for i in range(len(shopping_cart)):
            # Displaying items starting from number 1
            print(f'{i + 1}. {shopping_cart[i]} - ${prices[i]:.2f} (Qty: {quantities[i]})')
        removed_item = int(input('Which item would you like to remove (enter the number)? '))
        
        # Check if the input is valid
        if 1 <= removed_item <= len(shopping_cart):
            index_to_remove = removed_item - 1  # Convert to 0-based index
            removed_product = shopping_cart.pop(index_to_remove)
            removed_price = prices.pop(index_to_remove)
            removed_quantity = quantities.pop(index_to_remove)
            print(f'Item "{removed_product}" priced at ${removed_price:.2f} with quantity {removed_quantity} has been removed.')
        else:
            print("Invalid selection. Please try again.")

    elif action == 4:
        total_sum = sum(prices[i] * quantities[i] for i in range(len(prices)))
        print(f'The total price of the items in the shopping cart is: ${total_sum:.2f}')

    else:
        print("Invalid action. Please select a number between 1 and 5.")

print('Thank you for using the Shopping Cart Program!')