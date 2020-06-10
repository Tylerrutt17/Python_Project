"""
In this simple RPG game, The Hero (You) fights the goblin. You have the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack you anyway
3. flee

"""

# Hero and Goblin classes

import random
import time

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
            print("Oh no! %s is dead." % self.name)
    
    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)
    def print_status(self):
        print("%s has %s health" % (self.name, self.health))

class Hero(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.name = name
        self.health = 10
        self.power = 5

class Goblin(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.health = 6
        self.power = 2
        self.name = "Goblin"

your_hero = Hero("Tyler")
goblin = Goblin("Goblin")

def main():

    while goblin.is_alive() and your_hero.is_alive():
        print("You have %d health and %d power." % (your_hero.print_status, your_hero.power))
        print("The goblin has %d health and %d power." % (goblin.print_status, goblin.power))
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

        if goblin.is_alive():
            # Goblin attacks hero
            goblin.attack(your_hero)
            if your_hero.is_alive == False:
                print("You are dead.")

main()
