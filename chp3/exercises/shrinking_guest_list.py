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

print("\nHey I've found a bigger table!")

guests.insert(0, 'chopin')
guests.insert(2, 'vivaldi')
guests.append('strauss')

msg = guests[0].title()
print(f"\n{msg} please come dinner.")

msg = guests[1].title()
print(f"{msg} please come dinner.")

msg = guests[2].title()
print(f"{msg} please come dinner.")

msg = guests[3].title()
print(f"{msg} please come dinner.")

msg = guests[4].title()
print(f"{msg} please come dinner.")

msg = guests[5].title()
print(f"{msg} please come dinner.")

print("\nI can only invite two people")

removed = guests.pop()
print(f"\nSorry {removed.title()} you won't dinner.")

removed = guests.pop()
print(f"\nSorry {removed.title()} you won't dinner with us.")

removed = guests.pop()
print(f"\nSorry {removed.title()} you won't dinner.")

removed = guests.pop()
print(f"\nSorry {removed.title()} you won't dinner.")

invited = guests[0].title()
print(f"\n{invited} you are still invited.")

invited = guests[1].title()
print(f"\n{invited} you are still invited.")

del(guests[0])
del(guests[0])
print(guests)
