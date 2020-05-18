from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
{"name": "Thunder", "cost": 10, "dmg": 60},
{"name": "Blizzard", "cost": 10, "dmg": 60}]


player = Person(460, 65, 64, 30, magic)

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))
