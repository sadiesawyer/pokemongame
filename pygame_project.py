import pygame  # importing modules
import time
import os
import random
import sys
from classes import *  # import
from pokemon import *

pygame.init()


# this is our main character's setup

class Player(object):
    def __init__(self, x, y, width, height):  # initializing him and all his values
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.hitbox = pygame.Rect(self.x + 20, self.y, 28, 60)

    def draw(self, win):  # his animations
        global abletoup
        global abletodown
        global abletoleft
        global abletoright

        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        elif self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            if abletoleft:
                self.walkCount += 1
                man.x -= man.vel
                abletoright = True
                abletoup = True
                abletodown = True
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            if abletoright:
                self.walkCount += 1
                man.x += man.vel
                abletoleft = True
                abletodown = True
                abletoup = True
        elif self.up:
            win.blit(walkUp[self.walkCount // 3], (self.x, self.y))
            if abletoup:
                self.walkCount += 1
                man.y -= man.vel
                abletodown = True
                abletoright = True
                abletoleft = True
        elif self.down:
            win.blit(walkDown[self.walkCount // 3], (self.x, self.y))
            if abletodown:
                self.walkCount += 1
                man.y += man.vel
                abletoup = True
                abletoright = True
                abletoleft = True
        else:
            win.blit(char, (self.x, self.y))
        self.hitbox = pygame.Rect(self.x + 12, self.y + 8, 40, 55)


# setting up an item

class Item(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collected = False
        self.itemhitbox = pygame.Rect(self.x, self.y, 35, 35)

    def draw(self, win):
        if not potion.collected:
            win.blit(pokeitem, (self.x, self.y))
        if potion.itemhitbox.colliderect(man.hitbox):
            potion.collected = True
            print("You picked up a Potion!")


# SETUP FOR ALL THE TYPES OF NPCS
class Npc(object):
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.box = pygame.Rect(self.x + 12, self.y + 8, 40, 55)


# updating the game screen once every frame

def redrawgamewindow():
    global town
    global battlego
    battlego = False
    if town:
        win.blit(bg, (0, 0))
        potion.draw(win)
        rival.draw(win)
        man.draw(win)
    if pokemon_center:
        win.blit(pokemoncenterbg, (0, 0))
        man.draw(win)
        nurse.draw(win)
    if house1:
        win.blit(house1bg, (0, 0))
        man.draw(win)
    if battle:
        man.x = 400
        man.y = 650
        battle_func()
    pygame.display.update()


# MAIN LOOP

# defining our sprites as instances of the object classes we created

man = Player(400, 650, 64, 64)  # their x, y, width and height go here
potion = Item(180, 90, 30, 30)
rival = Npc(500, 400, 64, 64, rivaldude)  # here i made it so you specify the image
nurse = Npc(370, 221, 64, 64, nursepic)
run = True
town = True
pokemon_center = False
house1 = False
menu()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock = pygame.time.Clock()
    clock.tick(70)  # this sets the framerate
    speed = 0
    key = pygame.key.get_pressed()
    # create all of the hitboxes

    if town:
        pokemon_center = False
        house1 = False
        battle = False

        man.hitbox = pygame.draw.rect(win, blue, man.hitbox, 2)
        pokecenter = pygame.Rect(200, 520, 158, 159)
        pokemart = pygame.Rect(520, 140, 158, 139)
        mart_entrance = pygame.Rect(560, 230, 40, 60)
        center_entrance = pygame.Rect(240, 615, 42, 70)
        house1rect = pygame.Rect(160, 162, 158, 159)
        house1_entrance = pygame.Rect(200, 270, 40, 60)
        house2rect = pygame.Rect(560, 522, 158, 159)
        house2_entrance = pygame.Rect(600, 631, 40, 54)
        trees1 = pygame.Rect(0, 0, 85, 400)
        trees2 = pygame.Rect(0, 475, 85, 300)
        trees3 = pygame.Rect(715, 0, 100, 320)
        trees4 = pygame.Rect(715, 480, 100, 280)
        rivalbox = pygame.draw.rect(win, white, [rival.x + 12, rival.y + 8, 40, 50], 2)

        if man.hitbox.colliderect(center_entrance):
            man.x = 375
            man.y = 700
            pokemon_center = True
            town = False
        if man.hitbox.colliderect(mart_entrance):
            print("The Pokemart in this town is closed right now. Try again later!")
            man.y += 5
        if man.hitbox.colliderect(house2_entrance):
            print("The door to this house is locked.")
            man.y += 5
        if man.hitbox.colliderect(house1_entrance):
            town = False
            house1 = True
            man.x = 370
            man.y = 630
        if man.hitbox.colliderect(rivalbox):
            town = False
            win.fill((0, 0, 0))
            battle = True
        if man.y > 800 - man.height - man.vel or man.y < 5 or man.x < 5 or man.x > 800 - man.width - man.vel:
            print("You can't go this way yet!")

        # player is walking
        if not man.hitbox.colliderect(pokecenter) or man.hitbox.colliderect(pokemart) or man.hitbox.colliderect(house1rect) or man.hitbox.colliderect(house2rect) or man.hitbox.colliderect(rivalbox) or man.hitbox.colliderect(trees1) or man.hitbox.colliderect(trees2) or man.hitbox.colliderect(trees3) or man.hitbox.colliderect(trees4):
            if key[pygame.K_LEFT] and man.x > man.vel:
                man.left = True
                man.right = False
                man.up = False
                man.down = False
            elif key[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
                man.left = False
                man.right = True
                man.up = False
                man.down = False
            elif key[pygame.K_UP] and man.y > man.vel:
                man.left = False
                man.right = False
                man.up = True
                mandown = False
            elif key[pygame.K_DOWN] and man.y < 800 - man.height - man.vel:
                man.left = False
                man.right = False
                man.up = False
                man.down = True
            else:
                man.left = False
                man.right = False
                man.up = False
                man.down = False
                man.walkCount = 0

        # collision detection
        if man.hitbox.colliderect(pokecenter) or man.hitbox.colliderect(house1rect) or man.hitbox.colliderect(
                pokemart) or man.hitbox.colliderect(house2rect) or man.hitbox.colliderect(
            rivalbox) or man.hitbox.colliderect(trees1) or man.hitbox.colliderect(trees2) or man.hitbox.colliderect(
            trees3) or man.hitbox.colliderect(trees4):
            hit = True
            if hit:
                keys = pygame.key.get_pressed()  # See which keys are pressed
                if keys[pygame.K_UP]:
                    man.y += 2
                    abletoup = False
                    abletoleft = False
                    abletoright = False
                if keys[pygame.K_LEFT]:
                    man.x += 2
                    abletoleft = False
                    abletoup = False
                    abletodown = False
                if keys[pygame.K_DOWN]:
                    man.y -= 2
                    abletodown = False
                    abletoleft = False
                    abletoright = False
                if keys[pygame.K_RIGHT]:
                    man.x -= 2
                    abletoright = False
                    abletoup = False
                    abletodown = False

    if pokemon_center:
        man.up = True
        nursehitbox = pygame.Rect(nurse.x + 12, nurse.y + 8, 40, 120)
        if man.hitbox.colliderect(nursehitbox):
            hit2 = True
            man.up = False
            poke_q = input("Hi there, do you wish to heal your Pokemon?").lower()
            if poke_q == "yes":
                print("Okay, one second")
                shp = 30
                time.sleep(1)
                print("You're all set! Stay safe out there!")
            else:
                print("Okay! Come again soon!")
            man.down = True
            if man.y == 780:
                man.down = False
            town = True
            man.x = 220
            man.y = 680
            pokemon_center = False

    if house1:
        # collision
        table = pygame.Rect(475, 423, 125, 160)
        topwall = pygame.Rect(0, 0, 800, 235)
        furniture = pygame.Rect(460, 136, 300, 150)
        bed = pygame.Rect(25, 225, 205, 160)
        dresser = pygame.Rect(27, 348, 60, 280)
        house_exit = pygame.Rect(346, 710, 100, 70)

        # walking boundaries
        if not man.hitbox.colliderect(table) and not man.hitbox.colliderect(topwall) and not man.hitbox.colliderect(
                furniture) and not man.hitbox.colliderect(bed) and not man.hitbox.colliderect(dresser):
            if key[pygame.K_LEFT] and man.x > 15:
                man.left = True
                man.right = False
                man.up = False
                man.down = False
            elif key[pygame.K_RIGHT] and man.x < 785 - man.width - man.vel:
                man.left = False
                man.right = True
                man.up = False
                man.down = False
            elif key[pygame.K_UP] and man.y > man.vel:
                man.left = False
                man.right = False
                man.up = True
                mandown = False
            elif key[pygame.K_DOWN] and man.y < 785 - man.height - man.vel:
                man.left = False
                man.right = False
                man.up = False
                man.down = True
            else:
                man.left = False
                man.right = False
                man.up = False
                man.down = False
                man.walkCount = 0
        if man.hitbox.colliderect(house_exit):
            man.x = 230
            man.y = 300
            town = True
            house1 = False
        if man.hitbox.colliderect(table) or man.hitbox.colliderect(topwall) or man.hitbox.colliderect(
                furniture) or man.hitbox.colliderect(bed) or man.hitbox.colliderect(dresser):
            hit = True
            if hit:
                keys = pygame.key.get_pressed()  # See which keys are pressed
                if keys[pygame.K_UP]:
                    man.y += 2
                    abletoup = False
                    abletoleft = False
                    abletoright = False
                if keys[pygame.K_LEFT]:
                    man.x += 2
                    abletoleft = False
                    abletoup = False
                    abletodown = False
                if keys[pygame.K_DOWN]:
                    man.y -= 2
                    abletodown = False
                    abletoleft = False
                    abletoright = False
                if keys[pygame.K_RIGHT]:
                    man.x -= 2
                    abletoright = False
                    abletoup = False
                    abletodown = False

    redrawgamewindow()
pygame.quit()
