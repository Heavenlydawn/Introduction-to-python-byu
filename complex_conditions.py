gpa = float(input('What is your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the honor roll.')

if gpa >= .85 and lowest_grade >= .70:
    honor_roll = True
else:
    honor_roll = False


if honor_roll:
    print('You made the honor roll')

