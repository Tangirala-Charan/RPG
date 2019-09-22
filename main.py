from classes.game import bcolors, character
from classes.magic import Offensive_Spell
from classes.inventory import Item
import random

# Data about spells
Fire = Offensive_Spell('FIRE', 10, 60)
Tornado = Offensive_Spell('TORNADO', 9, 45)
Thunder = Offensive_Spell('THUNDER', 12, 75)

magic = [Fire, Tornado, Thunder]

# Inventory Data
Dagger = Item('Weapon', 'Dagger', 'deals 100 HP damage', 100)


# Defining the player and enemy stats
Player = character(520, 70, 60, 24, magic)
Enemy = character(1100, 80, 35, 30, magic )

print(bcolors.FAIL + bcolors.BOLD +
     'ENEMY ATTACKS!!!' + bcolors.ENDC)
i = 0
running = True  # Run condition

while running:
    print('==============================\n')

# Choosing attack method
    Player.action_list()
    choice = int(input('Choose an action: '))

# If we choose to attack Melee, or if there isn't enough MP
    if choice == 1 or Player.get_mp() == 0:
        print('You chose ATTACK')
        dmg = Player.generate_dmg()
        # Decreases Enemy HP
        Enemy.take_dmg(dmg)

# When we choose Magic
    elif choice == 2:
        print('You chose MAGIC')
    # Choosing the right spell
        Player.spells_list()
        choice = int(input("Choose a spell: ")) - 1
        Spell = magic[choice]
        print("You chose",bcolors.OKGREEN + bcolors.BOLD +
              Spell.name + bcolors.ENDC)
        cost = Spell.get_cost()
        # If MP is less than cost of spell:
        if Player.get_mp() < cost :
            print(bcolors.WARNING + bcolors.BOLD +
                'NOT ENOUGH MP' + bcolors.ENDC)
            continue  # Restarts the loop w/o any damage
        # Reduces our MP by the spell cost
        Player.reduce_mp(cost)
        # Does damage to the Enemy
        magic_dmg = Spell.generate_dmg()
        Enemy.take_dmg(magic_dmg)

# Prints Enemy HP after attack
    print('ENEMY HP:', Enemy.get_hp(), '/', Enemy.get_max_hp())

# If Enemy has enough MP
    if Enemy.get_mp() >0:
        # Chooses between the 2 options
        Enemychoice = random.randint(1,2)
    else:
        Enemychoice = 1
# When Enemy chooses Attack
    if Enemychoice == 1:
        dmg = Enemy.generate_dmg()
        # Decreases Player HP
        Player.take_dmg(dmg)

# Enemy chooses Magic
    else:
        # Chooses a spell at random
        Spell = magic[random.randint(0,2)]
        if Spell.get_cost() <= Enemy.get_mp():
            dmg = Spell.generate_dmg()
        else:
            dmg = Enemy.generate_dmg()
        # Decreases Player HP
        Player.take_dmg(dmg)

    print('YOU WERE ATTACKED!!'  + bcolors.FAIL + bcolors.BOLD,
          dmg,'HP LOST !' + bcolors.ENDC)

# Has a 20% chance of healing
    if random.randrange(5) == 2:
        # Randomly heals any value b/w 60 and 80
        heal = random.randint(50,70)
        # Increases Player HP
        Player.heal(heal)
        print(bcolors.OKGREEN + bcolors.BOLD +
             'YOU HEALED',heal,'HP!'+ bcolors.ENDC)

# Prints player HP and MP after one round
    print('PLAYER HP:', bcolors.FAIL + bcolors.BOLD,
           Player.get_hp(), '/', Player.get_max_hp(), bcolors.ENDC)
    print('PLAYER MP:', bcolors.OKGREEN + bcolors.BOLD,
           Player.get_mp(), '/', Player.get_max_mp(), bcolors.ENDC)

# Enemy death ! !
    if Enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + bcolors.UNDERLINE +
             '\nVICTORY! ENEMY KILLED!!'+ bcolors.ENDC)
    # Loop run condition set to False
        running = False
        break

# Player dies
    elif Player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD +
             '\nYOU DIED!!\nBETTERLUCK NEXT TIME' + bcolors.ENDC)
    # Loop run condition set to False
        running = False
        break

# Prints a warning when Player is close to death
    elif Player.get_hp() <= 150:
        print(bcolors.WARNING + bcolors.BOLD +
             'WARNING!! YOUR HP is GETTING LOW'+ bcolors.ENDC)
