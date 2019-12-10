#Fichier contenant toutes les données du problème

from tools.constraints import *
from tools.CLE_class import *

areas={"stock":Area("stock",500,{}),"transit":Area("transit",200,{}),"sortie_usine":Area("sortie_usine",0,{}),"atelier":Area("atelier",100,{}),"entree/sortie_CLE":Area("entree/sortie_CLE",100,{})}

entries_1=[entry(12,"sortie_usine","nissan",15),entry(12,"sortie_usine","renault",16),entry(13,"sortie_usine","renault",15),entry(13,"sortie_usine","renault",17),entry(14,"sortie_usine","nissan",18)]

outs_1=[out(12,14,"entree/sortie_CLE","nissan"),out(13,19,"entree/sortie_CLE","nissan"),out(13,13,"entree/sortie_CLE","renault"),out(13,14,"entree/sortie_CLE","renault"),out(13,15,"entree/sortie_CLE","renault")]

in_ateliers_1=[in_atelier(12,"stock","atelier","nissan"),in_atelier(13,"stock","atelier","nissan"),in_atelier(12,"stock","atelier","renault"),in_atelier(12,"transit","atelier","renault"),in_atelier(13,"transit","atelier","renault")]
out_ateliers_1=[out_atelier(13,"stock","atelier","nissan"),out_atelier(14,"stock","atelier","nissan"),out_atelier(15,"stock","atelier","renault"),out_atelier(15,"transit","atelier","renault"),out_atelier(16,"transit","atelier","renault")]

CLE_ESSAI_1=CLE(areas,dictionnaire_input,entry,out,['sortie_usine'],['entree/sortie_CLE'])
