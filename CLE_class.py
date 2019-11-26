import Task_class
import Area_class

class CLE:
    
    def __init__(self,areas,temps_vecteur,entry,out):
        self.areas=areas
        self.temps_vecteur=temps_vecteur
        self.entry=entry
        self.out=out
    
    def apply_task(self,task):
        D=self.areas[task.d_area]
        A=self.areas[task.a_area]
        if max(D.can_remove_car(task.car_type,1),A.can_add_car(task.car_type,1)):
            D.remove_car(task.car_type,1)
            A.add_car(task.car_type,1)