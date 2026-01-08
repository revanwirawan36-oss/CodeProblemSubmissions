import math
def flatland_ss(cities,n, stations):
    maxDis=-1
    stations.sort()
    #print(stations)
    for i in range(len(stations)-1):
        dis=abs(stations[i]-stations[i+1])
        maxDis=max(dis,maxDis)
    
    maxTemp=maxDis
    maxDis=max(abs(stations[0]-0), maxDis//2)
    
    if maxTemp==maxDis:
        maxDis=max(abs(stations[n-1]-(cities-1)), maxDis//2)
    else:
        maxDis=max(abs(stations[n-1]-(cities-1)), maxDis)
    
    if maxTemp==maxDis:
        return maxDis//2
    return maxDis
    
    '''
    maxGakeganti=maxTemp//2
    print(f"keganti: {maxKeganti}, gak: {maxGakeganti}")
    '''
    
if __name__ == '__main__':
    cities,n=map(int, input().split())
    stations=list(map(int, input().split()))
    print(flatland_ss(cities,n,stations))
