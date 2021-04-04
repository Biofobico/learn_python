guest_list = ['beethoven', 'david bowie', 'freddy mercury', 'mozart']
print("I'm sorry but I can only invite two people for dinner")

mozart_poped = guest_list.pop()
print(f"\nI'm sorry {mozart_poped.title()} but you are uninvited for dinner.")

freddy_poped = guest_list.pop()
print(f"Sorry {freddy_poped.title()}, you can't have dinner with us.")

print(f"\n Hello {guest_list[0].title()} and {guest_list[1].title()}. You're sill invited for dinner.")

del guest_list[0]
del guest_list[0]
print(f"\n{guest_list}")