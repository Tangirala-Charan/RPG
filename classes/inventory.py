class Item:

    def __init__(self, Type, name, desc, stat):
        self.name = name
        self.Type = Type
        self.desc = desc
        self.stat = stat

    def Name(self):
        return self.name

    def get_type(self):
        return self.Type

    def description(self):
        return self.name + ' ' + self.desc

    def effect(self):
        return self.stat