#Contient les classes et méthodes utiles à la modélisation du CLE

import data

class CLE:
    def __init__(self,areas,temps_vecteur,entry,out):
        self.areas=areas
        self.temps_vecteur=temps_vecteur
        self.entry=entry
        self.out=out

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
    
    def add_Car(self,car_type,nb_car):
        not_here=True
        for i in self.filling:
            if i==car_type:
                self.filling[i]+=nb_car
                not_here=False
        if not_here
    
