import numpy as np

class Jockey_pool:
    def __init__(self, max, navette_capacity, navette_fleet,CLE):
        self.max=max
        self.free=max
        self.navette_capacity=navette_capacity
        self.navette_fleet=navette_fleet
        self.free_navette=navette_fleet
        self.busy=[]
        self.busy_navette=[]
        # self.queue_in=np.zeros((len(CLE.creation_point),len(CLE.areas)))
        # self.queue_out=np.zeros((len(CLE.expedition_point),len(CLE.areas)))
        self.queue_in={b:{a:0 for a in CLE.areas} for b in CLE.creation_point}
        self.queue_out={b:{a:0 for a in CLE.areas} for b in CLE.expedition_point}
        self.CLE=CLE
    
    def dispo(self):
        return(self.free>0 and self.navette_fleet>0)
    
    def working(self,applied_order):
        time,d_area,f_area=applied_order
        
        if d_area in self.CLE.creation_point:
            self.queue_in[d_area][f_area]+=1
            
                
        if f_area in self.CLE.expedition_point and d_area not in CLE.creation_point :
            self.queue_out[f_area][d_area]+=1

                
    
    def refresh(self):
        
        if(self.free>0 and self.navette_fleet>0):
            for d_area in self.queue_in.keys():
                for f_area in self.queue_in[d_area].keys():
                    if self.queue_in[d_area][f_area]>=self.navette_capacity and self.free_navette>0:
                        working_jockey=min(self.free,self.navette_capacity)
                        time=self.CLE.temps_vecteur[d_area][f_area]
                        self.busy.append([time,working_jockey])
                        self.busy_navette.append(time)
                        self.free-=working_jockey
                        self.free_navette-=1
                        self.queue_in[d_area][f_area]-=working_jockey
                        print('navette entrée envoyée')
            
            for f_area in self.queue_out.keys():
                for d_area in self.queue_out[f_area].keys():
                    if self.queue_out[f_area][d_area]>=self.navette_capacity and self.free_navette>0:
                        working_jockey=min(self.free,self.navette_capacity)
                        self.busy.append([time,working_jockey])
                        time=self.CLE.temps_vecteur[d_area][f_area]
                        self.busy_navette.append(time)
                        self.free-=working_jockey
                        self.free_navette-=1
                        self.queue_in[f_area][d_area]-=working_jockey
                        print('navette sortie envoyée')
        
        
        freed_n=0

        
        for j in range(len(self.busy_navette)):
            if self.busy_navette[j-freed_n]<=1:
                self.busy_navette.remove(self.busy_navette[j-freed_n])
                freed_n+=1
                print('raz d une navette')
            else:
                self.busy_navette[j-freed_n]-=1
        self.free_navette+=freed_n
        
        freed=0
        
        for i in range(len(self.busy)):
            if self.busy[i-freed][0]<=1:
                self.free+=self.busy[i-freed][1]
                freed+=1
                self.busy.remove(self.busy[i-freed])
            else:
                self.busy[i-freed][0]-=1