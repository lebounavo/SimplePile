# !/usr/bin/env python
# -*- coding: iso8859_10 -*-
#
#  MaPile.py
#  
#  Copyright 2019 AM4MM - lebounavo
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from os import system, name 	

def EffaceEcran(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        
# colored text and background 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

def saisie():
	prGreen (" Saisir [Exit] pour quitter, [Help] pour obtenir de l'aide ")
	sraw=raw_input(" Nouvel élément : ")
	sunicode=sraw.decode("utf-8")                      # decode str-> unicode
	ss=sunicode.split(".")
	if len(ss)==2:
		if ss[0].isnumeric() and ss[1].isnumeric():
			sss=float(sunicode)
		else:
			sss=str(sunicode)
	else:
		if sunicode.isnumeric():
			sss=int(sunicode)
		else:
			if sunicode.startswith("-"):
				if sunicode[len("-"):].isnumeric():
					sss=int(sunicode)
				else:
					sss=str(sunicode)
			else:
				sss=str(sunicode)
	return sss

def Aide():
 	
 	EffaceEcran()
 	
 	print("")
 	prGreen("------------------------------ COPYRIGHT --------------------------------------")
 	print("")
	prGreen("   Copyright 2019-06-001-AM4MM - lebounavo - 1er programme Python")
	print("")	
	prCyan("-------------------------------- AIDE -----------------------------------------")
	print("")
	print(" - Saisie de texte : Ajout du texte saisi (élémént) sur le dessus de la pile")
	print("")
	print(" - Saisie d'un nombre entier positif : déplacement de l'élément du dessus de")
	print("   la pile à l'emplacement saisi. Exemple : 2 --> l'élément #0 est positionné")
	print("   en 3ème position (élément #2)")
	print("")
	print(" - Saisie d'un nombre entier négatif : suppression de l'élément de la pile")
	print("   Exemple : -2 --> Suppression de l'élément #2 de la pile")
	print("")
	print(" - Saisie d'un nombre décimal : E.d")
	print("   E correspondant à la partie entière et d à la partie décimale")
	#print("   E > d : Interversion des éléments de la pile")
	#print("      Exemple : 3.1 --> Echange des éléments #1 et #3.")
	print("   Déplacement de l'éléments E à la position d de la pile")
	print("")
			
	prCyan("------------------------------ LICENCE ----------------------------------------")
	print("")
	print("   Ce programme est un logiciel libre : vous pouvez le redistribuer et/ou le")
	print("   modifier sous les termes de la Licence Publique Générale GNU telle que")
	print("   publiée par la Free Software Foundation ; soit la version 2 de la licence,")
	print("   soit (à votre choix) toute version ultérieure.")
	print("")
	print("   Ce programme est distribué dans l'espoir qu'il sera utile, mais SANS AUCUNE")
	print("   GARANTIE ; sans même la garantie implicite de COMMERCIALISABILITÉ ou")
	print("   APTITUDE À UN USAGE PARTICULIER. Voir la Licence Publique Générale GNU pour")
	print("   plus de détails.")
	print("") 
	print("   Vous devriez avoir reçu une copie de la Licence Publique Générale GNU avec")
	print("   ce programme. Si ce n'est pas le cas, écrivez au Logiciel Libre, 51 Franklin")
	print("   Street, Fifth Floor, Boston, MA 02110-1301, USA.")
	print("")
	SuiteAide=raw_input("   Version anglaise (O/N) : ")
	
	if SuiteAide=='O':
		EffaceEcran()
	 	
		print("")
		prGreen("------------------------------ COPYRIGHT --------------------------------------")
		print("")
		prGreen("   Copyright 2019-06-001-AM4MM - lebounavo - 1st Python program")
		print("")
		print("")
		prYellow("=========================== ENGLISH VERSION ===================================")
		print("")
		
		prCyan("-------------------------------- HELP -----------------------------------------")
		
		
		print(" - Text entry: Adding the entered text (element) to the top of the stack")
		print("")
		print(" - Entering a positive integer: moving the element from the top of the stack to")
		print("   the location entered. Example: 2 --> element #0 is positioned in 3rd")
		print("   position (element #2)")
		print("")
		print(" - Entering a negative integer: deleting the stack element")
		print("   Example: -2 --> Deleting element #2 from the stack")
		print("")
		print(" - Entering a decimal number: E.d")
		print(" E is the integer part and d is the decimal part")
		#print(" E > d: Swapping stack elements")
		#print(" Example: 3.1 --> Exchange of elements #1 and #3.")
		print(" Moving the element E to the position d of the stack")

		prCyan("------------------------------- LICENSE ---------------------------------------")
		print("")
		print("   This program is free software; you can redistribute it and/or modify it")
		print("   under the terms of the GNU General Public License as published by the Free")
		print("   Software Foundation; either version 2 of the License, or (at your option)")
		print("   any later version.")
		print("")
		print("   This program is distributed in the hope that it will be useful, but WITHOUT")
		print("   ANY WARRANTY ; without even the implied warranty of MERCHANTABILITY or")
		print("   FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for")
		print("   more details.")
		print("")
		print("   You should have received a copy of the GNU General Public License along with")
		print("   this program; if not, write to the Free Software Foundation, Inc., 51")
		print("   Franklin Street, Fifth Floor, Boston,MA 02110-1301, USA.")
		print("")
		
	else:
		EffaceEcran()
	
	return SuiteAide

#def Pile():	
fichier=open('MaPile.csv','r')
f=fichier.read()
l1=f.split('\n')
fichier.close


prCyan ("------------------------------------- Pile ------------------------------------")
for i,Tache in enumerate(l1):
	if Tache=="":
		del l1[i]
	else:
		if i==0:
			prYellow(str(i)+" - "+Tache)
		else:
			print(" "+str(i)+" - "+Tache)
print("")
s=saisie()

while s!="Exit":
	if s!="Help":
		if type(s)==type("aaa"):						#Insertion de tâche
			l1.insert(0,s)
		else:
			if type(s)==type(9):
				if s>=0:                   				#Déplacement de tâche
					l1.insert(s+1,l1[0])
					del l1[0]
				else:
					del l1[-len(l1)-s]    				#Supression de tâche
			else:
				if type(s)==type(1.1):
					#print type(s)
					ind1=str(s).split(".")
					#print(ind1)
					if int(ind1[0])>int(ind1[1]):
					#	#Echange des tâches
					#	s1=l1[int(ind1[0])]
					#	l1[int(ind1[0])]=l1[int(ind1[1])]
					#	l1[int(ind1[1])]=s1
						#Remontée de l'élément à la position souhaitée
						l1.insert(int(ind1[1]),l1[int(ind1[0])])
						del l1[int(ind1[0])+1]
					else:
						#Descente de l'élément à la position souhaitée
						l1.insert(int(ind1[1])+1,l1[int(ind1[0])])
						del l1[int(ind1[0])]
		EffaceEcran()
	else:
		Aide()		
	prCyan ("------------------------------------- Pile ------------------------------------")
	for i,Tache in enumerate(l1):
		if Tache=="":
			del l1[i]
		else:
			if i==0:
				prYellow(str(i)+" - "+Tache)
			else:
				print(" "+str(i)+" - "+Tache)
	print("")
	s=saisie()


fichier2=open('MaPile.csv','w')
for Tache in l1:
	fichier2.write(Tache+"\n")
fichier2.close
