my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's foods are:")
print(friend_foods)

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\n")

for food in my_foods:
    print(f"{food.title()}")

print("\n")

for food in friend_foods:
    print(f"{food.title()}")
