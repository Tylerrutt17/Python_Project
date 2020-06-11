"""
In this simple RPG game, The Hero (You) fights the enemy. You have the options to:

1. fight enemy
2. do nothing - in which case the enemy will attack you anyway
3. Buy Magical Items
4. Use Said Magical Items
5. flee

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
            if self.name != "Jedi":
                # Zombies cannot die
                if self.name == "Zombie":
                    print("Uh Oh, Can't kill zombies! Zombie Heals 5 Health")
                    # Can't die, so set health to 5 every attack
                    self.health = 5
                else:
                    # Any other troop
                    print("Yeah! %s is dead. %s Credits Collected" % (self.name, self.bounty))
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

        if self.name == "Jedi":
            # 20% Chance of doing 2x damage
            chance = random.randint(1, 5)
            if chance == 1:
                print("The Jedi Dealt 2x Damage this attack!")
                _power_ = _power_ * 2
            # if sharpening tool has been bought, deal +1 damage
            if items[3] > 0:
                _power_+=1

        if enemy.name == "Jedi":
            # Palpatines Lighting Attack
            if self.name == "Palpatine":
                # 20% Chance of lighting attack
                chance = random.randint(1, 5)
                if chance == 1:
                    _power_ = self.power + 1
                    print("Palpatine Force Shocked You For +1 Damage!")

            # If Hero has evade on, give him a 5%+ each potion chance of evading an attack
            # Gets the count of evade potions from the items
            evade_count = items[2]
            chance = random.randint(1, 20)
            if chance <= evade_count:
                print("The Jedi Evaded the Attack!")
                _power_ = 0

            # If Hero has armor on, deduct damage by 1, unless its already at 0
            armor = items[1]
            # Armor > 0 means its been purchased
            if armor > 0:
                if _power_ > 0:
                    _power_-=1

        if enemy.name == "Medic":
            # 20% Chance of healing 2 health
            chance = random.randint(1, 5)
            if chance == 1:
                print("You dealt 2 less damage to the medic because he healed up!")
                _power_ = _power_ -2
        
        if enemy.name == "Shadow Trooper":
            # 10% Chance of taking damage
            chance = random.randint(1, 10)
            if chance != 1:
                print("The Shadow Trooper Evaded your attack!")
                _power_ = 0

        # if palpatine is attacking, 1/25 chance of 100 Damage Lightning shock // Instakill
        if self.name == "Palpatine":
            chance = random.randint(1, 25)
            if chance == 1:
                _power_ = 100
                print("\nPalpatine Called a Force Storm and Destroyed You!\n")

        # 20% Chance of doing +2 Damage
        if self.name == "Super Battle Droid":
            chance = random.randint(1, 5)
            if chance == 1:
                _power_+=2
                print("The Super Battle Droid shot his wrist rocket for +2 Damage")

        print("%s Dealt %s Damage to %s" % (self.name, _power_, enemy.name))
        enemy.receive_damage(_power_)
        time.sleep(1.5)
        
    def print_status(self):
        print("%s has %s health and %s power" % (self.name, self.health, self.power))

class Jedi(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.name = name
        self.health = 10
        self.power = 5

class Palpatine(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 30
        self.health = 25
        self.power = 5
        self.name = "Palpatine"

class Shadow(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 10
        self.name = name
        self.health = 1
        self.power = 2
        self.name = "Shadow Trooper"

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

class B1Droid(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 5
        self.health = 6
        self.power = 3
        self.name = "B1_Battle_Droid"

class SuperBattleDroid(Character):
    def __init__(self, name):
        super().__init__(name)  
        self.bounty = 8
        self.health = 10
        self.power = 3
        self.name = "Super Battle Droid"


def main():
    # Set it to false when hero dies to end game
    while True:
        
        # Game is over once all enemies are defeated
        if len(enemy_order) < 1:
            print("\n\nYou Beat All Of The Enemies! Thanks For Playing!")
            break

        # Just grab the first one and go from there. Removes one every time one is defeated
        current_enemy = enemy_order[0]

        while current_enemy.is_alive() and your_jedi.is_alive():
            your_jedi.print_status()
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
                your_jedi.attack(current_enemy)
            elif user_input == "2":
                pass
            elif user_input == "3":
                enter_store()
                break
            elif user_input == "4":
                #use a magical item
                use_items()
                break
            elif user_input == "5":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)

            if current_enemy.is_alive():
                # Current enemy alawys attacks hero after hero attacks
                current_enemy.attack(your_jedi)

def enter_store():
    while True:
        # Reference to coin coin
        global coin_count

        print("Welcome to the Magical Items Shop!\n---------------------")
        print("Items For Sale: \n$%s Super Tonic - Heals Jedi Back To 10 HP\n$%s Armor - Enemy Attacks Deal 1 Less Damage\n$%s Evade - +5 Percent chance evading an attacking. (Max 20 Percent)\n$%s Lightsaber extension - +1 Damage Per Hero Attack (1 MAX)" % (item_costs[0], item_costs[1], item_costs[2], item_costs[3]))
        print("YOUR CREDIT COUNT: %s" % coin_count)
        print("\nMENU: Leave Shop(1), Buy Super Tonic(2), Buy Armor(3), Buy Evade(4), Buy Lightsaber Extension(5)")
        menu_input = int(input())

        # Specifically the index for a item in either the 'items' list or 'item_costs' list
        i_inx = menu_input - 2

        if menu_input == 1:
            main()
            break
        elif menu_input == 2:
            if coin_count >= item_costs[i_inx] and items[i_inx] < 3:
                # subtracting coins and adding one of the item to the items list
                print("\nPURCHASED SUPER TONIC\n")
            else:
                print("Not enough credits, or maximum item count reached")
                continue
        elif menu_input == 3:
            if coin_count >= item_costs[i_inx] and items[i_inx] < 1:
                print("\nPurchased Armor!\n")
            else:
                print("Not enough credits, or maximum item count reached")
                continue
        elif menu_input == 4:
            if coin_count >= item_costs[i_inx] and items[i_inx] < 4:
                # subtracting coins and adding one of the item to the items list
                print("\nPURCHASED EVADE\n")
            else:
                print("You Can Only Buy Four of these")
                continue
        elif menu_input == 5:
            if coin_count >= item_costs[i_inx] and items[i_inx] < 1:
                # subtracting coins and adding one of the item to the items list
                print("\nPurchased Lightsaber Extension\n")
            else:
                print("You Can Only Buy 1 Of These")
                continue
        # Subtracts cost depending on which item selected
        if menu_input < 6:
            coin_count-=item_costs[i_inx]
            items[menu_input - 2]+=1
        else:
            print("Choose one of the items on the menu")
        
def use_items():
    while True:
        print("Your Items!")
        for counter, i in enumerate(items):
            # prints item index, how many, and what type
            print("%s: %sx %s" % (counter+1, i, item_names[counter]))
        
        # No items in list
        if counter <= 0:
            print("You Don't Have Any Items")
        
        use_input = int(input("Leave (0), Use Item(enter number)\n"))

        # Exits if input is 0
        if use_input == 0:     
            main()
            break

        # Can't use armor like a potion.
        if use_input != 2:
            if items[use_input-1] > 0:
                print("Using %s" % item_names[use_input-1])
                items[use_input-1]-=1
                print("Hero has 10 Health!")
                your_jedi.health = 10
            else:
                print("You Don't Own Any Of That Item!")
        else:
            if items[use_input-1] > 0:
                print("Armor is already attached.")
            else:
                print("You Don't Own Any Armor")

                
#colorize = Colorize(word_colors,{"Yellow":"\u001b[33;1m"})

# Receive coins from killing enemies. Use them to buy items in the shop
coin_count = 50
# 0, Tonic Drink, 1, Armor (Index is which item, number is how many)
items = [0, 0, 0, 0]
# Variables represent cost in coins for each item. index: 0 = tonic, 1 = armor, 2 = evade, etc. Makes it easy to change price JUST here.
item_costs = [5, 6, 5, 8]
item_names = ["Super Tonic", "Armor", "Evade Ability", "Lightsaber Extension"]

# Declaring all character entities
your_jedi = Jedi("Jedi")
palpatine = Palpatine("Palpatine")
super_battle_droid = SuperBattleDroid("Super Battle Droid")
b1_droid = B1Droid("b1_droid")
b1_droid_2 = B1Droid("b1_droid")
zombie = Zombie("zombie")
medic = Medic("Medic")
shadow = Shadow("Shadow")
# The order in which you face enemies
enemy_order = [b1_droid, b1_droid_2, super_battle_droid, medic, shadow, palpatine]

main()

