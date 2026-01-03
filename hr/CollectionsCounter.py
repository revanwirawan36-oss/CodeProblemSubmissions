from collections import Counter

if __name__=='__main__':
    n= int(input())
    
    liste=list(map(int, input().split()))
    tot=0
    m= int(input())
    
    counts=Counter(liste)
#   Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    for _ in range(m):
        a,b=map(int, input().split())
        if counts[a]>0:
            tot+=b
            counts[a]-=1
    print(tot)
