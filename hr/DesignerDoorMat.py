def designer_door_mat(N,M):
    numOfAtas=(M//2)-1
    
    for i in range(N//2+1):
        res=[]
        fin=""
        if i == (N//2):
            tempNOA=(M-7)//2
            for j in range(tempNOA):
                res.append("-")
            res.append("WELCOME")
            for j in range(tempNOA):
                res.append("-")
            fin="".join(res)
            print(fin)
            continue
        for j in range(numOfAtas):
            res.append("-")
        for j in range(i+i+1):
            res.append(".|.")
        for j in range(numOfAtas):
            res.append("-")
        numOfAtas-=3
        fin="".join(res)
        print(fin)
    numOfAtas+=3
    for i in range((N//2)-1, -1, -1):
        res=[]
        fin=""
        for j in range(numOfAtas):
            res.append("-")
        for j in range(i+i+1):
            res.append(".|.")
        for j in range(numOfAtas):
            res.append("-")
        numOfAtas+=3
        fin="".join(res)
        print(fin)



if __name__=='__main__':
    N,M=map(int, input().split())
    
    designer_door_mat(N,M)
        
            
            
        
