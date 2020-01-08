

class Jockey_pool:
    def __init__(self, max):
        self.max=max
        self.free=max
        self.busy=[]
    
    def dispo(self):
        return(self.free>0)
    
    def working(self,time):
        self.busy.append(time)
        self.free-=1
    
    def refresh(self):
        freed=0
        for i in range(len(self.busy)):
            if self.busy[i-freed]<=1:
                self.busy.remove(self.busy[i-freed])
                freed+=1
            else:
                self.busy[i-freed]-=1
        self.free+=freed