class Character:
    def __init__(self, name, life=20, attack=10) -> None:
        self.name = name
        self.life = life
        self.attack = attack
    
    def basic_attack(self, other):
        other.life -= self.attack
    
class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("Druid have been created!")
    
    def meditate(self):
        self.life +=10
        self.attack -=2

    def animal_help(self):
        self.attack +=5
    
    def fight(self, other):
        other.life -= (0.75 * self.life + 0.75 * self.attack)

class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("Warrior have been created!")
    
    def brawl(self, other):
        other.life -= 2 * self.attack
        self.life += 0.5 * self.attack

    def train(self):
        self.life += 2
        self.attack += 2

    def roar(self, other):
        other.attack -= 3

class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print("Mage have been created!")
    
    def curse(self, other):
        other.attack -= 2
    
    def summon(self):
        self.attack += 3

    def cast_spell(self, other):
        other.life -= self.attack // self.life

dru = Druid('Dru')
war = Warrior('War')
mag = Mage("Mag")

mag.cast_spell(war)
war.brawl(dru)
war.train()
mag.curse(dru)
mag.summon()
dru.meditate()

