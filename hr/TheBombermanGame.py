def the_bomberman_game(r,c,n,grid):
    if n==1:
        return grid
    elif n%2==0:
        return ['O'*c]*r
    indeks=set()
    
    for i in range(r):
        for j in range(len(grid[i])):
            if grid[i][j]=='O':
                indeks.add((i,j))
   # print(indeks)
                
    indeks2=set()
    
    for el in indeks:
        atasI= el[0]-1 if el[0]>0 else 0
        bawahI= el[0]+1 if el[0]<(r-1) else r-1
        kananJ= el[1]+1 if el[1]<(c-1) else c-1
        kiriJ=  el[1]-1 if el[1]>0 else 0
        indeks2.add((atasI,el[1]))
        indeks2.add((bawahI,el[1]))
        indeks2.add((el[0],kananJ))
        indeks2.add((el[0],kiriJ))
        
    indeks=indeks.union(indeks2)
    bomb=['O']*c
    
    newGrid=['O'*c]*r
    
    #print(newGrid)
    n= 3 if n%4==3 else 5
    
    for i in range(r):
        bomb=list(newGrid[i])
        for j in range(c):
            if (i,j) in indeks:
            #print(f"indeksnya: {i} {j}")
                bomb[j]='.'
        newGrid[i]="".join(bomb)
    
    if n == 3:
        return newGrid          
    
    indeks2=set()
    indeks=set()
        
    for i in range(r):
        for j in range(len(newGrid[i])):
            if newGrid[i][j]=='O':
                indeks.add((i,j))
        
    for el in indeks:
        atasI= el[0]-1 if el[0]>0 else 0
        bawahI= el[0]+1 if el[0]<(r-1) else r-1
        kananJ= el[1]+1 if el[1]<(c-1) else c-1
        kiriJ=  el[1]-1 if el[1]>0 else 0
        indeks2.add((atasI,el[1]))
        indeks2.add((bawahI,el[1]))
        indeks2.add((el[0],kananJ))
        indeks2.add((el[0],kiriJ))
        
    indeks=indeks.union(indeks2)
        
    newGrid=['O'*c]*r
        
    for i in range(r):
        bomb=list(newGrid[i])
        for j in range(c):
            if (i,j) in indeks:
            #print(f"indeksnya: {i} {j}")
                bomb[j]='.'
        newGrid[i]="".join(bomb)
    return newGrid

if __name__ =='__main__':
    r,c,n=map(int, input().split())
    grid=[]
    
    for _ in range(r):
        s=input()
        grid.append(s)
    print("\n".join(the_bomberman_game(r,c,n,grid)))
