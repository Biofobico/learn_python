motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]= 'ducati' # substitui o primeiro item da lista
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') #adiciona ducati ao fim da lista
print(motorcycles)

motorcycles = [] # cria uma lista vazia
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') #insere o valor 'ducati' no início da lista
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] #apaga o primeiro item da lista(se soubermos a posição do item na lista)
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() #remove o último item da lista(ainda pode ser usado)
print(motorcycles)
print(popped_motorcycle) # print o item removido da lista

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

first_owned = motorcycles.pop(0) #remove(pop) o primeiro item da lista
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

## remover item através do seu valor ao invés da posição(pode ser usado de seguida como o pop())
motorcycles.remove('ducati') #remove diz a python para encontrar o item 'ducati' na lista e para o remover

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")