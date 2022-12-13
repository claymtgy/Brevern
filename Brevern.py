player_health = 100
player_inventory = []

welcome_message = "The wind rustles the empty trees as you come to."

print(welcome_message)

starting_health = input("When you fell against the tree, were you: \n1: Losing a fight\n2: Drinking\n3: I have no idea\n\n[1]\n[2]\n[3]\n")

if starting_health == 1:
    player_health = 70

elif starting_health == 2:
    player_health == 100

else:
    player_health == 100

print(f"Your Health: {player_health}")
