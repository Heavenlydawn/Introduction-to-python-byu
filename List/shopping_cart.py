# print('Welcome to the Shopping Cart Program!')



# shopping_cart = []

# products = []
# prices = []

# # total_sum = 0

# while True:
#     print()
#     print('Please select one of the following:')
#     print('1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit')
#     action = int(input('Please enter an action '))

#     if action == 5:
#         break

#     elif action == 1:
#         product = input('What item would you like to add? ')
#         price = float(input('Enter product price: '))
#         shopping_cart.append(product)
#         products.append(product)
#         prices.append(price)
#         print(f" '{product}' has been added to cart")
      

#     elif action == 2:
#         print('The contents of the shopping cart are: ') 
#         for i in range(len(shopping_cart)):
#             print(f'{i}. {shopping_cart[i]}')

#     elif action == 3:
#         print('The contents of the shopping cart are: ') 
#         for i in range(len(shopping_cart)):
#             print(f'{i}. {shopping_cart[i]}')
#         print()
#         removed_item = int(input('Which item would you like to remove?'))
#         if 0 <= removed_item < len(shopping_cart):
#             shopping_cart.pop(removed_item)
#             prices.pop(removed_item)  # Ensure prices list stays in sync
#             print('Item Removed')
#         else:
#             print("Invalid selection. Please try again.")
#     elif action == 4:
#         total_sum = sum(prices)
#         print(f'The total price of the items in the shopping cart is: ${total_sum:.2f}')
    
#     else:
#         print("Invalid action. Please select a number between 1 and 5.")

