import sys, pygame
import random
from pygame.locals import *
from math import *
import json
from tkinter import *

pygame.init()

WIDTH  = 1156
HEIGHT = 650
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS    = pygame.time.Clock()

pygame.display.set_caption('PyDeathRace')

menu1 = pygame.image.load('Recursos/Menu_Principal.jpg').convert()


def main():

   while True:
        
        #Test if the game has been quit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        SCREEN.blit(menu1,(0,0))



        pygame.display.update()
        FPS.tick(60)
        
if __name__ == '__main__': main()
