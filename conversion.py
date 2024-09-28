Convert the temperature from Fahrenheit to Celsius
to_fahrenheit = input('What is the temperature in Fahrenheit?')
to_fahrenheit = int(to_fahrenheit)

to_celsius = (to_fahrenheit - 32) * 5 / 9
print(f'The temperature in Celsius is {to_celsius: .1f}')
