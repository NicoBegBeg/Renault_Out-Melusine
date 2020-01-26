from Input_Handler import *
from tools import *
import random as rng


given_zones = give_zone()

input_areas= [ ( Area(x[0],int(x[2]),{"renault": int(x[3]) } ), x[1] ) for x in given_zones ]

given_organisation = give_organisation()

given_nb_jockey = [int(given_organisation[0])] + [i+1 for i in range(int(given_organisation[0]),int(given_organisation[1]))]

given_heure_ouverture = int(given_organisation[2])
given_heure_fermeture = int(given_organisation[3])

given_temps_dechargement_camions = int(given_organisation[4])
given_temps_chargement_camions = int(given_organisation[5])
given_temps_deplacement_atelier = int(given_organisation[6])
given_temps_deplacement_interne = int(given_organisation[7])

given_temps_vecteurs = give_temps_vecteurs()

given_taches = give_taches()

given_temps_travail_minutes = (given_heure_fermeture - given_heure_ouverture) * 60
liste_temps = range(0,given_temps_travail_minutes)

constraints_list = []

for taches in given_taches:
    origin_area = taches[0]
    destination_area = taches[1]

    if origin_area == "entree/sortie_route" or origin_area == "usine":
        possible_time = given_temps_dechargement_camions
    elif destination_area == "entree/sortie_route":
        possible_time = given_temps_chargement_camions
    elif origin_area == "atelier" or destination_area == "atelier":
        possible_time = given_temps_deplacement_atelier
    else:
        possible_time = given_temps_deplacement_interne

    amount = int(taches[2])

    for i in range(0,amount):
        chosen_minute = rng.choice(liste_temps)
        constraints_list.append(general_constraint(chosen_minute,origin_area,"renault",chosen_minute+possible_time,destination_area,1)) #1 correspond à la date prévue de sortie, ici mise arbitrairement

constraints_list.sort(key = lambda current_constraint: current_constraint.departure_time)