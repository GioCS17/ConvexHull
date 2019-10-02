import math

def direction(p0,p1,p2):
    return (p1[0]-p0[0])*(p2[1]-p0[1])-(p1[1]-p0[1])*(p2[0]-p0[0])

def findSide(p0,p1,p2):
    val=(p1[0]-p0[0])*(p2[1]-p0[1])-(p1[1]-p0[1])*(p2[0]-p0[0])
    if val>0:
        return 1
    elif val<0:
        return -1
    return 0

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def slope(p1, p2):
    if p1[0]!=p2[0]:
        return math.atan2(p1[1]-p2[1],p1[0]-p2[0])
    else:
        return math.inf
def distanceToLine(u,l,p):
    return abs((u[1]-l[1])*p[0]-(u[0]-l[0])*p[1]+u[1]*l[0]-l[1]*u[0])/math.sqrt((u[1]-l[1])**2+(u[0]-l[0])**2)

def triangleArea(p1,p2,p3):
    return abs((p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))/2.0)

def slopeValue(p1,p2):
    if p1[0]!=p2[0]:
        return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])
    else:
        return math.inf

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

