#Fichier contenant toutes les données du problème

from tools.temps_vecteur import *
from tools.constraints import *
from tools.CLE_class import *
import random as rng

# areas={"stock":Area("stock",500,{}),"transit":Area("transit",200,{}),"sortie_usine":Area("sortie_usine",100,{}),"atelier":Area("atelier",100,{}),"entree/sortie_CLE":Area("entree/sortie_CLE",100,{})}
# 
# ## version "à la main"
# 
# entries_1=[entry(12,"sortie_usine","nissan",15),entry(12,"sortie_usine","renault",16),entry(13,"sortie_usine","renault",15),entry(13,"sortie_usine","renault",17),entry(14,"sortie_usine","nissan",18)]
# 
# outs_1=[out(12,14,"entree/sortie_CLE","nissan"),out(13,19,"entree/sortie_CLE","nissan"),out(13,13,"entree/sortie_CLE","renault"),out(13,14,"entree/sortie_CLE","renault"),out(13,15,"entree/sortie_CLE","renault")]
# 
# in_ateliers_1=[in_atelier(12,"stock","atelier","nissan"),in_atelier(13,"stock","atelier","nissan"),in_atelier(12,"stock","atelier","renault"),in_atelier(12,"transit","atelier","renault"),in_atelier(13,"transit","atelier","renault")]
# 
# out_ateliers_1=[out_atelier(13,"stock","atelier","nissan"),out_atelier(14,"stock","atelier","nissan"),out_atelier(15,"stock","atelier","renault"),out_atelier(15,"transit","atelier","renault"),out_atelier(16,"transit","atelier","renault")]
# 
# ##1ere version automatique
# 
# total_minutes = 60 * 12
# 
# total_minutes = total_minutes//2
# 
# entries_2=[]
# outs_2=[]
# in_ateliers_2=[]
# out_ateliers_2=[]
# 
# for minute in range (0,total_minutes+1):
#     if rng.random() >= 0.5:
#         continue
#     if rng.random() >= 0.5:
#         modele = "renault"
#     else:
#         modele = "nissan"
#     if rng.random() >= 0.5:
#         if rng.random() >= 0.5:
#             entries_2 += [entry(12,"sortie_usine",modele,minute)]
#         else:
#             outs_2 += [out(minute,minute+15,"entree/sortie_CLE",modele)]
#     else:
#         if rng.random() >= 0.35:
#             in_ateliers_2 += [in_atelier(minute,"stock","atelier",modele)]
#         else:
#             out_ateliers_2 += [out_atelier(minute,"stock","atelier",modele)]
# 
# CLE_ESSAI_1=CLE(areas,dictionnaire_temps_vecteur,['sortie_usine'],[],['stock','transit']) #'entree/sortie_CLE'
# 
# ##2eme version automatique
# 
# #datas
# 
# heure_ouverture = 5
# heure_fermeture = 23
# temps_travail_minutes = (heure_fermeture - heure_ouverture) * 60
# 
# temps_chargement_camion_minutes = 2 * 60
# 
# #à partir du référentiel capacitaire
# 
# stock_renault_dispo = 9500
# stock_renault_occupe = 7500
# transit_renault_dispo = 3000
# transit_renault_occupe = 3000
# stock_nissan_dispo = 5000
# stock_nissan_occupe = 2000
# 
# place_dispo_total = 18000
# total_transit_dispo = 4500
# total_stock_dispo = place_dispo_total - total_transit_dispo
# 
# #valeurs arbitraires
# 
# place_usine = 500
# place_atelier = 850 #sature si en dessous de 750
# place_entree_sortie = 500
# proba_renault = 4/5
# 
# #semaine 41
# total_entree = 1400
# total_interne = 1300
# total_sortie = 300
# total_autres = 1500
# 
# #On suppose que "autres" = "interne" et que tous les internes sont soit des entree atelier, soit des sorties ateliers
# 
# total_entree_atelier = ( total_interne + total_autres ) //2
# total_sortie_atelier = ( total_interne + total_autres ) //2
# 
# liste_temps = range(0,temps_travail_minutes)
# 
# 
# 
# entries_3=[]
# for i in range(0,total_entree):
# 
#     chosen_minute = rng.choice(liste_temps)
# 
#     if rng.random()<proba_renault:
#         modele = "renault"
#     else:
#         modele = "nissan"
# 
#     entries_3 += [entry(chosen_minute,"sortie_usine",modele,1)] #1 correspond à la date prévue de sortie, ici mise arbitrairement
# 
# entries_3.sort(key = lambda current_constraint: current_constraint.entry_time )
# 
# 
# outs_3=[]
# for i in range(0,total_sortie):
# 
#     chosen_minute = rng.choice(liste_temps)
# 
#     if rng.random()<proba_renault:
#         modele = "renault"
#     else:
#         modele = "nissan"
# 
#     outs_3 += [out(chosen_minute,chosen_minute+temps_chargement_camion_minutes,"entree/sortie_CLE",modele)]
# 
# outs_3.sort(key = lambda current_constraint: current_constraint.outtime_min )
# 
# 
# in_ateliers_3=[]
# for i in range(0,total_entree_atelier):
# 
#     chosen_minute = rng.choice(liste_temps)
# 
#     if rng.random()<proba_renault:
#         modele = "renault"
#     else:
#         modele = "nissan"
# 
#     in_ateliers_3 += [in_atelier(chosen_minute,"stock","atelier",modele)]
# 
# in_ateliers_3.sort(key = lambda current_constraint: current_constraint.entry_time )
# 
# 
# out_ateliers_3=[]
# for i in range(0,total_sortie_atelier):
# 
#     chosen_minute = rng.choice(liste_temps)
# 
#     if rng.random()<proba_renault:
#         modele = "renault"
#     else:
#         modele = "nissan"
# 
#     out_ateliers_3 += [out_atelier(chosen_minute,"stock","atelier",modele)]
# 
# out_ateliers_3.sort(key = lambda current_constraint: current_constraint.out_time )
# 
# #remplissage initial
# 
# areas={"stock":Area("stock",total_stock_dispo,{}),"transit":Area("transit",total_transit_dispo,{}),"sortie_usine":Area("sortie_usine",place_usine,{}),"atelier":Area("atelier",place_atelier,{}),"entree/sortie_CLE":Area("entree/sortie_CLE",place_entree_sortie,{})}
# 
# CLE_ESSAI_3=CLE(areas,dictionnaire_temps_vecteur,['sortie_usine'],[],['stock','transit'])
# 
# CLE_ESSAI_3.areas["stock"].filling["nissan"] = stock_nissan_occupe
# CLE_ESSAI_3.areas["stock"].filling["renault"] = stock_renault_occupe
# CLE_ESSAI_3.areas["transit"].filling["renault"] = transit_renault_occupe
# CLE_ESSAI_3.areas["atelier"].filling["renault"] = 50
# CLE_ESSAI_3.areas["atelier"].filling["nissan"] = 50
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
