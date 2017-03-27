# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:55:22 2017

@author: pierre.aubinaud
"""
import combat
from random import randint



class action():
    def quit_d(self):
        global enemi,joueur
        print "%s can't find the way back home, and dies of starvation.\nR.I.P." % self.joueur.nom
        self.joueur.pv = 0
        
        
    def help_d(self): print Commands.keys()
      
      
    def status(self):
        global enemi,joueur
        print "%s's health: %d/%d" % (self.joueur.nom, self.joueur.pv, self.joueur.pv_max)
      
      
    def tired(self):
        global enemi,joueur
        print "%s feels tired." % self.joueur.nom
        self.joueur.pv = max(1, self.joueur.pv - 1)
        
        
    def rest(self):
        global enemi,joueur
        if self.joueur.state != 'normal': 
            print "%s can't rest now!" % self.joueur.nom
            self.joueur.type_action = None
            combat.combat_start(self.joueur,self.enemi)
        else:
          print "%s rests." % self.joueur.nom
          if randint(0, 1):
            self.enemi = [combat.ennemi_test,combat.ennemi_test,combat.ennemi_test,combat.ennemi_test]
            print "%s is rudely awakened by %s!" % (self.joueur.nom, self.enemi[0].nom)
            self.joueur.state = 'fight'
            self.joueur.type_action = None
            combat.combat_start(self.joueur,self.enemi)
          else:
            if self.joueur.pv < self.joueur.pv_max:
              self.joueur.pv = self.joueur.pv + 1
            else: print "%s slept too much." % self.joueur.nom; self.joueur.pv = self.joueur.pv - 1
            
            
    def explore(self):
        global enemi,joueur
        if self.joueur.state != 'normal':
          print "%s is too busy right now!" % self.joueur.nom
          self.joueur.type_action = None
          combat.combat_start(self.joueur,self.enemi)
        else:
          print "%s explores a twisty passage." % self.joueur.nom
          if randint(0, 1):
            self.enemi = [combat.ennemi_test,combat.ennemi_test,combat.ennemi_test,combat.ennemi_test]
            print "%s encounters %s!" % (self.joueur.nom, self.enemi[0].nom)
            self.joueur.state = 'fight'
          else:
            if randint(0, 1): action.tired(action())
            
            
    def flee(self):
        global enemi,joueur
        if self.joueur.state != 'fight': print "%s runs in circles for a while." % self.joueur.nom; self.action.tired(action())
        else:
          if randint(1, self.joueur.pv + 5) > randint(1, self.enemi[0].pv):
            print "%s flees from %s." % (self.joueur.nom, self.enemi[0].nom)
            self.enemi = None
            self.joueur.state = 'normal'
          else: 
              print "%s couldn't escape from %s!" % (self.joueur.nom, self.enemi[0].nom)
              self.joueur.type_action = None
              combat.combat_start(self.joueur,self.enemi)
          
          
    def attack(self):
        global enemi,joueur
        if self.joueur.state != 'fight': print "%s swats the air, without notable results." % self.joueur.nom; self.action.tired(action())
        else:
            self.joueur.action = raw_input("What is your attack ?")
            while 1:
                c=raw_input("What is your cible ?")
                if c == 1:
                    self.joueur.cible= self.enemi[0]
                    break
                if c == 2:
                    self.joueur.cible= self.enemi[1]
                    break
                if c == 3:
                    self.joueur.cible= self.enemi[2]
                    break
                if c == 4:
                    self.joueur.cible= self.enemi[3]
                    break
            self.joueur.type_action = "attaque"
            combat.combat_start(self.joueur,self.enemi)
            if self.enemi[0].pv+self.enemi[1].pv+self.enemi[2].pv+self.enemi[3].pv ==0:
                print "%s executes kill all the enemy!" % (self.joueur.nom)
                self.enemi = None
                self.joueur.state = 'normal'
                pass
            if self.joueur.cible.pv <= 0:
                print "%s executes %s!" % (self.joueur.nom, self.joueur.cible.nom)
                
                
while 1:
    p = raw_input("What is your character's classe? ")
    
    if p == "Mage":
        action.joueur=combat.Mage()
        break
    elif p == "Combattant":
        action.joueur=combat.Combattant()
        break
    elif p == "AssassinsMagique":
        action.joueur=combat.AssassinsMagique()
        break
    elif p == "AssassinsPhysique":
        action.joueur=combat.AssassinsPhysique()
        break
    elif p == "Archer":
        action.joueur=combat.Archer()
        break
    elif p == "Soigneur":
        action.joueur=combat.Soigneur()
        break

action.joueur.pv=action.joueur.pv_max
action.joueur.state = 'normal'
action.enemi = None


Commands = {
  'quit': action.quit_d,
  'help': action.help_d,
  'status': action.status,
  'rest': action.rest,
  'explore': action.explore,
  'flee': action.flee,
  'attack': action.attack,
  }


    
print "(type help to get a list of actions)\n"
print "%s enters a dark cave, searching for adventure." % action.joueur.nom
 
while(action.joueur.pv > 0):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands:
      if args[0] == c[:len(args[0])]:
        print c
        Commands[c](action())
        commandFound = True
        break
    if not commandFound:
      print "%s doesn't understand the suggestion." % action.joueur.nom