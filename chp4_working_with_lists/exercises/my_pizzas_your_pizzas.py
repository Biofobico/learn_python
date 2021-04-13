favorite_pizza = ['tropical', 'havaiana', 'romana']
friends_pizzas = favorite_pizza[:]

favorite_pizza.append('napolitana')
friends_pizzas.append('pepperoni')

print("My favorite pizzas are:")
for pizza in favorite_pizza:
    print(f"- {pizza}")

print("\nMy friends favorite pizzas are:")
for pizza in favorite_pizza:
    print(f"- {pizza}")
