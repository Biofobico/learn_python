# Tuples são imutáveis
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions")
for dimension in dimensions:
    print(dimension)

# Mas podemos alterar os seus valores atribuindo um novo valor
# a uma variável que representa uma tupla
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
