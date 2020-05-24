from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# The Black Magic Spells
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
tsunami = Spell("Tsunami", 40, 1200, "black")
meteor = Spell("Meteor", 20, 200, "black")

# The White Magic Spells
cure = Spell("Cure", 25, 620, "white")
healing_word = Spell("Healing Word", 32, 1500, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, tsunami, meteor, cure, healing_word]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, 
{"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5}, {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Instantiate People
player1 = Person("Blk Q:", 3260, 140, 300, 30, player_spells, player_items)
player2 = Person("Cloud:", 4160, 188, 325, 30, player_spells, player_items)
player3 = Person("Penny:", 3090, 174, 288, 30, player_spells, player_items)
enemy = Person("Chimera", 11200, 701, 500, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("============================================")

    print("\n\n")
    print("NAME                          HP                                 MP")
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:      
        
        player.choose_action()
        choice = input("       Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.") ##Enemy HP:, enemy.get_hp()
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("     Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spell_damage()
            cost = spell.cost

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)


            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("      Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "Fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg) ##"Player HP", player.get_hp()
    print("==========================================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your Enemy Has Defeated You!" + bcolors.ENDC)
        running = False