import random  # i mostly get this code from different pokemon adventure games on stack overflow and stuff, just a PSA
import sys
import time
import os
import pygame
from classes import *

pygame.init()

water_gun = 5  # give different moves values
scratch = 3
ember = 6
vine_whip = 4
tackle = 5
bite = 4
razor_leaf = 6
bubble_beam = 5
fire_fang = 6
pursuit = 5
poison_sting = 5
acid = 5
pound = 5

sname = "you"
ename = "Reynolds"


def battle_func():
    randechoice = random.randrange(1, 3)
    win.fill((0, 0, 0))
    "Your rival REYNOLDS wishes to battle!"
    print("1-BULBASAUR.\n2-SQUIRTLE.\n3-CHARMANDER.")
    choice = input("Choose your Pokemon: ")

    print("×" * 41)
    if int(choice) == 1:
        shp = 50
        satk = 40
        sdef = 50
        sspd = 45
        startername = "BULBASAUR"
        move1 = tackle
        move1name = "Tackle"
        move2 = vine_whip
        move2name = "Vine Whip"
        move3 = razor_leaf
        move3name = "Razor Leaf"
    elif int(choice) == 2:
        shp = 50
        satk = 40
        sdef = 60
        sspd = 40
        startername = "SQUIRTLE"
        move1 = bite
        move1name = "Bite"
        move2 = water_gun
        move2name = "Water Gun"
        move3 = bubble_beam
        move3name = "Bubble Beam"
    elif int(choice) == 3:
        shp = 50
        satk = 70
        sdef = 35
        sspd = 50
        startername = "CHARMANDER"
        move1 = scratch
        move1name = "Scratch"
        move2 = ember
        move2name = "Ember"
        move3 = fire_fang
        move3name = "Fire Fang"
    else:
        print("Please input proper values.")

    if randechoice == 1:
        ehp = 40
        eatk = 40
        edef = 30
        espd = 30
        enemyname = "JIGGLYPUFF"
        emove1 = pound
        emove1name = "Pound"
        emove2 = tackle
        emove2name = "Tackle"
        emove3 = scratch
        emove3name = "Scratch"
    elif randechoice == 2:
        ehp = 30
        eatk = 70
        edef = 30
        espd = 60
        enemyname = "RATTATA"
        emove1 = bite
        emove1name = "Bite"
        emove2 = tackle
        emove2name = "Tackle"
        emove3 = pursuit
        emove3name = "Pursuit"
    else:
        ehp = 50
        eatk = 60
        edef = 30
        espd = 40
        enemyname = "EKANS"
        emove1 = bite
        emove1name = "Bite"
        emove2 = poison_sting
        emove2name = "Poison Sting"
        emove3 = acid
        emove3name = "Acid"

    print("×" * 41)

    # begin the battle
    print("=" * 41)
    print("A BATTLE BEGAN")
    print("=" * 41)

    print("You chose level 10 " + startername + "!")
    print("Your rival chose level 10 " + enemyname + "!")
    print("-" * 41)

    if (espd > sspd):
        enemyturn = True
        starterturn = False
    else:
        starterturn = True
        enemyturn = False  # fight until either ones hp is 0 or less
    while ehp > 0 and shp > 0:
        while enemyturn:
            randmove = random.randrange(1, 4)
            if randmove == 1:
                damage = (emove1 * eatk) // sdef
                print(enemyname + " used " + emove1name + " and dealt " + str(damage) + " damage")
                shp = shp - damage
                enemyturn = False
                starterturn = True
                if shp <= 0:
                    print(startername + " fainted!")
                    print(str(sname) + " blacked out")
                    pokemon_center = True
                else:
                    print(startername + " has " + str(ehp) + "  hp left")
                print("=" * 41)
                break
            elif randmove == 2:
                damage = (emove2 * eatk) // sdef
                print(enemyname + " used " + emove2name + " and dealt " + str(damage) + "  damage")
                shp = shp - damage
                enemyturn = False
                starterturn = True
                if shp <= 0:
                    print(startername + ", fainted!")
                    print(str(sname) + "black out!")
                    pokemon_center = True
                else:
                    print(startername + " has " + str(ehp) + "  hp left")
                print("=" * 41)
                break
            else:
                damage = (emove3 * eatk) // sdef
                print(enemyname + " used " + emove3name + " and dealt " + str(damage) + " damage")
                shp = shp - damage
                enemyturn = False
                starterturn = True
                if shp <= 0:
                    print(startername + " fainted!")
                    print(str(sname) + "blacked out!")
                    sys.exit()
                else:
                    print(startername + " has " + str(shp) + " hp left")
                print("=" * 41)
                break
            break
        while starterturn:
            print("What will " + startername + " do?")
            print("1-" + move1name)
            print("2-" + move2name)
            print("3-" + move3name)
            print("4- Use a Potion")
            wmove = int(input("Enter:\n"))
            print("-" * 41)
            if wmove == 1:
                damage = (move1 * satk) // edef
                print(startername + " used " + move1name + " and dealt " + str(damage) + " damage")
                ehp = ehp - damage
                starterturn = False
                enemyturn = True
                if ehp <= 0:
                    print(enemyname + " has fainted!")
                    print("Congratulations, " + str(sname) + " you have defeated " + str(
                        ename) + " and you are a winner!")
                    sys.exit()
                else:
                    print(enemyname + " has " + str(ehp) + " hp left")
                print("=" * 41)
                break
            elif wmove == 2:
                damage = (move2 * satk) // edef
                print("{0} used {1} and dealt {2} damage".format(startername, move2name, damage))
                ehp = ehp - damage
                starterturn = False
                enemyturn = True
                if ehp <= 0:
                    print(enemyname + " has fainted!")
                    print("Congratulations, {0} you have defeated {1} and you are the winner".format(sname, ename))
                    sys.exit()
                else:
                    print(enemyname + " has " + str(ehp) + " hp left")
                print("=" * 41)
                break
            elif wmove == 3:
                damage = (move3 * satk) // edef
                print("{0} used {1} and dealt {2} damage".format(startername, move3name, damage))
                ehp = ehp - damage
                starterturn = False
                enemyturn = True
                if ehp <= 0:
                    print(enemyname + " has fainted!")
                    print("Congratulations, {0} you have defeated {1} and you are the winner!".format(sname, ename))
                    sys.exit()
                else:
                    print(enemyname + " has " + str(ehp) + "  hp left")
                print("=" * 41)
                break
            elif wmove == 4:
                print("You used a potion!")
                print(startername + " was healed by 20 hp!")
                shp += 20
                if shp > 50:
                    shp = 50
                break
            else:
                print("Please input proper values.")
            break
    pygame.display.update()
