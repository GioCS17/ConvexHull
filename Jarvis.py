import FunctionsHelpers as fh

def run(data):
    l=min(data)
    ind=data.index(l)
    indabs=ind
    jarvis=[]
    jarvis.append(l)
    while True:
        aux=(ind+1)%len(data)
        for i in range(len(data)):
            if i==ind:
                continue
            d =  fh.direction(data[ind],data[i],data[aux])
            if d>0 or(d==0 and fh.distance(data[i],data[ind])>fh.distance(data[ind],data[aux])):
                aux=i
        
        ind=aux
        if aux==indabs:
            break
        jarvis.append(data[aux])
    
    jarvis.append(l)
    return jarvis