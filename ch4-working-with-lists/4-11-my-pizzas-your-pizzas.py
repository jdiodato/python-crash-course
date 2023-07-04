my_pizzas = ['pineapple' ,'onion', 'green pepper']
friend_pizzas = my_pizzas[:]

my_pizzas.append('tomato')
friend_pizzas.append('anchovy')

print("My favorite pizza toppings are:")
for topping in my_pizzas:
    print(topping)

print("\nMy friend's favorite pizza toppings are:")
for topping in friend_pizzas:
    print(topping)