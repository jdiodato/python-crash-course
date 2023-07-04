# Using my pizza program from exercise 4-1.

toppings = ['onion', 'mushroom', 'green pepper', 'pineapple', 'tomato', 'anchovy', 'olives']

for topping in toppings:
    print(f"I like {topping} on my pizza.")

print("\nI really love pizza!\n")

print("The first three toppings in my list are:")
for topping in toppings[0:3]:
    print(topping)

print("\nThree items from the middle of my list are")
for topping in toppings[2:5]:
    print(topping)

print("\nThe last three items in my list are:")
for topping in toppings[-3:]:
    print(topping)