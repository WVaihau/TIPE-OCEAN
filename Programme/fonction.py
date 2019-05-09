# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:11:54 2019

@author: vwork
"""
import os
from tkinter import messagebox
#------Arduino Connection-------#
def CheckPort(): #Prototype bin_test-serial3.py
    """CETTE FONCTION VÉRIFIE QUE LA CARTE DE CONTRÔLE EST CONNECTÉE"""
    verif = False
    while verif == False:
        try:
            Listport = os.popen('python -m serial.tools.list_ports').readlines()
            os.system('exit')
            assert len(Listport)!= 0
            verif = True
        except AssertionError:
            messagebox.showerror("Erreur de connection", "La carte n'est reconnue sur aucun port de l'ordinateur. Veuillez vérifier la connection et appuyer sur OK")

    return Listport[0].split(' ')[0]