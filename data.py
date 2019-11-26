#Fichier contenant toutes les données du problème

import temps_vecteur
import contraints

areas=[Area("stock",500,{}),Area("transit",200,{}),Area("sortie_usine",0,{}),Area("atelier",100,{}),Area("entree/sortie_CLE",100,{})]

entry=[entry(12,"entree/sortie_CLE","nissan",15),entry(12,"entree/sortie_CLE","renault",16),entry(13,"entree/sortie_CLE","renault",15),entry(13,"entree/sortie_CLE","renault",17),entry(14,"entree/sortie_CLE","nissan",18)]
out=[out(15,17,"entree/sortie_CLE","nissan"),out(16,19,"entree/sortie_CLE","nissan"),out(15,18,"entree/sortie_CLE","renault"),out(16,17,"entree/sortie_CLE","renault"),out(17,21,"entree/sortie_CLE","renault")] #compléter avec constraints

CLE_ESSAI_1=CLE(areas,dictionnaire_input,entry,out)
