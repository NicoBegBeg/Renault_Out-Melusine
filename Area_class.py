filling = {"nissan":100,"type2":200}

class Area:
    
    def __init__(self,name,nb_slot,filling): #filling est un dictionnaire du type : {nom de modèle, nombre de véhicule entreposés}
        self.name=name
        self.filling=filling
        self.nb_slot=nb_slot
        
    
    def nb_places_restantes(self):
        count=0
        for i in self.filling:
            count+=self.filling[i]
        return(self.nb_slot-count)
    
    def can_add_car(self,car_type,nb_car):
        return(nb_car<self.nb_places_restantes)
    
    def can_remove_car(self,car_type,nb_car):
        can=False
        for i in self.filling:
            if i==car_type:
                can=(self.filling[i]>=nb_car)
        return can
    
    def add_car(self,car_type,nb_car):
        not_here=True
        for i in self.filling:
            if i==car_type:
                self.filling[i]+=nb_car
                not_here=False
        if not_here:
            self.filling[car_type]=nb_car
        assert nb_places_restantes>=0,"Ajout interdit"
    
    def remove_car(self,car_type,nb_car):
        for i in self.filling:
            if i==car_type:
                self.filling[i]-=nb_car
                assert self.filling[i]>=0,"Retrait interdit"



    
