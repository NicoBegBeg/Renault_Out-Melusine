from tools.Task_class import *
from tools.Area_class import *
from tools.temps_vecteur import *

class CLE:

    def __init__(self,areas,temps_vecteur,entry,out,creation_point,expedition_point):
        self.areas=areas
        self.temps_vecteur=temps_vecteur
        self.entry=entry
        self.out=out
        self.creation_point=creation_point
        self.expedition_point=expedition_point
        self.working_time=0

    def give_take_in_order(self,d_area,car_type): #génère naïvement la task pour affecter une voiture au stockage
        for area in self.areas:
            if (self.areas[area].can_add_car(car_type,1) and area not in self.creation_point and area not in self.expedition_point):
                return(Task(d_area,area,car_type,'time'))
        print("Pas d'espace pour stocker le véhicule")

    def give_take_out_order(self,f_area,car_type): #génère naïvement la task pour sortir une voiture du stockage
        for area in self.areas:
            if (self.areas[area].can_remove_car(car_type,1) and area not in self.creation_point and area not in self.expedition_point):
                return(Task(area,f_area,car_type,'time'))
        print("Pas de véhicule correspondant")


    def apply_task(self,task):
        D=self.areas[task.d_area]
        F=self.areas[task.f_area]

        # Plutot mettre des raiseError

        if (D.can_remove_car(task.car_type,1) or D.name in self.creation_point) and (F.can_add_car(task.car_type,1) or F.name in self.expedition_point):

            self.working_time+=dictionnaire_temps_vecteur[task.d_area][task.f_area]

            if D.name not in self.creation_point:
                D.remove_car(task.car_type,1)
            if F.name not in self.expedition_point:
                F.add_car(task.car_type,1)

        else:
            print("error : ",D.name, " ", F.name)


    def affichage_remplissage(self):
        for area_name in self.areas:
            print(area_name,self.areas[area_name].filling)