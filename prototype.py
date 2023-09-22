class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype
        
    def info(self):
        l = "weak" if self.level <= 20 else 'fair' if self.level <= 50 else "strong"
        p = {'water':'wet', 'fire': 'fiery', 'grass': 'grassy',}
        return "{}, a {} and {} Pokemon.".format(self.name, p[self.pkmntype], l)