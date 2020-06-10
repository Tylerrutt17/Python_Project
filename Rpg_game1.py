"""
In this simple RPG game, The Hero (You) fights the goblin. You have the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack you anyway
3. flee

"""

# Hero and Goblin classes

import random
import time
from colorize import Colorize

class Character(object):
    def __init__(self, name='<undefined>', health=10, power=5, coins=20):
        self.name = name
        self.health = health
        self.power = power

    def is_alive(self):
        return self.health > 0

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            # If its any other troop than hero, remove it from enemy_order.
            if self.name != "Hero":
                print("Yeah! %s is dead." % self.name)
                enemy_order.pop(0)
                if len(enemy_order) > 0:
                    print("\nNEW CHALLENGER: %s\n" % enemy_order[0].name)
            else:
                print("OH NO, YOU DIED!\nThanks For Playing!")
                exit()
    
    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))

        # Outside reference to the troops power
        _power_ = self.power

        if self.name == "Hero":
            # 20% Chance of doing 2x damage
            chance = random.randint(1, 5)
            if chance == 1:
                print("The Hero Dealt 2x Damage this attack!")
                _power_ = _power_ * 2

        if enemy.name == "Medic":
            # 20% Chance of healing 2 health
            chance = random.randint(1, 5)
            if chance == 1:
                print("You dealt 2 less damage to the medic because he healed up!")
                _power_ = _power_ -2
        
        if enemy.name == "Shadow":
            # 10% Chance of taking damage
            chance = random.randint(1, 10)
            if chance != 1:
                print("The Shadow Evaded your attack!")
                _power_ = 0

        print("%s Dealt %s Damage to the %s" % (self.name, _power_, enemy.name))
        enemy.receive_damage(_power_)
        time.sleep(1.5)
        
    def print_status(self):
        print("%s has %s health and %s power" % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.name = name
        self.health = 10
        self.power = 5

class Shadow(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.name = name
        self.health = 1
        self.power = 1
        self.name = "Shadow"

class Zombie(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.name = name
        self.health = 5
        self.power = 2
        self.name = "Zombie"

class Medic(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.name = name
        self.health = 20
        self.power = 2
        self.name = "Medic"

class Goblin(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.health = 6
        self.power = 3
        self.name = "Goblin"

def main():
    # Set it to false when hero dies to end game
    

    while True:
        # Just grab the first one and go from there. Removes one every time one is defeated
        current_enemy = enemy_order[0]

        while current_enemy.is_alive() and your_hero.is_alive():
            your_hero.print_status()
            current_enemy.print_status()
            print()
            print("What do you want to do?")
            print("1. fight %s" % current_enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = input()
            if user_input == "1":
                # Hero attacks current troop
                your_hero.attack(current_enemy)
            elif user_input == "2":
                pass
            elif user_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)

            if current_enemy.is_alive():
                # Current enemy alawys attacks hero after hero attacks
                current_enemy.attack(your_hero)


word_colors = {
    "dice":"Green",
    "YOU DIED":"Red",
    "NEW CHALLENGER":"Yellow",
    "Hero":"Green",
    "Goblin":"Red",
    "Shadow":"Magenta",
    "average":"Yellow"

}

colorize = Colorize(word_colors,{"Yellow":"\u001b[33;1m"})

your_hero = Hero("Hero")
goblin = Goblin("Goblin")
medic = Medic("Medic")
shadow = Shadow("Shadow")
enemy_order = [goblin, medic, shadow]
main()
