import pyxel
from math import *
import random
import time 


class Jeu:
    def __init__(self):
        
        pyxel.init(128, 128, title="Nuit du Code")
        
        self.debut = False
        
        self.velocity = 2
        
        self.scene = 1
        
        self.list_touche = [pyxel.KEY_A,pyxel.KEY_B,pyxel.KEY_C,pyxel.KEY_D,pyxel.KEY_E,pyxel.KEY_F,pyxel.KEY_G,pyxel.KEY_H,pyxel.KEY_I,pyxel.KEY_J,pyxel.KEY_K,pyxel.KEY_L,pyxel.KEY_M,pyxel.KEY_N,pyxel.KEY_O,pyxel.KEY_P,pyxel.KEY_Q,pyxel.KEY_R,pyxel.KEY_S,pyxel.KEY_T,pyxel.KEY_U,pyxel.KEY_V,pyxel.KEY_W,pyxel.KEY_X,pyxel.KEY_Y,pyxel.KEY_Z]
    
        self.timer = True
        self.start = time.time()
        self.time_left = None
        
        self.player_x = 64
        self.player_y = 64
        
        self.nombre_bonus = 0
        self.nombre_malus = 0
        self.nombre_rocher= 0
        self.nombre_rocher_indice = 0
        
        self.liste_bonus = []
        self.liste_malus = []
        self.liste_rocher = []
        self.liste_rocher_indice = []
        
        self.liste_indice_bin = []
        self.i = 0
        
        self.bonne_reponse = ""
        
        self.mots = ["code", "nuit", "papa", "loup"]
        
        pyxel.load("4.pyxres")
        
        pyxel.run(self.update, self.draw)
        
        
    #Distance entre deux objets
    def distance(self, x1, y1, x2, y2):
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    
    #Bouton start
    def debut_partie(self):
        if self.debut == False and pyxel.btn(pyxel.KEY_SPACE):
            self.debut = True
            
    #établir le code secret
    def convertir_mot_binaire(self):
        l = []
        d = self.mots[0].encode()
        for i in d:
            l.append(bin(i)[2:])
        return l
        
    
    #Déplacement du joueur   
    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x<115:
            self.player_x += self.velocity
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x>5:
            self.player_x += -self.velocity
        if pyxel.btn(pyxel.KEY_DOWN) and self.player_y<115:
            self.player_y += self.velocity
        if pyxel.btn(pyxel.KEY_UP) and self.player_y>5:
            self.player_y += -self.velocity
        
        
        
    # Création et contact avec les bonus
    def bonus_creation(self):
        if self.nombre_bonus < 3:
            self.liste_bonus.append([random.randint(10, 110), random.randint(20, 110)])
            self.nombre_bonus += 1 
    def bonus_contact(self):
        for bonus in self.liste_bonus:
            if self.distance(self.player_x, self.player_y, bonus[0], bonus[1]) <= 5:
                self.liste_bonus.remove(bonus)
           
           
           
    # Création et contact avec les bonus
    def malus_creation(self):
        if self.nombre_malus < 1:
            self.liste_malus.append([random.randint(10, 110), random.randint(20, 110)])
            self.nombre_malus += 1
    def malus_contact(self):
        for malus in self.liste_malus:
            if self.distance(self.player_x, self.player_y, malus[0], malus[1]) <= 5:
                self.liste_malus.remove(malus)
    
    
    
    #Création et contact avec les rochers 
    def rocher_creation(self):
        if self.nombre_rocher < 14:
            self.liste_rocher.append([random.randint(10, 110), random.randint(20, 110)])
            self.nombre_rocher += 1
    def rocher_contact(self):
        for rocher in self.liste_rocher:
            if self.distance(self.player_x, self.player_y, rocher[0], rocher[1]) <= 5:
                self.liste_rocher.remove(rocher)
                
                
                
    #Création et contact avec les rochers indice
    def rocher_indice_creation(self):
        if self.nombre_rocher_indice < 1:
            self.liste_rocher_indice.append([random.randint(10, 110), random.randint(20, 110)])
            self.nombre_rocher_indice += 1
    def rocher_indice_contact(self):
        for rocher_indice in self.liste_rocher_indice:
            if self.distance(self.player_x, self.player_y, rocher_indice[0], rocher_indice[1]) <= 5:
                self.liste_rocher_indice.remove(rocher_indice)
                self.liste_indice_bin.append(rocher_indice)

    
    
    # =====================================================
    # == UPDATE
    # =====================================================    
    def update(self):
        pyxel.load("4.pyxres")
        
        self.debut_partie()
            
        if self.debut == True :
            
            if self.scene == 1 and self.distance(self.player_x, self.player_y, 0, 15) < 8:
                self.scene = 2
                self.nombre_bonus = 0
                self.nombre_malus = 0
                self.nombre_rocher= 0
                self.nombre_rocher_indice = 0
                
                self.liste_bonus = []
                self.liste_malus = []
                self.liste_rocher = []
                self.liste_rocher_indice = []

                
            if self.scene == 2 and self.distance(self.player_x, self.player_y, 115, 15) < 8:
                self.scene = 1
                self.nombre_bonus = 0
                self.nombre_malus = 0
                self.nombre_rocher= 0
                self.nombre_rocher_indice = 0
                
                self.liste_bonus = []
                self.liste_malus = []
                self.liste_rocher = []
                self.liste_rocher_indice = []

            
                
            self.deplacement()
            
            self.bonus_creation()
             
            self.bonus_contact()
            
            self.malus_creation()
            
            self.malus_contact()
            
            self.rocher_creation()
            
            self.rocher_contact()
            
            self.rocher_indice_creation()
            
            self.rocher_indice_contact()
            
            
            
            #Le temps
            
            self.time_left = 60 - int(time.time() - self.start)
            if self.time_left >= 0:
                self.timer = False
                
        if self.time_left == 0:
            pyxel.quit()
            
    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        
        
        if self.debut == False:
            pyxel.cls(1)
            pyxel.text(2,45, f"Click on the space bar to start  ",7)
            pyxel.text(40,52, f" the game :) ",7)
            pyxel.rect(50,70,30,10,10)
            pyxel.text(55, 72, 'Start', pyxel.COLOR_BLACK)  
            
        
        else:
            
            ########################################################
            #Dessin paysage                
            if self.scene == 1: 
                pyxel.cls(1)
                pyxel.blt(self.player_x, self.player_y, 0, 1, 26, 5, 6)
                "la partie gauche du cadre jeu"
                for k in range (7):
                    pyxel.blt(0, k*10, 0, 9,217 , -6, 10)
                
                pyxel.blt(0,10 , 0, 8,0 , -6, 10)
                for t in range (5):
                    pyxel.blt(0, (t+7)*10, 0, 9,217 , -6, 10)
                    
                "la partie du bas du jeu"
                for m in range (16):
                    pyxel.blt(m*15, 119, 0, 9,217 , 20, 20)
            
                "la partie de droite"
                for i in range (14):
                    pyxel.blt(123, i*10, 0, 9,217 , 10, 20)
                "la partie haute"
                for l in range (25):
                    pyxel.blt(l*5,0,0, 9,217 , 5, 5)
            
            
            
            if self.scene == 2:
                pyxel.cls(3)
                pyxel.blt(self.player_x, self.player_y, 0, 1, 26, 5, 6)
                "la partie gauche du cadre jeu"
                for k in range (7):
                    pyxel.blt(0, k*10, 0, 9,217 , -6, 10)
                
                for t in range (5):
                    pyxel.blt(0, (t+7)*10, 0, 9,217 , -6, 10)
                    
                "la partie du bas du jeu"
                for m in range (16):
                    pyxel.blt(m*15, 119, 0, 9,217 , 20, 20)
            
                "la partie de droite"
                for i in range (14):
                    pyxel.blt(123, i*10, 0, 9,217 , 10, 20)
                
                pyxel.blt(122,20 , 0, 8,0 , 6, 10)    
            
                "la partie haute"
                for l in range (25):
                    pyxel.blt(l*5,0,0, 9,217 , 5, 5)
                    
                    
            
                
            ##################################################################   
            
            #Message à coté du coffre
            if self.distance(self.player_x, self.player_y, 6, 110)<= 15 and len(self.liste_indice_bin) == 4:
                    pyxel.text(8, 105, f"Saisissez le mot en lettre",7)
                    pyxel.text(45,110, f"miniscule",7)
                    
                    for i in range(26):
                        if pyxel.btnr(self.list_touche[i]) == True :
                            self.bonne_reponse += chr(97+i)
                                
                    pyxel.text(24,64,f"{self.bonne_reponse}", 7)
                    if self.bonne_reponse == "code":
                        pyxel.text(24,84,"bonne reponse", 7)
                            
        
                    
            
                    
                
            #Dessin des rochers indice avec texte
            if len(self.liste_indice_bin) == 1:
                pyxel.text(95,5 , f"{self.convertir_mot_binaire()[0]}", 7)
                if pyxel.btn(pyxel.KEY_C):
                    pyxel.text(64,64, "C", 7)
                
            if len(self.liste_indice_bin) == 2:
                pyxel.text(95,5 , f"{self.convertir_mot_binaire()[0]}", 7)
                pyxel.text(95,12 , f"{self.convertir_mot_binaire()[1]}", 7)
                
            if len(self.liste_indice_bin) == 3:
                pyxel.text(95,5 , f"{self.convertir_mot_binaire()[0]}", 7)
                pyxel.text(95,12 , f"{self.convertir_mot_binaire()[1]}", 7)
                pyxel.text(95,19 , f"{self.convertir_mot_binaire()[2]}", 7)
                
            if len(self.liste_indice_bin) == 4:
                pyxel.text(95,5 , f"{self.convertir_mot_binaire()[0]}", 7)
                pyxel.text(95,12 , f"{self.convertir_mot_binaire()[1]}", 7)
                pyxel.text(95,19 , f"{self.convertir_mot_binaire()[2]}", 7)
                pyxel.text(95,26, f"{self.convertir_mot_binaire()[3]}", 7)
                
            
            for rocher_indice in self.liste_rocher_indice:
                pyxel.blt(rocher_indice[0], rocher_indice[1], 0, 41, 169, 6,6)
            
            
            #Dessin des rochers
            for rocher in self.liste_rocher:
                pyxel.blt(rocher[0], rocher[1], 0, 41, 169, 6,6)
                
            
            #Dessin des malus
            for malus in self.liste_malus:
                pyxel.blt(malus[0], malus[1], 0, 49, 193, 6,6)
                self.time_left += 20
            
            #Dessin des bonus
            for bonus in self.liste_bonus:
                pyxel.blt(bonus[0], bonus[1], 0, 49, 193, 6,6)
                self.time_left -= 5

                
            #Le perso
            pyxel.blt(self.player_x, self.player_y, 0, 2, 18, 5, 6)
            if pyxel.btn(pyxel.KEY_RIGHT) :
               pyxel.blt(self.player_x, self.player_y, 0, 34, 18, 5, 6) 
            if pyxel.btn(pyxel.KEY_LEFT) :
               pyxel.blt(self.player_x, self.player_y, 0, 34, 26, 5, 6)
            if pyxel.btn(pyxel.KEY_DOWN) :
               pyxel.blt(self.player_x, self.player_y, 0,74 , 18, 5, 6)
            if pyxel.btn(pyxel.KEY_UP) :
               pyxel.blt(self.player_x, self.player_y, 0, 66, 17, 5, 6)
            
            #Coffre
            pyxel.blt(6,113, 0, 32, 201, 6, 6)
            
            #Timer
            pyxel.text(8, 5, 'Time left:', pyxel.COLOR_WHITE)
            pyxel.text(50, 5, str(self.time_left), pyxel.COLOR_RED)

Jeu()