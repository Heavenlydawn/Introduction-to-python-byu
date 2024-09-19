# Importing Math Library in order to use the math.sqrt function
import math

# # SQUARE
square = input('What is the length of a side of the square?')

square = float(square) ** 2
area_of_a_square = square
print(f'The area of the square is {area_of_a_square}')



# # RECTANGLE
rectangle_length = input ('What is the length of the rectangle?')
rectangle_width = input ('What is the width of the rectangle?')

rectangle_length = float(rectangle_length)
rectangle_width = float(rectangle_width)
area_of_a_rectangle = rectangle_length * rectangle_width

print(f'The area of the rectangle is {area_of_a_rectangle}')



# # CIRCLE

radius_of_a_circle = input('What is the radius of  the circle?')
radius_of_a_circle = float(radius_of_a_circle)

area_of_a_circle = math.pi * (radius_of_a_circle ** 2)

print(f'The area of the circle is {area_of_a_circle: .1f}')

