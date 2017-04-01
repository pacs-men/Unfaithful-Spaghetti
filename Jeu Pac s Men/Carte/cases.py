# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *


class carte:
    def __init__(self, taille_mat, fenetre):
        
        
        self.matrice = [[[] for a in range(taille_mat)] for a in range(taille_mat)]
        for x in range(taille_mat):
            for y in range(taille_mat):
                self.matrice[x][y] = herbe([x, y], fenetre)
                


         
        
                


class case:
    def __init__(self):
        self.type = "case"
        self.marchable = True
        self.ouvrable = False
        self.chemin_image = ""
        self.rep = " "
        self.dessus = None
 
    def __repr__(self):
        if self.dessus == None:
            return self.rep
        else:    
            return self.dessus.rep
        
    def __str__(self):
        return "case de type {} a la position {} \n marchable = {} ouvrable = {} l'image ce trouve en {}".format(
        self.type, self.pos, self.marchable, self.ouvrable, self.image)
    
class herbe(case):
    def __init__(self, pos, fenetre):
      case.__init__(self, pos, fenetre)
      self.type = "herbe"
      self.rep = "H"
      self.chemin_image = "Data/herbe.png"
      self.load_png(self.chemin_image)
class mur(case):
    def __init__(self, pos, fenetre):
      case.__init__(self, pos, fenetre)
      self.type = "mur"
      self.marchable = False
      self.rep = "M"
      self.chemin_Image = "Data/Mur.png"
      

        
if __name__ == "__main__":
    a = carte(10)
    print(a.matrice)
    