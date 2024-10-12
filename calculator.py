# Requesting the user to type in their garde percentage
grade = float(input('What is your grade percentage? '))

# Checking for the letter associated with a garde
if grade >= 90:
    letter = "A"
elif grade >= 80:
   letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Stretch Challenge
grade_sign = ''

last_digit = grade % 10
print(last_digit)

if last_digit >= 7:
    grade_sign = '+'
elif last_digit < 3:
    grade_sign = '-'
else:
    grade_sign = ''

if grade >= 93:
    grade_sign = ''

if letter == "F":
    grade_sign = ''


print()
print(f"Your letter grade is: {letter}{grade_sign}")
print()

if grade >= 70:
    print('congratulation you are an honor roll student')
else:
    print('I trust you can do better, do not give up!')
