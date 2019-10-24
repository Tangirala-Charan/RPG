from classes.game import bcolors, character
from classes.magic import Offensive_Spell
from classes.inventory import Item
import random


# Data about spells
Fire = Offensive_Spell('Fire', 10, 60)
Tornado = Offensive_Spell('Tornado', 9, 45)
Thunder = Offensive_Spell('Thunder', 12, 75)
Quake = Offensive_Spell('Earthquake', 16, 95)

magic = [Fire, Tornado, Thunder, Quake]


# Inventory Data
Dagger = Item('Dagger', 'deals 100 HP damage', 100, 3)
Grenade = Item('Grenade', 'deals 200 HP damage', 200, 2)

Weapons = [Dagger, Grenade]

Meed = Item('Meed', 'restores a small amount of HP', 50, 5)
Elixir = Item('Elixir', 'restores a considerable amount of HP', 100, 3)
Medkit = Item('Cure-all', 'restores HP to max', 10_000, 1)
#Boost = Potion('Boost', 'increases Attack by 50%', 1.5, 1)

Potions = [Meed, Elixir, Medkit]

# Need to change Items Structure.
# Hard to assign item number
Items = {'Weapons': Weapons, 'Potions': Potions}  # Add Boost later

weapons_num = len(Weapons)
items_num = weapons_num + len(Potions)


# Defining the player and enemy stats

P1 = character('Percy', 520, 70, 60, 24, magic[:], Items)
P2 = character('Jason', 600, 50, 80, 18, magic[1:], Items)
P3 = character('Grover', 900, 55, 40, 20, magic[1:3], Items)

Players = [P1, P2, P3]

E1 = character('Kronos', 1100, 80, 35, 30, magic, {})
E2 = character('Kronos', 1100, 80, 35, 30, magic, {})
E3 = character('Kronos', 5000, 80, 30, 50, magic, {})

Enemies = [E1, E2, E3]


def choose_target(opp_team = Enemies):
    '''
    Prints a list of opponents you can attack.
    Choose one of them. Default list is Enemies.
    '''
    for i in range(len(opp_team)):
        print(f'{i+1}. {opp_team[i].name}' )

    target = opp_team[int(input('Choose your target:')) - 1]

    return target

print(bcolors.FAIL + bcolors.BOLD +
      '\nYou are being ATTACKED!!!' + bcolors.ENDC)

i = 0

while True:

    print('='*68 + '\n')

    print('Name' + ' '*17 + 'HP' + ' '*29 + 'MP')

    for char in Players:
        char.Info()

    print('\nENEMY:')
    for Enemy in Enemies:
        Enemy.Info(bcolors.FAIL)

    Player = Players[i]  # Players acc. to turns
    i = (i + 1) % len(Players)

    Enemy = random.choice(Enemies)  # Randomly chooses Enemy

# Choosing attack method
    Player.action_list()
    choice = int(input(f'\n{Player.name},\nChoose an action: '))

# If we choose to attack Melee, or if there isn't enough MP
    if choice == 1:

        print('\n'+ Player.name,'chose ATTACK')
        dmg = Player.generate_dmg()

        choose_target().take_dmg(dmg)

# When we choose Magic
    elif choice == 2:

        Player.spells_list()
        choice = int(input("\nChoose a spell: ")) - 1

        Spell = magic[choice]

        print(Player.name,'chose', bcolors.OKGREEN +
              bcolors.BOLD + Spell.name + bcolors.ENDC)

        # Restart if MP is less than cost of spell.
        if Player.mp < Spell.cost:
            print(bcolors.WARNING + bcolors.BOLD +
                  'Not Enough MP' + bcolors.ENDC)
            continue

        Player.reduce_mp(Spell.cost)
        dmg = Spell.generate_dmg()

        choose_target().take_dmg(dmg)

    elif choice == 3:

        Player.items_list()

        choice = int(input('\nChoose an item: ')) - 1

        if choice not in range(items_num):
            print("INVALID CHOICE")
            continue

        # If choice is a Weapon
        if choice < weapons_num:

            item = Items['Weapons'][choice]

            if item.count == 0:
                print('ITEM NOT AVAILABLE')
                continue

            else:
                choose_target().take_dmg(item.get_stat())

        # If choice is a Potion
        else:

            item = Items['Potions'][choice - weapons_num]

            if item.count == 0:
                print('ITEM NOT AVAILABLE')
                continue

            Player.heal(item.get_stat())

            if item == Medkit:
                continue  # Prevents Enemy from attacking

        print('\n'+ Player.name, ' chose', item.name + '\n')


    Enemychoice = random.randint(1, 2)


# Enemy chooses Attack
    if Enemychoice == 1:
        dmg = Enemy.generate_dmg()


# Enemy chooses Magic
    else:

        Spell = random.choice(magic)
        # IF MP is not available
        if Spell.cost > Enemy.mp:
            dmg = Enemy.generate_dmg()  # Normal Attack

        else:
            dmg = Spell.generate_dmg()
            Enemy.reduce_mp(Spell.cost)

    # Randomly attacks a player
    target = random.choice(Players)
    target.take_dmg(dmg)

    print(Player.name, 'lost ' + bcolors.FAIL + bcolors.BOLD,
          dmg, bcolors.ENDC + ' HP !')


# IF enemy dies
    if Enemy.hp == 0:

        print(bcolors.OKGREEN + bcolors.BOLD + bcolors.UNDERLINE +
              f'\n' + Enemy.name + ' Dead.\n' + bcolors.ENDC)
        # Removing Enemy from the list
        Enemies.remove(Enemy)
        # If Enemies are all dead / len == 0
        if not Enemies:
            print(bcolors.BOLD + bcolors.OKBLUE + '\n'+
                  '\nENEMIES VANQUISHED!!!\nHEROES for the WIN' + bcolors.ENDC)

            break

# Player dies
    elif Player.hp == 0:

        print('\n'+ Player.name + ' was '+
              bcolors.FAIL + bcolors.BOLD + 'KILLED!!\n' + bcolors.ENDC)

        Players.remove(Player)
        # If all players are dead.
        if not Players:
            print('\nAll Players are DEAD.\nBetter luck Next time.')

            break


# Prints a warning when Player is close to death
    elif Player.hp <= 150:

        print(bcolors.WARNING + bcolors.BOLD +
              'WARNING!! ' + Player.name +'\'s HP is getting low'
              + bcolors.ENDC)
