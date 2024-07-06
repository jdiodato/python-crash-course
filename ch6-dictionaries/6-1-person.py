p = {
    'first name': 'jim',
    'last name': 'kirk',
    'age': 40,
    'city': 'riverside'
}

first_name = p['first name'].title()
last_name = p['last name'].title()
age = p['age']
city = p['city'].title()

print(f"This person's name is {first_name} {last_name}.")
print(f"He hails from the city of {city}.")