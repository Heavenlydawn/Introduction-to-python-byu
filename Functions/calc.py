import math

# SQUARE
def compute_area_square(square):
    area_of_a_square = square ** 2
    return area_of_a_square

# # RECTANGLE
def compute_area_rectangle(rectangle_length, rectangle_width):
    area_of_a_rectangle = rectangle_length * rectangle_width
    return area_of_a_rectangle


# CIRCLE
def compute_area_circle(radius):
    area_of_a_circle = math.pi * (radius ** 2)
    return area_of_a_circle






shape = ''

while shape != "quit":
    shape = input("What shape do you have? ")

    # Convert to lower case
    shape = shape.lower()

    if shape == "square":
        square_area = float(input('What is the length of a side of the square? '))
        print(f'The area of the square is {compute_area_square(square_area )}')

    elif shape == "rectangle":
        rectangle_length = float(input ('What is the length of the rectangle? '))
        rectangle_width = float(input ('What is the width of the rectangle?'))
        print(f'The area of the rectangle is {compute_area_rectangle(rectangle_length, rectangle_width)}')

    elif shape == "circle":
        radius_of_a_circle = float(input('What is the radius of  the circle? ' ))
        print(f'The area of the circle is {compute_area_circle(radius_of_a_circle): .2f}')