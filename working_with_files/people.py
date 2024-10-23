people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_person_age = 9999
youngest_person_name = ''

for person in people:
    # print(person)
    name = person.split()[0]
    age = int(person.split()[1])
    # print(age)
    # print(name)

    if age < youngest_person_age:
        youngest_person_age = age
        youngest_person_name = name
print(f'The youngest is {youngest_person_name} {youngest_person_age} years of age')