
def lisas_workbook(n,k,arr):
    buku=[]
    special=0
    for problem in arr:
        hlm=[]
        for i in range(problem):
            hlm.append(i+1)
            if (i+1)%k==0 or i+1==problem:
                buku.append(hlm)
                hlm=[]
    for i in range(len(buku)):
        if i+1 in buku[i]:
            special+=1
    return special
    
if __name__=='__main__':
    n,k=map(int, input().split())
    arr=list(map(int, input().split()))
    
    print(lisas_workbook(n,k,arr))
