
# -*- coding: utf-8 -*-
import cases


class perso:
    def __init__(self, carte, pos):
        self.direction = "droite"
        self.pos = pos
        self.carte = cases.carte(10)
        
    def bouton_appuye(self, bouton):
        if bouton == self.direction:
            
            x=0
            y=0
            
            if self.direction == "haut":
                x = 0
                y = -1
            elif self.direction == "bas":
                x = 0 
                y = 1
            elif self.direction == "gauche":
                x = -1
                y = 0
            elif self.direction == "droite":
                x = 1
                y = 0
            if self.carte.matrice[self.pos[0]+x, self.pos[1]+y].marchable == True and self.carte.matrice[self.pos[0]+x, self.pos[1]+y].dessus == None:
                self.pos[0] += x
                self.pos[1] += y
                self.carte.matrice[x, y].dessus =  
        else:
            self.direction = bouton 
            
            
 
if __name__ == "__main__":
    p = perso([5, 5])
    