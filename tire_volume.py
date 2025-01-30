import math
"""
    Calculate the volume of space inside a tire.
    :param width: Width of the tire in millimeters (w)
    :param aspect_ratio: Aspect ratio of the tire (a)
    :param diameter: Diameter of the wheel in inches (d)
    :return: Volume of the tire in liters (v)
"""

def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def main():
    print("Enter the dimensions of the tire:")
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15) "))


    volume = calculate_tire_volume(width, aspect_ratio, diameter)


    print(f"\nThe approximate volume of the tire is {volume:.2f} liters.")

if __name__ == "__main__":
    main()