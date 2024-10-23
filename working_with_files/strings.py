colors = 'red green blue yellow '

color_parts = colors.split()
# ['red', 'green', 'blue', 'yellow']

for color in color_parts:
    print(color)



# Removing whitespace from strings
name = "Heaven Gabriel"

clean_name = name.strip()

print(f'----{name}----            ')
print(f'----{clean_name}----')