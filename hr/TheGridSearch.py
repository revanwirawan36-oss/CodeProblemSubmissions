def the_grid_search(R,C,grid,r,c,search):
    for i in range(R):
        for j in range(C-c+1):
            if grid[i][j:j+c]==search[0]:
                ada=True
                for k in range(1,r):
                    if grid[i+k][j:j+c]!=search[k]:
                        ada=False
                        break
                if ada:
                    return "YES"
    return "NO"

if __name__=='__main__':
    t=int(input())
    
    for _ in range(t):
        R,C=map(int, input().split())
        grid=[]
        for o in range(R):
            el=input()
            grid.append(el)
        r,c=map(int, input().split())
        search=[]
        for o in range(r):
            el=input()
            search.append(el)
        print(the_grid_search(R,C,grid,r,c,search))
        
