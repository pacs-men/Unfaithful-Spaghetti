# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
#==============================================================================
# import sys
# sys.path.append("C:\Users\nassim\Documents\GitHub\Unfaithful-Spaghetti\Jeu Pac s Men\combat")
# import combat
#==============================================================================

def deplacement():
    tkey=pygame.key.get_pressed()
    if tkey[K_LEFT]: 
        if x>0:            
            x-=1
    elif tkey[K_RIGHT]: 
        if x<taille_carte-D:
            x+=1
    elif tkey[K_UP]: 
        if y>0:            
            y-=1
    elif tkey[K_DOWN]: 
        if y<taille_carte-D:
            y+=1