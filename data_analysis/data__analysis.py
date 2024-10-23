'''
===================================
Identify the year and country that has the largest drop from one year to the next
stable and unstable countries
Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
Checked for anomalies such as extreme life expectancy values.
insights into the life expectancy for a user-specified year and country.
===================================

'''


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

country_life_exp_min = 9999
country_life_exp_max = -1
country_total_life_exp = 0
country_count = 0

life_expectancy_history = {} 

with open('life-expectancy.csv') as life_expectancy_data:
    user_year = int(input('Enter the year of interest: '))
    
    country_of_interest = input('Enter the country of interest: ').strip().lower()

    # Iterating through each line of the dataset
    for line in life_expectancy_data:
        # Split each line into columns
        line = line.strip().split(',')

        try:
            country = line[0].strip().lower()
            year = int(line[2])
            life_expectancy = float(line[3])
        except ValueError:
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

        '''
        ===========================================
        Track life expectancy for year-to-year comparisons
        ===========================================
        '''
        if country not in life_expectancy_history:
            life_expectancy_history[country] = []
        life_expectancy_history[country].append((year, life_expectancy))

        # User's input year
        if year == user_year:
            # Total count for average life expectancy
            total_life_expectancy += life_expectancy
            count += 1

            # maximum life expectancy in the year
            if life_expectancy > year_life_exp_max:
                year_life_exp_max = life_expectancy
                year_country_max = country

            # minimum life expectancy in the year
            if life_expectancy < year_life_exp_min:
                year_life_exp_min = life_expectancy
                year_country_min = country

        # User's input country
        if country_of_interest in country:
            # Calculate total and count for country-specific life expectancy
            country_total_life_exp += life_expectancy
            country_count += 1

            # maximum life expectancy for the country
            if life_expectancy > country_life_exp_max:
                country_life_exp_max = life_expectancy

            # minimum life expectancy for the country
            if life_expectancy < country_life_exp_min:
                country_life_exp_min = life_expectancy

# Average life expectancy for the year of interest
if count > 0:
    avg_life_expectancy = total_life_expectancy / count
else:
    avg_life_expectancy = 0

# Average life expectancy for the country of interest
if country_count > 0:
    avg_country_life_exp = country_total_life_exp / country_count
else:
    avg_country_life_exp = 0

# Results
print(f'\nThe overall maximum life expectancy is {maximum_life_expectancy:.2f} from {country_max.capitalize()} in {year_max}.')
print(f'The overall minimum life expectancy is {minimum_life_expectancy:.2f} from {country_min.capitalize()} in {year_min}.')

print(f'\nFor the year {user_year}:')
print(f'The average life expectancy across all countries was: {avg_life_expectancy:.2f}')
print(f'The max life expectancy was in: {year_country_max.capitalize()} with {year_life_exp_max:.2f}')
print(f'The min life expectancy was in: {year_country_min.capitalize()} with {year_life_exp_min:.2f}')

# Handling cases where no matching country was found
if country_count > 0:
    print(f'\nFor {country_of_interest.capitalize()}:')
    print(f'Minimum life expectancy: {country_life_exp_min:.2f}')
    print(f'Maximum life expectancy: {country_life_exp_max:.2f}')
    print(f'Average life expectancy: {avg_country_life_exp:.2f}')
else:
    print(f'\nNo data found for the country: {country_of_interest.capitalize()}')

# Detecting anomalies, drops, and patterns

largest_drop = 0
country_largest_drop = ''
year_largest_drop = ''

stable_countries = []
unstable_countries = []


for country, history in life_expectancy_history.items():
    # Sort the life expectancy history by year for the country
    history = sorted(history, key=lambda x: x[0])

    # Detect the largest drop in life expectancy year-to-year
    for i in range(1, len(history)):
        previous_year, previous_life_exp = history[i - 1]
        current_year, current_life_exp = history[i]
        drop = previous_life_exp - current_life_exp

        if drop > largest_drop:
            largest_drop = drop
            country_largest_drop = country
            year_largest_drop = current_year

    # checking for  stable countries (variance of life expectancy over time)
    life_expectancies = [exp for year, exp in history]
    variance = max(life_expectancies) - min(life_expectancies)
    # Arbitrary threshold for "stability"
    if variance < 2:  
        stable_countries.append(country)
    else:
        unstable_countries.append(country)


print(f'\nThe largest year-to-year drop in life expectancy was {largest_drop:.2f} in {country_largest_drop.capitalize()} for the year {year_largest_drop}.')

print(f"\nCountries with relatively stable life expectancy over time: {', '.join([c.capitalize() for c in stable_countries])}")

print(f"\nCountries with highly fluctuating life expectancy: {', '.join([c.capitalize() for c in unstable_countries])}")
