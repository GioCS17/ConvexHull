import math

def direction(p0,p1,p2):
    return (p1[0]-p0[0])*(p2[1]-p0[1])-(p1[1]-p0[1])*(p2[0]-p0[0])
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def slope(p1, p2):
    return math.atan2(p1[1]-p2[1],p1[0]-p2[0]) if p1[0]!=p2[0] else float['inf']

def min_point(data,upperX,upperY):
    pmini=(upperX,upperY+1)
    ind = -1
    for i in range(len(data)):
        if data[i][1]<pmini[1]:
            pmini=data[i]
            ind=i
        elif data[i][1]==pmini[1]:
            if(data[i][0]<pmini[0]):
                pmini=data[i]

    return pmini,ind

