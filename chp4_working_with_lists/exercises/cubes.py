cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

#método List comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
