first_name = input('What is your first name?')
last_name = input('What is your last name?')
email_address = input('Type in your working email address')
phone_number= input('Type in your working phone number')
job_title = input('What do you do?')
id_number = input('Type in your Identity Number')

hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")

# output = f'{first_name} {last_name}.upper() {email_address}.lower() {phone_number} {job_title}.capitalize() {id_number}'
print('\nThe ID Card is')
print("----------------------------------------")
print('')
print(f'{last_name.upper(),} {first_name}')
print(job_title.title())
print(f'ID: {id_number}')
print()
print()
print(email_address.lower())
print(phone_number)
print("----------------------------------------")
print()
print(f"Hair: {hair_color:} Eyes: {eye_color}")
print(f"Month: {month:} Training: {training}")
print("----------------------------------------")