fruta_1 = 'laranja'
fruta_2 = 'limão'

print(fruta_1 == fruta_2)
print("Falso")

print(fruta_1 != fruta_2)
print("Verdadeiro")

fruta_3 = 'Banana'
fruta_4 = 'banana'

print(fruta_3 == fruta_4)
print("Falso")

print(fruta_3.lower() == fruta_4)
print("Verdadeiro")

num_1 = 5
num_2 = 8

print(num_1 == num_2)
print("\nFalso")

print(num_1 > num_2)
print("Falso")

print(num_1 < num_2)
print("Verdadeiro")

print(num_1 >= num_2)
print("Falso")

print(num_1 <= num_2)
print("Verdadeiro")

print(num_1 != num_2)
print("Verdadeiro")

lista_a = [5, 8, 3]
lista_b = [12, 1, 8]

total_a = sum(lista_a)
total_b = sum(lista_b)

print(f"\ntotal_a = {total_a}")
print(f"total_b = {total_b}")

print("\ntotal_a >= 21 and total_b >= 21: Falso")
print((total_a >= 21) and (total_b >= 21))

print("\ntotal_a >= 21 or total_b >= 21: Verdadeiro")
print((total_a >= 21) or (total_b >= 21))

big_6 = [
    'liverpool', 'manchester united', 'arsenal', 'manchester city', 'chelsea',
    'totenham'
]

print('arsenal' in big_6)

club = 'leicester'
if club not in big_6:
    print(
        f"\n{club.title()} devia fazer parte do big_6 porque já ganhou um campeonato."
    )
