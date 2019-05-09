# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:11:54 2019

@author: vwork
--Main Code--
"""

import fonction as f

# Variables
n = 50 
values = [0 for i in range(0,n+1)]
bauds = 9600 #débit de données en bits/s pour la transmission de données en série
f.plt.ion() #Active le mode d'intéraction de matplotlib : ON
cnt=0 #Compteur

serialArduino = f.Port.linkArduino(f.Port()) # Connexion au port de l'arduino

while True:
    while (serialArduino.inWaiting()==0):
        #Tant que tu ne reçois aucune donnée tu ne fait rien
        pass
    
    valueRead = f.serialArduino.readline() # Lis les données envoyé par la carte

    try: # Vérifie que les données peuvent être afficher
        valueInInt = int(valueRead) 
        if valueInInt <= 1024: # Plage du capteur 
            if valueInInt >= 0:
                values.append(valueInInt)
                values.pop(0) 
                f.drawnow(f.plotValues(values)) # Afficher le graphique dynamique
                plt.pause(.000001) # Éviter les crash sur drawnow
            else:
                print("Invalid! negative number")
        else:
            print("Invalid! too large")
    except ValueError:
        print("Invalid! cannot cast")
