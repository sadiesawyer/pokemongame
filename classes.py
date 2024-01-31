import pygame

pygame.init()

# creating our global variables for the different levels(scenes) of the game

global run
global pokemon_center
global town
global house1
global battle

# directions
print("""Directions:
Use the arrow keys to walk; hold B to run.
Walk up to someone to talk to them.

You should go battle your rival! 
""")

# game screen setup <3
win = pygame.display.set_mode((800, 800))
WINDOWWIDTH = 800
WINDOWHEIGHT = 800

# LOAD IN OUR IMAGES
pygame.display.set_caption("Pokemon Pink")
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'),
             pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'),
             pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'),
            pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'),
            pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png')]
walkUp = [pygame.image.load('images/B1.png'), pygame.image.load('images/B2.png'), pygame.image.load('images/B3.png'),
          pygame.image.load('images/B1.png'), pygame.image.load('images/B2.png'), pygame.image.load('images/B3.png'),
          pygame.image.load('images/B1.png'), pygame.image.load('images/B2.png'), pygame.image.load('images/B3.png')]
walkDown = [pygame.image.load('images/F1.png'), pygame.image.load('images/F2.png'), pygame.image.load('images/F3.png'),
            pygame.image.load('images/F1.png'), pygame.image.load('images/F2.png'), pygame.image.load('images/F3.png'),
            pygame.image.load('images/F1.png'), pygame.image.load('images/F2.png'), pygame.image.load('images/F3.png')]
bg = pygame.image.load('images/background2.png')
pokeitem = pygame.image.load('images/item.png')
pokemoncenterbg = pygame.image.load('pokemoncenterbg.png')
professor = pygame.image.load('images/professor.png')
char = pygame.image.load('images/playerstanding.png')
rivaldude = pygame.image.load('images/enemy.png')
nursepic = pygame.image.load('nurse.png')
background = pygame.image.load('images/pink.png')
house1bg = pygame.image.load('house1.png')
background_rect = background.get_rect()
title = pygame.image.load('images/title.png')
battle_cr = pygame.image.load('battle_cr.png')

# these are the values for the colors i'll be using
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

# some stuff for collision detection
abletoup = True
abletodown = True
abletoleft = True
abletoright = True


# a function to draw text to the screen
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


# the function for the menu to run

def menu():
    win.blit(background, background_rect)
    win.blit(title, (140, 100))
    draw_text(win, "PRESS [ENTER] TO BEGIN", 45, 400, 600, blue)
    draw_text(win, "PRESS [Q] TO QUIT", 45, 400, 650, blue)
    pygame.display.update()
    menu_run = True
    while menu_run:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
