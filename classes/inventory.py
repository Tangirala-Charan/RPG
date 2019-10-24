'''
class Weapon:

    def __init__(self, name, desc, dmg, count):
        self.name = name
        self.desc = desc
        self.dmg = dmg
        self.count = count

    def Name(self):
        return self.name

    def description(self):
        return self.name + ' ' + self.desc

    def damage(self):
        if self.count > 0:
            self.count -= 1
            return self.dmg
        return -1

    def Count(self):
        return self.count

class Potion:

    def __init__(self, name, desc, stat, count):
        self.name = name
        self.desc = desc
        self.stat = stat
        self.count = count

    def Name(self):
        return self.name

    def description(self):
        return self.name + ' ' + self.desc

    def Heal(self):
        if self.count > 0:
            self.count -= 1
            return self.stat
        return self.stat

    def Count(self):
        return self.count
'''
class Item:

    def __init__(self, name, desc, stat, count):
        self.name = name
        self.desc = desc
        self.stat = stat
        self.count = count

    def Name(self):
        return self.name

    def description(self):
        return self.name + ' ' + self.desc

    def get_stat(self):

        if self.count > 0:
            self.count -= 1
            return self.stat

        return -1

    def Count(self):
        return self.count