#Fichier contenant toutes les données du problème

import temps_vecteur
import contraints

areas={"stock":Area("stock",500,{}),"transit":Area("transit",200,{}),"sortie_usine":Area("sortie_usine",0,{"clio":3, "zoé":50}),"atelier":Area("atelier",100,{}),"entree/sortie_CLE":Area("entree/sortie_CLE",100,{})}

entry=[]
out=[] #compléter avec constraints

CLE_ESSAI_1=CLE(areas,dictionnaire_input,entry,out)

#Test

Task_1=Task("sortie_usine","stock","clio",10)
CLE_ESSAI_1.apply_task(Task_1)