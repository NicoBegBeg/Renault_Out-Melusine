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
        return(nb_car<=self.nb_places_restantes())

    def can_remove_car(self,car_type,nb_car):
        for i in self.filling:
            if i==car_type:
                return (self.filling[i]>=nb_car)
        return False

    def add_car(self,car_type,nb_car):

        assert self.nb_places_restantes()>=nb_car,"Ajout interdit : Pas assez de places"
        #Plutot des RaiseError

        not_here=True
        for i in self.filling:
            if i==car_type:
                self.filling[i]+=nb_car
                not_here=False
        if not_here:
            self.filling[car_type]=nb_car

    def remove_car(self,car_type,nb_car):
        done=False
        for i in self.filling:
            if i==car_type:
                assert self.filling[i]>=nb_car,"Retrait interdit : Pas assez de véhicules de ce modèle"
                #Plutot des RaiseError
                done=True
                self.filling[i]-=nb_car

        assert done,"Retrait interdit : Aucun véhicules de ce modèle"
        #Plutot des RaiseError

    def __repr__(self):
        total_filling = sum([x for x in self.filling.values()])
        return f"Area('{self.name}' : {total_filling}/{self.nb_slot})"
