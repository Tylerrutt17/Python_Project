"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

# Hero and Goblin classes

import random
import time

class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.power = 5


    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

class Goblin():
    def __init__(self):
        self.health = 6
        self.power = 2
        self.name = "Goblin"
    
    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    # Innefficient to do the same things in both classes, just doing it for now because of time.
    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

your_hero = Hero("Tyler")
goblin = Goblin()

def main():

    #hero_health = 10
    #hero_power = 5
    #goblin_health = 6
    #goblin_power = 2

    while goblin.health > 0 and your_hero.health > 0:
        print("You have %d health and %d power." % (your_hero.health, your_hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            your_hero.attack(goblin)
            #goblin.health -= your_hero.power
            print("You do %d damage to the goblin." % your_hero.power)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(your_hero)
            if your_hero.health <= 0:
                print("You are dead.")

main()
