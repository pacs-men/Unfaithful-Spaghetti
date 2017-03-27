# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:20:28 2017

@author: pierre.aubinaud
"""

def popo_actif(self):
    potion=self.action
    if potion == "vie1": self.pv += 50
    
    if potion == "vie2": self.pv += 100
    
    if potion == "vie3": self.pv += 250
    
    if potion == "force1": self.atk += 50 
    self.mag += 50  
    self.force1 =2
    self.force1fois +=1
    
    if potion == "force2": self.atk +=100
    self.mag +=100
    self.force1 =2
    self.force2fois +=1
    
    if potion == "force3": self.atk +=150
    self.mag +=150
    self.force3 =1  #"tour"
    self.force3fois +=1
    
    if potion == "armure1": self.defend +=5
    self.res +=5
    self.armure1 =2 #"tour"
    self.armure1fois +=1
    
    if potion == "armure2": self.defend +=10
    self.res +=10
    self.armure2 =2 #"tour"
    self.armure2fois +=1
    
    if potion == "armure3": self.defend +=20
    self.res +=20
    self.armure3 =1 #"tour"
    self.armure3fois +=1
    
    if potion == "critique1": self.crit += 5
    self.critique1 =4 #"tour"
    self.critique1fois +=1
    
    if potion == "critique2": self.crit += 10
    self.critique2 =3#"tour"
    self.critique2fois +=1
    
    if potion == "critique3": self.crit += 15
    self.critique3 =2 #"tour"
    
    if potion == "vitesse": self.vit += 100
    self.vitesse =1 #"combat"
    self.vitessefois +=1
    
    if potion == "precision": self.prec += 15
    self.precision =1 #"combat"
    self.precisionfois +=1
    
    
def popo_def(self):
        if self.effet==True:
            if self.brulure > 0:
                self.pv -= 5
                self.brulure -= 1
            elif self.saignement > 0:
                self.pv -= 10
                self.saignement -= 1
            else:
                self.effet=False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    