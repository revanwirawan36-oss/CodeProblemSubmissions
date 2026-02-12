

if __name__=='__main__':
    n=int(input())
    string=[]
    for _ in range(n):
        string.append(input())
        
    q=int(input())
    query=[]
    for _ in range(q):
        query.append(input())
    
    for i in range(q):
        ada=0
        for j in range(n):
            if query[i]==string[j]:
                ada+=1
        print(ada)
