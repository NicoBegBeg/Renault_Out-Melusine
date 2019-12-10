#Fichier contenant toutes les données du problème

from tools.constraints import *
from tools.CLE_class import *
import random as rng

areas={"stock":Area("stock",500,{}),"transit":Area("transit",200,{}),"sortie_usine":Area("sortie_usine",100,{}),"atelier":Area("atelier",100,{}),"entree/sortie_CLE":Area("entree/sortie_CLE",100,{})}

entries_1=[entry(12,"sortie_usine","nissan",15),entry(12,"sortie_usine","renault",16),entry(13,"sortie_usine","renault",15),entry(13,"sortie_usine","renault",17),entry(14,"sortie_usine","nissan",18)]

outs_1=[out(12,14,"entree/sortie_CLE","nissan"),out(13,19,"entree/sortie_CLE","nissan"),out(13,13,"entree/sortie_CLE","renault"),out(13,14,"entree/sortie_CLE","renault"),out(13,15,"entree/sortie_CLE","renault")]

in_ateliers_1=[in_atelier(12,"stock","atelier","nissan"),in_atelier(13,"stock","atelier","nissan"),in_atelier(12,"stock","atelier","renault"),in_atelier(12,"transit","atelier","renault"),in_atelier(13,"transit","atelier","renault")]

out_ateliers_1=[out_atelier(13,"stock","atelier","nissan"),out_atelier(14,"stock","atelier","nissan"),out_atelier(15,"stock","atelier","renault"),out_atelier(15,"transit","atelier","renault"),out_atelier(16,"transit","atelier","renault")]


total_minutes = 60 * 12

total_minutes = total_minutes//2

entries_2=[]
outs_2=[]
in_ateliers_2=[]
out_ateliers_2=[]

for minute in range (0,total_minutes+1):
    if rng.random() >= 0.5:
        continue
    if rng.random() >= 0.5:
        modele = "renault"
    else:
        modele = "nissan"
    if rng.random() >= 0.5:
        if rng.random() >= 0.5:
            entries_2 += [entry(12,"sortie_usine",modele,minute)]
        else:
            outs_2 += [out(minute,minute+15,"entree/sortie_CLE",modele)]
    else:
        if rng.random() >= 0.5:
            in_ateliers_2 += [in_atelier(minute,"stock","atelier",modele)]
        else:
            out_ateliers_2 += [out_atelier(minute,"stock","atelier",modele)]

CLE_ESSAI_1=CLE(areas,dictionnaire_input,entry,out,['sortie_usine'],[]) #'entree/sortie_CLE'
