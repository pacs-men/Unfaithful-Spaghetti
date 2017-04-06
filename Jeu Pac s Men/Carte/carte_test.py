# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:40:25 2017

@author: Emeric Coudeville
"""
import pygame
from pygame.locals import *
import random


class carte:
    """ """
    def __init__(self, taille_mat):

        self.taille_mat = [taille_mat, taille_mat]

        self.dict_cases = {
                            "herbe1": herbe1(),
                            "herbe2": herbe2(),
                            "herbe3": herbe3(),
                            "herbe4": herbe4(),
                            "mur": mur(),
                            "arbre": arbre()
                          }

        self.matrice_case = [[[] for a in range(self.taille_mat[1])] for a in range(self.taille_mat[0])]
        choix_herbe=random.randrange(1,4)
        for x in range(self.taille_mat[0]):
            for y in range(self.taille_mat[1]):
                if choix_herbe==1:
                    self.matrice_case[x][y] = "herbe1"
                    choix_herbe=random.randrange(1,4)
                elif choix_herbe==2:
                    self.matrice_case[x][y] = "herbe2"
                    choix_herbe=random.randrange(1,4)
                elif choix_herbe==3:
                    self.matrice_case[x][y] = "herbe3"
                    choix_herbe=random.randrange(1,4)
                elif choix_herbe==4:
                    self.matrice_case[x][y] = "herbe4"
                    choix_herbe=random.randrange(1,4)


        for x in range(self.taille_mat[0]):
            print self.taille_mat
            self.matrice_case[x][0] = "mur"
            self.matrice_case[x][self.taille_mat[0]-1] = "mur"

        for y in range(self.taille_mat[1]):
            self.matrice_case[0][y] = "mur"
            self.matrice_case[self.taille_mat[1]-1][y] = "mur"

        self.list_objet = []

    def get_image_case(self, x, y):
        return self.dict_cases[self.matrice_case[x][y]].image

    def add_objet(self, x, y, objet):
        i

    def __repr__(self):
        ch = ""
        for x in range(self.taille_mat[0]):
            for y in range(self.taille_mat[1]):
                if self.matrice_chose[x][y] != None:
                    ch += self.matrice_chose[x][y].rep
                else:
                    ch += self.dict_cases[self.matrice_case[x][y]].rep
            ch += "\n"
        return ch



class case:
    def __init__(self):
        self.type = "case"
        self.marchable = True
        self.ouvrable = False
        self.chemin_image = ""
        self.rep = " "
        self.image = None

    def load_image(self):
        self.image = pygame.image.load(self.chemin_image).convert_alpha()

    def __repr__(self):
        if self.dessus == None:
            return self.rep
        else:
            return self.dessus.rep

    def __str__(self):
        return "case de type {} a la position {} \n marchable = {} ouvrable = {} l'image ce trouve en {}".format(
        self.type, self.pos, self.marchable, self.ouvrable, self.image)

class objet:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy


class herbe1(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe1"
      self.rep = "H"
      self.chemin_image = "Data/grass17.png"
      self.load_image()

class herbe2(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe2"
      self.rep = "H"
      self.chemin_image = "Data/grass04.png"
      self.load_image()

class herbe3(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe3"
      self.rep = "H"
      self.chemin_image = "Data/grass03.png"
      self.load_image()

class herbe4(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe4"
      self.rep = "H"
      self.chemin_image = "Data/grass02.png"
      self.load_image()

class mur(case):
    def __init__(self):
      case.__init__(self)
      self.type = "mur"
      self.marchable = False
      self.rep = "M"
      self.chemin_image = "Data/Mur.png"
      self.load_image()

class arbre(case):
    def _init_(self):
      case.__init__(self)
      self.type = "arbre"
      self.marchable = False
      self.rep = "A"
      self.chemin_image = "Data/sprite_00.png"
      self.load_image()


if __name__ == "__main__":
    a = carte(10)
    print(a)
    print a .get_image_case(2, 2)