import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def main():
    # Prompt the user for the three numbers
    print("Enter the dimensions of the tire:")
    width = float(input("Width of the tire in mm (e.g., 205): "))
    aspect_ratio = float(input("Aspect ratio of the tire (e.g., 60): "))
    diameter = float(input("Diameter of the wheel in inches (e.g., 15): "))

    # Calculate the volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Display the result
    print(f"\nThe approximate volume of the tire is {volume:.2f} liters.")

    # Getting the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Open the file and append the data
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")

    # Tire pricing
    tire_price = None
    if abs(width - 205) < 0.1 and abs(aspect_ratio - 60) < 0.1 and abs(diameter - 15) < 0.1:
        tire_price = 75.99
    elif abs(width - 225) < 0.1 and abs(aspect_ratio - 65) < 0.1 and abs(diameter - 17) < 0.1:
        tire_price = 89.99
    elif abs(width - 195) < 0.1 and abs(aspect_ratio - 55) < 0.1 and abs(diameter - 16) < 0.1:
        tire_price = 69.99
    elif abs(width - 215) < 0.1 and abs(aspect_ratio - 50) < 0.1 and abs(diameter - 18) < 0.1:
        tire_price = 99.99

    if tire_price:
        print(f"Tires with the dimensions {width}/{aspect_ratio}R{diameter} cost ${tire_price:.2f} each.")

    # Additional feature:
    # Asking if the user wants to buy tires and recording their details in a file
    buy_tires = input("\nDo you want to buy tires with these dimensions? (yes/no): ").strip().lower()
    if buy_tires == "yes":
        quantity = float(input("How many tires will you love to get? "))
        phone_number = input("Please enter your phone number: ").strip()
        address = input("Please enter your address: ").strip()
        price = quantity * tire_price
        
        with open("volumes.txt", "a") as file:
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Price: {price}\n")
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Address: {address}\n")
        print("Thank you! Your request has been recorded.")

if __name__ == "__main__":
    main()
