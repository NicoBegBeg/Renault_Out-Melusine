from tools import *
from Jockey_class import *
from data_from_input import *

#Principe : A partir des contraintes, on effectue une série de tâches pour y répondre -> chaque tâche demande un temps t
#Sans tenir compte de limites temporelles/matérielles/humaines, on applique toutes ces tâches successives au CLE
#On somme enfin les durées de toutes les tâches pour obtenir un temps total de travail pour une journée
#A partir de ce temps total, on en déduit combien de jockeys sont nécessaires à faire fonctionner le CLE

#Pour l'instant, les contraintes de temps sont ignorées
#Il faudra aussi ajouter les contraintes liées aux Jockeys (disponibilité/ils se déplacent par 3 + 1 navette)



if __name__ == "__main__":

    CLE=CLE(input_areas,given_temps_vecteurs)
    CLE_Jockey_pool = Jockey_pool(given_nb_jockey)

    #régime de fonctionnement temporel

    to_do=[]
    late=[]

    for m in liste_temps:
        
        for constraint in constraints_list:
            if constraint.departure_time <= m:
                to_do.append(constraint)
                constraints_list.remove(constraint)

        for constraint in to_do:
            order=CLE.give_order(constraint)
            if order!=False and CLE_Jockey_pool.dispo():
                
                if m>constraint.latest_possible_arrival_time:
                    late.append(m-constraint.latest_possible_arrival_time)

                else :
                    order_time=CLE.apply_task(order)
                    CLE_Jockey_pool.working(order_time)
                
                to_do.remove(constraint)
        
        CLE_Jockey_pool.refresh()

    CLE.affichage_remplissage()
    
    print("Temps total travaillé, en minutes : "+str(CLE.working_time))
    print("Temps total travaillé, en heures : "+str(CLE.working_time/60))
    
    print("Nombre de tâches toujours en attente à la fin de la journée = "+str(len(to_do)))
    
    if late!=[]:
        print("Nombre de tâche en retards pendant la journée = "+str(len(late)))
        print("Retard moyen = "+str(sum(late)/len(late)))
    else :
        print('Pas de retard')
