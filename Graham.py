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
    sort_point=sorted(data[1:],key=lambda p:fh.slope(p,data[0]))
    
    to_remove=[]
    for i in range(len(sort_point)-1):
        j=i
        k=i+1
        d=fh.direction(firstP,sort_point[j],sort_point[k])
        while d==0:
            if fh.distance(firstP,sort_point[j])<fh.distance(firstP,sort_point[k]):
                to_remove.append(j)
                j+=1
            else:
                to_remove.append(k)
            k+=1
            if k>=len(sort_point):
                break
            d=fh.direction(firstP,sort_point[j],sort_point[k])
        i=k
        
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
