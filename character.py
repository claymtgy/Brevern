class Character:
    def __init__(self, name, health, defense, weapon):
        self.name = name
        self.health = health
        self.defense = weapon

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, target):
        target.take_damage(self.weapon.damage)

