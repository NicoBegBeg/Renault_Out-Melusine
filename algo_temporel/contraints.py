class entry:
    def __init__(self,entry_time,entry_area,model,out_date):
        self.entry_time = entry_time
        self.entry_area = entry_area
        self.model = model
        self.out_date = out_date

class out:
    def __init__(self,outtime_min,outtime_max,out_area,model):
        self.outtime_min = outtime_min
        self.outtime_max = outtime_max
        self.out_area = out_area
        self.model = model

class in_atelier:
    def __init__(self,entry_time,area_in,area_atelier,model):
        self.entry_time = entry_time
        self.area_in = area_in
        self.area_atelier = area_atelier
        self.model = model

class out_atelier:
    def __init__(self,out_time,area_out,area_atelier,model):
        self.out_time = out_time
        self.area_atelier = area_atelier
        self.area_out = area_out
        self.model = model

