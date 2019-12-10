from tools import *

#Principe : A partir des contraintes, on effectue une série de tâches pour y répondre -> chaque tâche demande un temps t
#Sans tenir compte de limites temporelles/matérielles/humaines, on applique toutes ces tâches successives au CLE
#On somme enfin les durées de toutes les tâches pour obtenir un temps total de travail pour une journée
#A partir de ce temps total, on en déduit combien de jockeys sont nécessaires à faire fonctionner le CLE

#Pour l'instant, les contraintes de temps sont ignorées
#Il faudra aussi ajouter les contraintes liées aux Jockeys (disponibilité/ils se déplacent par 3 + 1 navette)



if __name__ == "__main__":

    CLE=CLE_ESSAI_1

    entries=entries_1
    outs=outs_1

    in_ateliers=in_ateliers_1
    out_ateliers=out_ateliers_1

    #régime de fonctionnement temporel

    for constraint in entries:
        CLE.apply_task(CLE.give_take_in_order(constraint.entry_area,constraint.model))



    CLE.affichage_remplissage()
    print(CLE.working_time)
