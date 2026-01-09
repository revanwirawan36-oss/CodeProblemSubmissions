def climbing(n, ranked, m, player):
    liste=[]
    unq=list(dict.fromkeys(ranked))
    currRankIndex=len(unq)-1
    for score in player:
        while currRankIndex>=0 and score >= unq[currRankIndex]:
            currRankIndex-=1
        liste.append(str(currRankIndex+2))
    return liste
        
if __name__=='__main__':
    n=int(input())
    ranked=list(map(int, input().split()))
    m=int(input())
    player=list(map(int, input().split()))
    
    print("\n".join(climbing(n,ranked,m,player)))
