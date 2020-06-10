"""
In this simple RPG game, The Hero (You) fights the enemy. You have the options to:

1. fight enemy
2. do nothing - in which case the enemy will attack you anyway
3. flee

"""

# Hero and Goblin classes

import random
import time
from colorize import Colorize

class Character(object):
    def __init__(self, name='<undefined>', health=10, power=5, coins=20, bounty=5):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty

    def is_alive(self):
        return self.health > 0

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            # If its any other troop than hero, remove it from enemy_order.
            if self.name != "Hero":
                # Zombies cannot die
                if self.name == "Zombie":
                    print("Uh Oh, Can't kill zombies! Zombie Heals 5 Health")
                    # Can't die, so set health to 5 every attack
                    self.health = 5
                else:
                    # Any other troop
                    print("Yeah! %s is dead. %s Coins Collected" % (self.name, self.bounty))
                    # getting the global value of coin_count since its outside the function
                    global coin_count
                    coin_count += self.bounty
                    enemy_order.pop(0)

                    if len(enemy_order) > 0:
                        # Special msg for Palpatine aka the boss
                        if enemy_order[0].name == "Palpatine":
                            print("\n'I AM THE SENATE!'\nUh oh, Palpatine just showed up\n")
                        else:
                            # Standard msg
                            print("\nNEW CHALLENGER: %s\n" % enemy_order[0].name)
            else:
                print("OH NO, YOU DIED!\nThanks For Playing!")
                exit()
    
    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))

        # Outside reference to the troops power. Changed for abilities and such.
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

        # if palpatine is attacking, 1/10 chance of 100 Damage Lightning shock
        if self.name == "Palpatine":
            chance = random.randint(1, 10)
            if chance == 1:
                _power_ = 100

        print("%s Dealt %s Damage to %s" % (self.name, _power_, enemy.name))
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

class Palpatine(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 30
        self.health = 15
        self.power = 5
        self.name = "Palpatine"

class Shadow(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 7
        self.name = name
        self.health = 1
        self.power = 1
        self.name = "Shadow"

class Zombie(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 5
        self.health = 5
        self.power = 2
        self.name = "Zombie"

class Medic(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 10
        self.health = 20
        self.power = 2
        self.name = "Medic"

class Goblin(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 5
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
            print("3. Buy Magical Items")
            print("4. Use A Magical Item")
            print("5. flee")
            print("> ",)
            user_input = input()
            if user_input == "1":
                # Hero attacks current troop
                your_hero.attack(current_enemy)
            elif user_input == "2":
                pass
            elif user_input == "3":
                enter_store()
                break
            elif user_input == "4":
                #use a magical item
                break
            elif user_input == "5":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)

            if current_enemy.is_alive():
                # Current enemy alawys attacks hero after hero attacks
                current_enemy.attack(your_hero)


def enter_store():
    while True:

        print("Welcome to the Magical Items Shop!\n---------------------")
        print("Items For Sale: \n$%s Super Tonic - Heals Hero Back To 10 HP\n$%s Armor - Enemy Attacks Deal 1 Less Damage" % (item_costs[0], item_costs[1]))
        print("\nMENU: Leave Shop(1), Buy Super Tonic(2), Buy Armor(3)")
        menu_input = int(input())

        # Reference to coin coin
        global coin_count

        #  Specifically the index for a item in either the 'items' list or 'item_costs' list
        i_inx = menu_input - 1

        if menu_input == 1:
            main()
            break
        elif menu_input == 2:
            if coin_count >= item_costs[i_inx] and items[i_inx] < 3:
                # subtracting coins and adding one of the item to the items list
                coin_count=-5
                items[menu_input - 2]+=1
                print("Purchased Super Tonic!")
            else:
                print("Not enough coins, or maximum item count reached")
        elif menu_input == 3:
            if coin_count >= item_costs[i_inx] and items[i_inx] < 1:
                coin_count-=6
                items[menu_input - 2]+=1
            else:
                print("Not enough coins, or maximum item count reached")
        

def use_items():
    while True:
        print("YOUR ITEMS = ")


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

# Receive coins from killing enemies. Use them to buy items in the shop
coin_count = 0
# 0, Tonic Drink, 1, Armor (Index is which item, number is how many)
items = [0, 0]
# Variables represent cost in coins for each item. index: 0 = tonic, 1 = armor, etc. Makes it easy to change price JUST here.
item_costs = [5, 6]
item_names = ["Super Tonic", "Armor"]

# Declaring all character entities
your_hero = Hero("Hero")
palpatine = Palpatine("Palpatine")
goblin = Goblin("Goblin")
zombie = Zombie("zombie")
medic = Medic("Medic")
shadow = Shadow("Shadow")
# The order in which you face enemies
enemy_order = [goblin, palpatine, medic, shadow]

main()

