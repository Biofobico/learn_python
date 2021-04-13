guests = ['bob marley', 'david bowie', 'freddy mercury']

name = guests[0].title()
print(f"{name} please come dinner.")

name = guests[1].title()
print(f"{name} please come dinner.")

name = guests[2].title()
print(f"{name} please come dinner.")

print(f"\n{guests[2].title()} can't come to dinner.")

del guests[-1]
guests.append('bach')

name = guests[0].title()
print(f"\n{name} please come dinner.")

name = guests[1].title()
print(f"{name} please come dinner.")

name = guests[2].title()
print(f"{name} please come dinner.")

