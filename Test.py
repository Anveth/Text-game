import random

#Create account

print("Create Account")
print()

login = input("create login: ")
password = input("create password: ")
print()
print("Account Created")
print("Log in")
print()

while True:
    enter_login = input("enter login: ")
    enter_password = input("enter password: ")
    if enter_login == login and password == enter_password:
        print()
        print("You succesfully logged in")
        print()
        break
    elif enter_login != login and password == enter_password:
        print()
        print("invalid login")
        print()
    elif enter_login == login and password != enter_password:
        print()
        print("invalid password")
        print()
    else:
        print()
        print("Invalid login and password")
        print()

#Characters

class Char:
    def __init__(self, gender, race, spec, atkp):
        self.gender = gender
        self.race = race
        self.spec = spec
        self.atkp = atkp
        
Man = Char("Male", "Human", "Warrior", 250)
print(Man.gender + " | " + Man.race + " | " + Man.spec + " | " + str(Man.atkp))
print()
print()

Woman = Char("Female", "Elf", "Mage", 310)
print(Woman.gender + " | " + Woman.race + " | " + Woman.spec + " | " + str(Woman.atkp))
print()
print()

if Man.atkp + Woman.atkp < 500:
    print("Your attack power is too low")
elif Man.atkp + Woman.atkp > 800:
    print("Your attack power is great")
else:
    print("You have enough attack power")
    
#Random number    

print()
print("Random Number: " + str(random.randint(50,250)))
print()

#Game

import time
import random
# zport sys

time.sleep(0.5)
name = input("Write your name: ")
time.sleep(0.5)
print("Welcome " + name)
print()
time.sleep(0.5)


race = input("what is your race? ")
time.sleep(0.5)
print("You are " + race)
print()
time.sleep(0.5)

spec = input("what is your specialization? \"warrior\" or \"mage\": ")
print()
print()
time.sleep(0.5)
print("Your specialization is: " + spec)
print()

time.sleep(2)

print("You are: " + name + " | " + race + " | " + spec)
print()

time.sleep(2)

if spec == "warrior":
    print("You are a warrior from Vrenthos")
    print()
elif spec == "mage":
    print("you are a mage from Anvethye")
    print()
else:
    print("invalid specialization, game over")
#    sys.exit()

road = input("You are heading to the town, which way do you want to take, forest or mainroad? ")
print()
print()

if road == "mainroad":
    print("You are going to the town by the main road")
    print()
    
elif road == "forest":
    print()
    print()
    print("You are going to the town by the forest")
    print()
    action = input("On your road you encounter huge bear, do you \"attack\" it or \"run\" away from it? ")
    print()
    
    if action == "attack":
        roll = input("Write \"roll\" to generate your attack power: ")
        if roll == "roll":
            random_number = random.randint(0, 10)
            print("You rolled: " + str(random_number))
            print()
            if random_number == 0:
                print("You missed the hit and the bear has bitten u badly in the hand, but the second hit was deadly for the bear")
                print()
            elif random_number <= 4:
                print("You managed to defeat the bear, but you are really exhausted now")
                print()
            elif random_number <= 9:
                print("You defeated the bear with ease")
                print()
            else:
                print("*critical hit* You defeated the bear with first strike and now you preper the food from the bear, you get well fed status")
                print()
        else:
            print("You have run out of time and the bear has eaten you alive")
            #    sys.exit()
            
    elif action == "run":
        roll = input("Write \"roll\" to generate your escaping chance: ")
        print()
        if roll == "roll":
            random_number = random.randint(0, 10)
            print("You rolled: " + str(random_number))
            print()
            if random_number == 0:
                print("You stepped on a rock, fell down and the bear has bitten your leg")
                print()
            else:
                print("You managed to escape the bear")
                print()
        else: 
            print("death")
            print()
else:
    print ("You chose the wrong way and died")

print("You reach the town of Aedos")
print()