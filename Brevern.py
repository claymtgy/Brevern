  from character import Character
  from weapon import Weapon
  from inventory import Inventory

  # Create some weapons
  sword = Weapon("Sword", 10, 5)
  dagger = Weapon("Dagger", 5, 7)

  # Create a character and give them a weapon
  player = Character("Player", 100, sword)

  # Create an inventory and add some items to it
  inventory = Inventory()
  inventory.add_item(dagger)

  # Get the first item in the inventory and equip it as the player's weapon
  item = inventory.get_item(0)
player.weapon = item

# Attack the target with the player's current weapon
target = Character("Target", 100, None)
player.attack(target)

# Print out the target's health to verify that it was damaged
print(target.health)

