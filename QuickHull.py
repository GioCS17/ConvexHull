import FunctionsHelpers as fh

def lineDist(p1,p2,p):
    return abs((p[1]-p1[1])*(p2[0]-p1[0])-(p2[1]-p1[1])*(p[0]-p1[0]))

def recursive(data,ch,u,l,side):
    maxd=-1
    ind=-1
    for i in range(len(data)):
        d=lineDist(l,u,data[i])
        if fh.findSide(l,data[i],u)==side and d>maxd:
            maxd=d
            ind=i
    if ind==-1:
        ch.append(u)
        ch.append(l)
        return 
    recursive(data,ch,l,data[ind],-fh.findSide(data[ind],u,l))
    recursive(data,ch,u,data[ind],-fh.findSide(data[ind],l,u))


    

def run(data):
    ch=[]
    mini=min(data)
    maxi=max(data)
    recursive(data,ch,maxi,mini,-1)
    recursive(data,ch,maxi,mini,1)
    ans=[]
    mini=min(ch)
    ind=ch.index(mini)
    ch[0],ch[ind]=ch[ind],ch[0]
    ans.append(ch[0])
    sort_point=sorted(ch[1:],key=lambda p:fh.slope(p,ch[0]))
    ans=ans+sort_point
    ans.append(ch[0])
    return ans
