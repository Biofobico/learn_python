guest_list = ['bob marley', 'david bowie', 'freddy mercury', 'mozart']
print(f"Hello {guest_list[0].title()}, would you like to have dinner with me?")
print(f"Hi {guest_list[1].title()}, would you like to have dinner with me?")
print(f"Hello {guest_list[2].title()}, fancy a dinner with me?")
print(f"Hello {guest_list[-1].title()}, would you like to have a dinner with me?")

print(f"\nUnfortunately {guest_list[0].title()} can't join us for dinner.")

guest_list[0] = 'beethoven'

print(f"\nHello {guest_list[0].title()}, would you like to have a dinner with us?")
print(f"Good afternoon {guest_list[1].title()}, would you like to have a dinner with us?")
print(f"Hi {guest_list[2].title()}, would you like to have a dinner with us?")
print(f"Howdy {guest_list[-1].title()}, would you like to have a dinner with us?")