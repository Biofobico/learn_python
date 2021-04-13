foods = ('pizza', 'hamburger', 'hot dog', 'ice cream', 'nuggets')
print("Podes escolher os seguintes pratos:")
for food in foods:
    print(f"- {food.title()}")

foods = ('pizza', 'hamburger', 'hot dog', 'ice cream', 'salad')

print("O nosso menu foi atualizado:")
print("\nOs pratos disponiveis são:")
for food in foods:
    print(f"- {food.title()}")
