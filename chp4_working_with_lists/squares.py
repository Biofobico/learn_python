squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# Mais conciso e produz o mesmo resultado que o código acima
quadrados = []
for value in range(10, 21):
    quadrados.append(value**2)
print(f"\n{quadrados}")
