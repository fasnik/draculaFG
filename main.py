from assets.logo import Logo
from characters.dracula import Dracula
from characters.npc import NPC
from assets.gameover import GameOver

from random import randint
import sys

from pygame import Vector2, init, display, event, time, sprite, key
from pygame.locals import *

#CONSTANTS
NUM_NPCS = 2

# INIT PYGAME WINDOWS
jogo = init()
size = Vector2((1280,960))
janela = display.set_mode(size)
display.set_caption('Vampiro Doidão','VP')

#INIT CLOCK 
c = time.Clock()

#INIT OVERLAYS
logo = Logo()

# INIT PLAYER
dracula = Dracula(0, size.y)

#GROUPS
playerGroup = sprite.GroupSingle(dracula)
projectileGroup = sprite.GroupSingle(dracula.projectile)
npcGroup = sprite.Group()

# INIT NPCS
for i in range(NUM_NPCS):
    newnpc = NPC(randint(500,800), size.y)
    npcGroup.add(newnpc)


# GAME LOOP
isRunning = True
while isRunning:


    #EVENT FOR X SCREEN BUTTON WORKS
    for e in event.get():
            if e.type == QUIT: 
                sys.exit()

    #COLLIDE ACTIONS
    sprite.spritecollide(dracula, npcGroup, False, collided=dracula.collide_player_npc)
    sprite.spritecollide(dracula.projectile, npcGroup, True, collided=dracula.projectile.collide_projectile_npc)

    #FILL BACKGROUND
    janela.fill((0,0,0))
    janela.blit(logo.imag, size/2-Vector2((logo.imag.get_size()))/2)

    #GAMEOVER AND RESTART
    if dracula.lifebar.lifebar_life.width == 0:
        gameover = GameOver()
        janela.blit(gameover.surf, size/8)
        
        if key.get_pressed()[K_RETURN]:
            dracula.lifebar.update_size_life(dracula.lifebar.size_life.x)
           
            playerGroup.remove(dracula)
            projectileGroup.remove(dracula.projectile)
           
            dracula = Dracula(0, size.y)
           
            playerGroup.add(dracula)
            projectileGroup.add(dracula.projectile)
            
    #RUN GAME
    else:

        #DRAW ELEMENTS
        playerGroup.draw(janela)
        npcGroup.draw(janela)
        janela.blit(dracula.lifebar.lifebar_surf, dracula.lifebar.pos)
        
        if dracula.projectile.isProjectileActive:
            projectileGroup.draw(janela)

        #UPDATE ELEMENTS    
        playerGroup.update(janela)
        projectileGroup.update(janela)           
    
    display.flip() 