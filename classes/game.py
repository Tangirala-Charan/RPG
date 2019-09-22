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


class character :

    def __init__(self, hp, mp, atk, df, magic ):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.df = df
        self.atkl = atk - 15
        self.atkh = atk + 15
        self.magic = magic
        self.actions = ['ATTACK', 'MAGIC']

    def generate_dmg(self):
        return random.randint(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg

        if self.hp <= 0:
            self.hp = 0

        return self.hp

    def heal(self,heal):
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

    def spell_name(self,i):
        return self.magic[i]

    def reduce_mp(self,cost):
        self.mp -= cost

        if self.mp <= 0:
            self.mp = 0

        return self.mp

    def action_list(self):
        print(bcolors.OKBLUE + bcolors.BOLD +
              'ACTIONS:'+ bcolors.ENDC)
        i = 1

        for item in self.actions:
            print(str(i)+':',item)
            i += 1

    def spells_list(self):
        print(bcolors.OKGREEN + bcolors.BOLD
              + 'SPELLS:'+ bcolors.ENDC)
        i = 1

        for spell in self.magic:
            print(str(i)+'. ' + spell.get_name() + ' COST:',
                  spell.get_cost(), 'ATTACK:', spell.avg_dmg())
            i += 1
