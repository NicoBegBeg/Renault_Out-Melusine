from tools.Task_class import *
from tools.Area_class import *


class CLE:

    def __init__(self,list_areas,temps_vecteur):
        
        self.areas={"stock":{},"atelier":{},"usine":{},"entree/sortie_route":{}}
        for area in list_areas:
            if area[1] in self.areas.keys():
                self.areas[area[1]][area[0].name]=(area[0])
            else :
                print('Erreur : la fonction "+str(area[1])+" n_est pas dans la liste "stock","atelier","usine","entree/sortie_route"')
        
        self.temps_vecteur=temps_vecteur
        self.working_time=0

    def give_order(self,constraint): #génère "naïvement" la task pour sortir une voiture du stockage

        possible_departure_area=[]
        possible_arrival_area=[]
        
        for area_name in self.areas[constraint.departure_fonction_area]:
            area=self.areas[constraint.departure_fonction_area][area_name]
            if (area.can_remove_car(constraint.model,1) or constraint.departure_fonction_area=="usine"):
                possible_departure_area.append(area)
        
        for area_name in self.areas[constraint.arrival_fonction_area]:
            area=self.areas[constraint.arrival_fonction_area][area_name]
            if (area.can_add_car(constraint.model,1) or constraint.arrival_fonction_area=="entree/sortie_route"):
                possible_arrival_area.append(area)

        
        min=10**5
        id_d_min=-1
        id_a_min=-1
        
        for a_d in possible_departure_area:
            for a_a in possible_arrival_area:
                id_d=a_d.name
                id_a=a_a.name
                if float(self.temps_vecteur[id_d][id_a])<min:
                    id_d_min=id_d
                    id_a_min=id_a
                    min=float(self.temps_vecteur[id_d][id_a])
        
        if id_d_min!=-1:
            return(Task(constraint.departure_fonction_area,id_d_min,constraint.arrival_fonction_area,id_a_min,constraint.model))
        else:
            return(False)


    def apply_task(self,task):
        
        D=self.areas[task.fct_d_area][task.d_area]
        F=self.areas[task.fct_f_area][task.f_area]

        # Plutot mettre des raiseError

        if (D.can_remove_car(task.car_type,1) or task.fct_d_area=="usine") and (F.can_add_car(task.car_type,1) or task.fct_f_area=="entree/sortie_route"):

            self.working_time+=float(self.temps_vecteur[task.d_area][task.f_area])

            if task.fct_d_area!="usine":
                D.remove_car(task.car_type,1)
            if task.fct_f_area!="entree/sortie_route":
                F.add_car(task.car_type,1)

        else:
            print(f"Error ! Impossible to move a car from {D.name} (possible : {D.can_remove_car(task.car_type,1) or task.fct_d_area=='usine'} ; remplissage : {D.filling}) to  {F.name} (possible : {F.can_add_car(task.car_type,1) or task.fct_f_area=='entree/sortie_route'} ; places disponibles : {F.nb_places_restantes()})")

        return(float(self.temps_vecteur[task.d_area][task.f_area]))

    def affichage_remplissage(self):
        for area_fct in self.areas:
            print(str(area_fct) + " :")
            for area_name in self.areas[area_fct]:
                print(self.areas[area_fct][area_name].filling)