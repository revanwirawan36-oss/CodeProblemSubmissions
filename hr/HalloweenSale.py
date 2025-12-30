def howManyGames(p, d, m, s):
    hitung = 0
    while s > 0:
        s-=p
        if p > m:
            p-=d
        if p <= m:
            p=m
        hitung+=1
        if s < 0:
            hitung-=1
    
    return hitung

if __name__ == '__main__':
    p,d,m,s=map(int, input().split())
    
    print(howManyGames(p,d,m,s))
