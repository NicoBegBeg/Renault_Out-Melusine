from Task_class import *
from Area_class import *

class CLE:

    def __init__(self,areas,temps_vecteur,entry,out,creation_point,expedition_point):
        self.areas=areas
        self.temps_vecteur=temps_vecteur
        self.entry=entry
        self.out=out
        self.creation_point=creation_point
        self.expedition_point=expedition_point
    
    def give_take_in_order(self,d_area,car_type): #génère naïvement la task pour affecter une voiture au stockage
        for area in self.areas:
            if self.areas[area].can_add_car(car_type,1):
                return(Task(d_area,area,car_type,'time'))
        

    def apply_task(self,task):
        D=self.areas[task.d_area]
        F=self.areas[task.f_area]

        # Plutot mettre des raiseError

        if max(D.can_remove_car(task.car_type,1),F.can_add_car(task.car_type,1)):
            
            if D.name not in self.creation_point:
                D.remove_car(task.car_type,1)
                print('done1')
            if D.name not in self.expedition_point:
                F.add_car(task.car_type,1)
                print('done2')

    def affichage_remplissage(self):
        for area_name in self.areas:
            print(area_name,self.areas[area_name].filling)