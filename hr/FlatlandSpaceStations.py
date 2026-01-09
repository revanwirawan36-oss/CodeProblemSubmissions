import math
def flatland_ss(cities,n, stations):
    stations.sort()
    maxDis=max(abs(stations[0]-0), abs(stations[n-1]-(cities-1)))
    for i in range(n-1):
        maxDis=max(abs(stations[i]-stations[i+1])//2, maxDis)
    return maxDis
    
if __name__ == '__main__':
    cities,n=map(int, input().split())
    stations=list(map(int, input().split()))
    print(flatland_ss(cities,n,stations))
