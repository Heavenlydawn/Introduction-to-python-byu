# clients = ["Heaven", "Ozioma", "Gabriel"]
# print(clients) 

# for client in clients:
#     print(client)  # prints each client on a new line



# clients = []

# new_client = ''
# while new_client != "quit":
#     new_client = input('What is the name of the client? ')
#     clients.append(new_client)

# for client in  clients:
#     print(client)

'''
================================================
Declare a variable outside a loop that you can 
reference in the loop as you iterate through each individual item.
=================================================

'''

# tips = [12.25, 13.95, 8.50]

# running_total = 0

# for tip in tips:
#     running_total += tip

# print(f'Your tip total is ${running_total:.2f}')


# friend_list = []

# friends = None
# # friends = ''

# while friends != "end":
#     friends = input('What is the name of your friend? ')
#     if friends != "end":
#         friend_list.append(friends)
# print()
# print('Your friends are: ')

# for friend in friend_list:
#     print(friend)




'''
=========================================================
Looking a little closer at that for loop 
you can see that len(books) gets the number of items 
in the list, and then the for i in range(...): 
part iterates through the numbers 0, 1, 2, 3, ..., 
up until (but not including) the size of the list.
==========================================================

'''
# books = ['Lord of the rings', 'Dunes', 'Love is a decision', 'Four seasons of marriage']
# for i in range(len(books)):
#     book = books[i]
#     print(f'{i + 1}. {book}')


# names = ['Heaven', 'Gabriel']
# numbers = [7088808842, 9034969138]

# for i in range(len(names)):
#     name = names[i]
#     number = numbers[i]

#     print(f"{name} - {number}")

print('Please enter the items of the shopping list (type quit to finish) ')
shopping_list = []

items = " "

while items != 'quit':
    items = input('Item: ')
    if items != "quit":
        shopping_list.append(items)
        

print()
print('The shopping list is: ')
for item in shopping_list:
    print(item)

print()
print('The shopping list with indexes is:')
for item in range(len(shopping_list)):
    print(f'{item}. {shopping_list[item]}')
    print(end='')

changed_item = int(input('What item would you like to change? '))

new_item = input('What is the new item? ')

shopping_list[changed_item] = new_item

print()
print('The shopping list with indexes is:')

for item in range(len(shopping_list)):
    print(f'{item}. {shopping_list[item]}')
    print(end='')