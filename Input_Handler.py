def give_zone():
    file = open("zones.csv","r")
    res = []
    for line in file:
        res.append([x.replace('\n','') for x in line.split(";")])
    file.close()
    return res[1:]

def give_taches():
    file = open("taches.csv","r")
    res = []
    for line in file:
        res.append([x.replace('\n','') for x in line.split(";")])
    file.close()
    return res[1:]

def give_temps_vecteurs():
    file = open("temps_vecteurs.csv","r")
    res = []
    for line in file:
        res.append([x.replace('\n','') for x in line.split(";")])
    file.close()
    res2 = {x:{} for x in res[0][1:]}
    for i in range(1,len(res)):
        for j in range(1,len(res)):
            res2[ res[0][i] ][ res[0][j] ] = res[i][j]
    return res2

def give_organisation():
    file = open("organisation.csv","r")
    res = []
    for line in file:
        res.append([x.replace('\n','') for x in line.split(";")])
    return [x[1] for x in res]