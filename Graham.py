import FunctionsHelpers as fh

def polar_cmp(p0,p1,p2):
    d =fh.direction(p0,p1,p2)
    if d<0:
        return -1
    elif d>0:
        return 1
    else:
        if(fh.distance(p0,p1)<fh.distance(p0,p2)):
            return -1
        else:
            return 1


def run(data,upperX,upperY):
    ch=[]
    firstP=min(data)
    ind=data.index(firstP)
    data[0],data[ind]=data[ind],data[0]
    #sort_point=sorted(data[1:],key=lambda p1,p2:(polar_cmp(firstP,p1,p2)))
    #sort_point=sorted(data[1:],key=lambda p1:direction2(firstP,p1))
    pointsl=[x for x in data[1:] if x[0]<firstP[0]]
    pointsE=[x for x in data[1:] if x[0]==firstP[0]]
    pointsR=[x for x in data[1:] if x[0]>firstP[0]]
    pointsl=sorted(pointsl,key=lambda p: fh.slope(p, firstP))
    pointsR=sorted(pointsR,key=lambda p: fh.slope(p, firstP))
    sort_point=pointsR+pointsE+pointsl
    
    to_remove=[]
    for i in range(len(sort_point)-1):
        d=fh.direction(firstP,sort_point[i],sort_point[i+1])
        if d==0:
            to_remove.append(i)
        
    last_array=[sort_point[x] for x in range(len(sort_point)) if x not in to_remove]


    ch.append(data[0])
    ch.append(last_array[0])
    ch.append(last_array[1])

    p1=last_array[0]
    p2=last_array[1]

    for i in range(2,len(last_array)):
        while fh.direction(ch[-2],last_array[i],ch[-1])>=0:
                ch.pop()
        ch.append(last_array[i])

    ch.append(data[0])

    return ch
