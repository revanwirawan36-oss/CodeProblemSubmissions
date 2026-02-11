import math

def most_distant(p):
    minx=miny=maxx=maxy=0
    
    for i in range(len(p)):
        x,y=p[i][0],p[i][1]
        if x == 0:
            if y>maxy: maxy=y
            if y<miny: miny=y
        if y == 0:
            if x>maxx: maxx=x
            if x<minx: minx=x
    d1=maxx-minx
    d2=maxy-miny
    d3=math.sqrt((maxx**2)+maxy**2)
    d4=math.sqrt((maxx**2)+miny**2)
    d5=math.sqrt((minx**2)+maxy**2)
    d6=math.sqrt((minx**2)+miny**2)
    return f"{max(d1,d2,d3,d4,d5,d6):.6f}"
    
if __name__=='__main__':
    N=int(input())
    
    p=[]
    
    for _ in range(N):
        evp=list(map(int, input().split()))
        p.append(evp)
        
    print(most_distant(p))
