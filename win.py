'Two fighters, one winner.'
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def declare_winner(fighter1, fighter2, first_attacker):
        fighter1roundsalive = fighter1.health/fighter2.damage_per_attack
        fighter2roundsalive = fighter2.health/fighter1.damage_per_attack
        if fighter1roundsalive == fighter2roundsalive:
            return first_attacker
        else:
            return fighter1.name if fighter1roundsalive > fighter2roundsalive else fighter2.name


