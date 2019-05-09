# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:11:54 2019

@author: vwork
"""
import serial.tools.list_ports
from tkinter import messagebox

class Port:
    def __init__(self): #Variable
        self.portsFound = Port.get_ports()
        self.baud = 9600
        
        
    def get_ports():
        """Renvoie la liste des périphériques connectés sur l'ordinateur"""
        ports = serial.tools.list_ports.comports()
        
        return ports
    
    def linkArduino(self):
        """Tentative de connection à la carte arduino"""
        nameFound = False
        commPort = 'None'

        while nameFound == False:
            try:
                numConnection = len(self.portsFound) #Nombre de périphérique détecté
                assert numConnection != 0 #Vérifie que la liste n'est pas nul
    
                for i in range(0,numConnection): #Cherche la carte
                    port = self.portsFound[i] #Sélectionne le port
                    strPort = str(port) #Convertie en chaine de caractère
                    if 'Arduino' in strPort: #Vérifie la présence de la carte
                        splitPort = strPort.split(' ') #Sépare les élements de la chaine de caractère
                        commPort = (splitPort[0]) #Récupère le nom du port où est connecté la carte
                
                assert commPort != 'None'        
                nameFound = True #On a trouver le nom du port de l'arduino
            
            except AssertionError: #Affiche un message d'erreur si la carte n'est reconnue sur aucun port
                messagebox.showerror("Erreur de connection", "La carte n'est reconnue sur aucun port de l'ordinateur. Veuillez vérifier la connection et appuyer sur OK")
        
        #On se connecter au port de l'arduino :
        connect = serial.Serial(commPort,baudrate = self.baud, timeout=1)
        print('Connected to '+commPort)
        return connect #Port de l'arduino
            
                    
