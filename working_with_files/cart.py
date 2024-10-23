shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1
max_product = ''

for item in shopping_cart:
    # Product name is the first part
    product_name = item[0]
    # The price is the second part of the item as the product is the first
    price = item[1]

    if price > max_price:
        # This is the new max
        max_price = price
        max_product = product_name
print(f'The maximum price is: {max_price: .2f}')
print(f"The product with the maximum price is: {max_product}")
print(f"You have {max_product} ---------- {max_price}")