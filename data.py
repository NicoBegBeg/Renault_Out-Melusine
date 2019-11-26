#Fichier contenant toutes les données du problème

import temps_vecteur
import contraints

areas=[Area("stock",500,{}),Area("transit",200,{}),Area("sortie_usine",0,{"clio":3, "zoé":50}),Area("atelier",100,{}),Area("entree/sortie_CLE",100,{})]

entry=[]
out=[] #compléter avec constraints

CLE_ESSAI_1=CLE(areas,dictionnaire_input,entry,out)

#Test

Task("sortie_usine","stock","clio",10)
