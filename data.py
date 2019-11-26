#Fichier contenant toutes les données du problème

from temps_vecteur import *
from contraints import *
from CLE_class import *

areas=[Area("stock",500,{}),Area("transit",200,{}),Area("sortie_usine",0,{}),Area("atelier",100,{}),Area("entree/sortie_CLE",100,{})]

entries=[entry(12,"entree/sortie_CLE","nissan",15),entry(12,"entree/sortie_CLE","renault",16),entry(13,"entree/sortie_CLE","renault",15),entry(13,"entree/sortie_CLE","renault",17),entry(14,"entree/sortie_CLE","nissan",18)]
outs=[out(12,14,"entree/sortie_CLE","nissan"),out(13,19,"entree/sortie_CLE","nissan"),out(13,13,"entree/sortie_CLE","renault"),out(13,14,"entree/sortie_CLE","renault"),out(13,15,"entree/sortie_CLE","renault")] #compléter avec constraints

inaterliers=[inatelier(12,"stock","atelier","nissan"),inatelier(13,"stock","atelier","nissan"),inatelier(12,"stock","atelier","renault"),inatelier(12,"transit","atelier","renault"),inatelier(13,"transit","atelier","renault")]
outateliers=[outatelier(13,"stock","atelier","nissan"),outatelier(14,"stock","atelier","nissan"),outatelier(15,"stock","atelier","renault"),outatelier(15,"transit","atelier","renault"),outatelier(16,"transit","atelier","renault")]

CLE_ESSAI_1=CLE(areas,dictionnaire_input,entry,out)
