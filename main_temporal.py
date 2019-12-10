from tools import *
from Jockey_class import *

#Principe : A partir des contraintes, on effectue une série de tâches pour y répondre -> chaque tâche demande un temps t
#Sans tenir compte de limites temporelles/matérielles/humaines, on applique toutes ces tâches successives au CLE
#On somme enfin les durées de toutes les tâches pour obtenir un temps total de travail pour une journée
#A partir de ce temps total, on en déduit combien de jockeys sont nécessaires à faire fonctionner le CLE

#Pour l'instant, les contraintes de temps sont ignorées
#Il faudra aussi ajouter les contraintes liées aux Jockeys (disponibilité/ils se déplacent par 3 + 1 navette)



if __name__ == "__main__":

    T=24*60
    Nb_Jockeys=20 #à passer dans data à terme

    CLE=CLE_ESSAI_1
    Jockey_pool = Jockey_pool(Nb_Jockeys)

    entries=entries_1
    outs=outs_1

    in_ateliers=in_ateliers_1
    out_ateliers=out_ateliers_1

    #régime de fonctionnement temporel

    to_do_in=[]
    to_do_in_atelier=[]
    to_do_out=[]
    to_do_out_atelier=[]
    late=[]

    for m in range(T):
        for constraint in entries:
            if constraint.out_date <= m:
                to_do_in.append(constraint)
                entries.remove(constraint)
        
        for constraint in in_ateliers:
            if constraint.entry_time <= m:
                to_do_in_atelier.append(constraint)
                in_ateliers.remove(constraint)
        
        for constraint in out_ateliers:
            if constraint.out_time <= m:
                to_do_out_atelier.append(constraint)
                out_ateliers.remove(constraint)
        
        for constraint in outs:
            if constraint.outtime_min <= m:
                to_do_out.append(constraint)
                outs.remove(constraint)
            
        #
        
        for constraint in to_do_in:
            if CLE.give_take_in_order_temporel(constraint.entry_area,constraint.model,m)!=False:
                CLE.apply_task(CLE.give_take_in_order_temporel(constraint.entry_area,constraint.model,m))
                to_do_in.remove(constraint)
        
        for constraint in in_ateliers_1:
            if CLE.give_take_out_order_temporel(constraint.area_atelier,constraint.model,m)!=False:
                CLE.apply_task(CLE.give_take_out_order_temporel(constraint.area_atelier,constraint.model,m))
        
        for constraint in out_ateliers_1:
            if CLE.give_take_in_order_temporel(constraint.area_atelier,constraint.model,m)!=False:
                CLE.apply_task(CLE.give_take_in_order_temporel(constraint.area_atelier,constraint.model,m))
        
        for constraint in outs:
            if CLE.give_take_out_order_temporel(constraint.out_area,constraint.model,m)!=False:
                CLE.apply_task(CLE.give_take_out_order_temporel(constraint.out_area,constraint.model,m))
        
        #CLE.affichage_remplissage()
                


    CLE.affichage_remplissage()
    print(CLE.working_time)
