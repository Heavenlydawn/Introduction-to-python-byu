'''
==========================================
CREATIVITY
Clear formatting for the output to enhance readability.
A single print statement at the beginning to summarize the temperature before listing wind chill values, making it easier for users to reference.
==========================================

'''

def calculate_wind_chill(temperature, wind_speed):
    # Formula for Calculating the wind chill.
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

    # Convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32

# Main program
def calculate_windchill():
    # Get user input for temperature
    temperature = float(input("What is the temperature? "))
    temp_scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    # Convert temperature from Celsius to Fahrenheit  
    if temp_scale == 'C':
        temperature = celsius_to_fahrenheit(temperature)
    
    # Display results for wind chill calculations
    print(f"At temperature {temperature:.1f}F, wind chill values are:")

    # From 5 to 60 mph, increment by 5
    for wind_speed in range(5, 65, 5):  
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

if __name__ == "__main__":
    calculate_windchill()