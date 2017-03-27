# -*- coding: utf-8 -*-
import carte_test
import pygame
from pygame.locals import *


#==============================================================================
# map=cases.carte(10)
# map.matrice[x][y].afficher(i, j)
#==============================================================================




D=20
pygame.init()
fenetre=pygame.display.set_mode((640,640), RESIZABLE)
pygame.display.set_caption('Programme Pygame de base')

mape= carte_test.carte(D)




for x in range(10):
    for y in range(10):
        fenetre.blit(mape.get_image_case(x, y),(x*64, y*64))

continuer = 1       

while continuer:
     for event in pygame.event.get():
         if event.type == QUIT:
             continuer = 0       
pygame.display.flip()
#==============================================================================
# def haut():
#     global x,y
#     y+=2
#     draw(x,y)
# 
# def bas():
#     global x,y
#     y-=2
#     draw(x,y)
# 
# def droite():
#     global x,y
#     x-=2
#     draw(x,y)
#     
# def gauche():
#     global x,y
#     x+=2
#     draw(x,y)
# 
# def draw(x,y):
#     global carte
#     carte.delete(ALL)
# 
# for event in pygame.event.get():
# 	if event.type == QUIT:
# 		return
# 	elif event.type == KEYDOWN:
# 		if event.key == K_UP:
# 			haut()
# 		if event.key == K_DOWN:
# 			bas()			
# 	elif event.type == KEYUP:
# 		if event.key == K_UP or event.key == K_DOWN:
#	player.movepos = [0,0]
#			player.state = "still"
# continuer = 1
#
# 
# while continuer:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             continuer = 0
#==============================================================================
    
