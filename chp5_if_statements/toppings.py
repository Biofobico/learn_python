requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in toppings:
    print("\nAdding mushrooms.")
if 'pepperoni' in toppings:
    print("Adding pepperoni.")
if 'extra cheese' in toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

print("\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_toppings}.")

print("\nFinished making your pizza.")
