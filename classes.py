#Contient les classes et méthodes utiles à la modélisation du CLE

import data

class CLE:
    def __init__(self,areas,temps_vecteur,entry,out):
        self.areas=areas
        self.temps_vecteur=temps_vecteur
        self.entry=entry
        self.out=out

class Area:
    def __init__(self,nb_places,filling):
        self.filling=filling
    
    def nb_places_restantes(self):
        count=0
        for i in self.filling:
            count+=self.filling[i]
        return(self.nb_places-count)
