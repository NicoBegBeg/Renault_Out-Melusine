# Première instance : 1 zone de stock, 1 zone de transit, 1 zone de sortie d'usine, 1 zone d'entree/sortie du CLE, 1 atelier

dictionnaire_temps_vecteur = {"stock":{},"transit":{}, "sortie_usine":{}, "atelier":{}, "entree/sortie_CLE":{}}

dictionnaire_temps_vecteur["stock"]["stock"] = 0 # pas forcément nul : on peut juste la changer de place
dictionnaire_temps_vecteur["stock"]["transit"] = 4
dictionnaire_temps_vecteur["stock"]["atelier"] = 6
dictionnaire_temps_vecteur["stock"]["sortie_usine"] = 5
dictionnaire_temps_vecteur["stock"]["entree/sortie_CLE"] = 8

dictionnaire_temps_vecteur["transit"]["stock"] = 4
dictionnaire_temps_vecteur["transit"]["transit"] = 0
dictionnaire_temps_vecteur["transit"]["atelier"] = 3
dictionnaire_temps_vecteur["transit"]["sortie_usine"] = 2
dictionnaire_temps_vecteur["transit"]["entree/sortie_CLE"] = 2

dictionnaire_temps_vecteur["atelier"]["stock"] = 6
dictionnaire_temps_vecteur["atelier"]["transit"] = 3
dictionnaire_temps_vecteur["atelier"]["atelier"] = 0
dictionnaire_temps_vecteur["atelier"]["sortie_usine"] = 10
dictionnaire_temps_vecteur["atelier"]["entree/sortie_CLE"] = 10

dictionnaire_temps_vecteur["sortie_usine"]["stock"] = 5
dictionnaire_temps_vecteur["sortie_usine"]["transit"] = 2
dictionnaire_temps_vecteur["sortie_usine"]["atelier"] = 10
dictionnaire_temps_vecteur["sortie_usine"]["sortie_usine"] = 0
dictionnaire_temps_vecteur["sortie_usine"]["entree/sortie_CLE"] = 10

dictionnaire_temps_vecteur["entree/sortie_CLE"]["stock"] = 8
dictionnaire_temps_vecteur["entree/sortie_CLE"]["transit"] = 2
dictionnaire_temps_vecteur["entree/sortie_CLE"]["atelier"] = 10
dictionnaire_temps_vecteur["entree/sortie_CLE"]["sortie_usine"] = 10
dictionnaire_temps_vecteur["entree/sortie_CLE"]["entree/sortie_CLE"] = 0

# données de Mardi pour la semaine 35

# dictionnaire_input["sortie_usine"]["transit"] donne le nombre de véhicules qui arrivent depuis la sortie de l'usine et qu'il stocker en transit

dictionnaire_input ={"sortie_usine":{"stock":4+11+16+3+8+2,"transit":18+25+3+7}, "entree/sortie_CLE":{"stock":310+3+24+19+3+4+8,"transit":17+3+9+11}}

# on suppose que les véhicules partent forcément du CLE depuis un zone de transit ?
# en fait je suis pas sûr de comprendre les données

output = 10 + 5 + 8

if __name__ == "__main__":
    for nom,val in dictionnaire_temps_vecteur.items():
        print(nom, " ", val)










