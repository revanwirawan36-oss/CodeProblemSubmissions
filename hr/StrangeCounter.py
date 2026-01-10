def strange_counter(t):
    
    nearestStop=3
    prev=-1
    neaerestStopTime=-1
    while True:
        nearestStop*=2
        if neaerestStopTime>=t:
            nearestStop=prev
            break
        prev=nearestStop
        neaerestStopTime=prev-2
    #print(f"tnya: {neaerestStopTime//2-1}")
    #print(f"valnya: {nearestStop//2}")
    
    if t == neaerestStopTime:
        return nearestStop
        
    kelebihanT=t-((neaerestStopTime//2)-1)
    return (nearestStop//2)-kelebihanT
    
if __name__=='__main__':
    t=int(input())
    print(strange_counter(t))
