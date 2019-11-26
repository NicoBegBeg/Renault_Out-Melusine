from Task_class import *
from Area_class import *

class CLE:

    def __init__(self,areas,temps_vecteur,entry,out):
        self.areas=areas
        self.temps_vecteur=temps_vecteur
        self.entry=entry
        self.out=out

    def apply_task(self,task):
        D=self.areas[task.d_area]
        F=self.areas[task.f_area]

        # Plutot mettre des raiseError

        if max(D.can_remove_car(task.car_type,1),F.can_add_car(task.car_type,1)):
            D.remove_car(task.car_type,1)
            F.add_car(task.car_type,1)

    def affichage_remplissage(self):
        for area_name in self.areas:
            print(area_name,self.areas[area_name].filling)