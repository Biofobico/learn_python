guest_list = ['beethoven', 'david bowie', 'freddy mercury', 'mozart']
print("I've found a bigger table so I'll invite more people.")

guest_list.insert(0, 'chopin')
guest_list.insert(3, 'vivaldi')
guest_list.append('bach')

print(f"\nHello {guest_list[0].title()}, would you like to have a dinner with us?")
print(f"Good morning {guest_list[1].title()}, would you like to have a dinner with us?")
print(f"Hi {guest_list[2].title()}, would you like to have a dinner with us?")
print(f"Howdy {guest_list[3].title()}, would you like to have a dinner with us?")
print(f"Hello {guest_list[4].title()}, would you like to have a dinner with us?")
print(f"Good afternoon {guest_list[5].title()}, would you like to have a dinner with us?")
print(f"Hi there {guest_list[-1].title()}, would you like to have a dinner with us?")
