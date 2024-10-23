# Initialize variables for minimum and maximum values
minimum_life_expectancy = 9999
maximum_life_expectancy = -1
country_min = ''
country_max = ''

year_min = ''
year_max = ''

# Variables to store year-specific data
year_life_exp_min = 9999
year_life_exp_max = -1
year_country_min = ''
year_country_max = ''
total_life_expectancy = 0
count = 0
# country__min = ' ' 
# country__max = ' ' 

with open('life-expectancy.csv') as life_expectancy_data:
    # Ask the user for a year of interest
    user_year = int(input('Enter the year of interest: '))

    # Iterate through each line of the dataset
    for line in life_expectancy_data:
        # Split each line into columns
        line = line.strip().split(',')

        try:
            country = line[0]
            year = int(line[2])
            life_expectancy = float(line[3])
        except ValueError:
            # Skip the current iteration if parsing fails
            continue

        # Maximum life expectancy
        if life_expectancy > maximum_life_expectancy:
            maximum_life_expectancy = life_expectancy
            country_max = country
            year_max = year

        # Minimum life expectancy
        if life_expectancy < minimum_life_expectancy:
            minimum_life_expectancy = life_expectancy
            country_min = country
            year_min = year

        # user's input
        if year == user_year:
            # Average life expectancy
            total_life_expectancy += life_expectancy
            count += 1

            #  maximum life expectancy
            if life_expectancy > year_life_exp_max:
                year_life_exp_max = life_expectancy
                year_country_max = country

            #  minimum life expectancy
            if life_expectancy < year_life_exp_min:
                year_life_exp_min = life_expectancy
                year_country_min = country

# Calculate the average life expectancy for the user's year
if count > 0:
    avg_life_expectancy = total_life_expectancy / count
else:
    avg_life_expectancy = 0



print(f'\nThe overall maximum life expectancy is {maximum_life_expectancy} from {country_max} in {year_max}.')
print(f'The overall minimum life expectancy is {minimum_life_expectancy} from {country_min} in {year_min}.')

print()
print(f'\nFor the year {user_year}:')
print(f'The average life expectancy across all countries was: {avg_life_expectancy: .2f}')
print(f'The max life expectancy was in: {year_country_max} with {year_life_exp_max}')
print(f'The max life expectancy was in: {year_country_min} with {year_life_exp_min}')
