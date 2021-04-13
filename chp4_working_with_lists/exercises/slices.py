numbers = []
for value in range(1, 21):
    numbers.append(value)
print(numbers)

print(f"The first three items in the list are: {numbers[:3]}")
print(f"The three numbers from the middle of the list are: {numbers[9:12]}")
print(f"The last three items in the list are: {numbers[-3:]}")
