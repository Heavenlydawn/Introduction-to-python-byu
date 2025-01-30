def display_regular(string):
    string_received = string
    return string_received

def display_uppercase(string):
    string_received = string.upper()
    return string_received

def display_lowercase(string):
    string_received = string.lower()
    return string_received

first_name = input('Enter your first name: ')

print(display_regular(first_name))
print(display_uppercase(first_name))
print(display_lowercase(first_name))

'''
OR

def display_regular(message):
    print(message)

def display_uppercase(message):
    # This could be done on one line, without creating a new variable new_message
    new_message = message.upper()
    print(new_message)

def display_lowercase(message):
    new_message = message.lower()
    print(new_message)

# The regular flow of the program starts here...
user_message = input("What is your message? ")

# Pass this variable to each of the functions above to do their work
display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)

'''