from .magic import Offensive_Spell
import random


class bcolors:
    # Different colour codes
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class character:

    def __init__(self, name, hp, mp, atk, df, magic, Items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.df = df
        self.atkl = atk - 15
        self.atkh = atk + 15
        self.magic = magic
        self.Items = Items
        self.actions = ['Attack', 'Magic', 'Items']

    def Name(self):
        return self.name

    def generate_dmg(self):
        return random.randint(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg

        if self.hp <= 0:
            self.hp = 0

        return self.hp

    def heal(self, heal):
        self.hp += heal

        if self.hp >= self.max_hp:
            self.hp = self.max_hp

        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def spell_name(self, i):
        return self.magic[i]

    def reduce_mp(self, cost):
        self.mp -= cost

        if self.mp <= 0:
            self.mp = 0

        return self.mp

    def hp_bar(self):
        return int(20*self.hp/self.max_hp)

    def mp_bar(self):
        return int(10*self.mp/self.max_mp)

    '''
    def double_atk(self, incr):
        self.atk *= incr

    def original_atk(self):
        self.atk = atk
    '''


    def Info(self, color = bcolors.OKGREEN):

        spchar = '█'
        print(' '*28 + '_'*20 + ' '*9 + '_'*10)
        print(bcolors.BOLD + f'{self.name:15s}  '+
              f'{self.hp:4d}/{self.max_hp:4d} |'+
              color + f'{spchar*self.hp_bar():20s}'+
              bcolors.ENDC + '| ' + bcolors.BOLD +
              f'{self.mp:2d}/{self.max_mp} |'+ bcolors.OKBLUE+
              f'{spchar*self.mp_bar():10s}' + bcolors.ENDC + '|\n')


    def action_list(self):
        print(bcolors.OKBLUE + bcolors.BOLD + 'ACTIONS:' + bcolors.ENDC)
        i = 1
        for item in self.actions:
            print(f'{i}. {item}')
            i += 1

    def spells_list(self):
        print(bcolors.OKGREEN + bcolors.BOLD + '\nSPELLS:' + bcolors.ENDC)

        print(f'   NAME      COST   DAMAGE')
        i = 1
        for spell in self.magic:
            print(f'{i:<3d}{spell.Name():13s}{spell.Cost():2d}      {spell.Damage()}')
            i += 1

    def items_list(self):
        print(bcolors.OKGREEN + bcolors.BOLD + '\nITEMS:' + bcolors.ENDC)
        i = 1
        for Type in self.Items:
            print('\n' + Type + ':\n')
            for item in self.Items[Type]:
                print(f'{i}. {item.description():50s} {item.Count()}')
                i += 1
