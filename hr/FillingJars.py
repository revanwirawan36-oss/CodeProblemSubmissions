import math

def filling_jars(a,b,k):
    return abs((b-a)+1)*k

def akhir(hasil,n):
    return hasil//n
    
if __name__=='__main__':
    n,size=map(int, input().split())
    
    hasil=0
    for _ in range(size):
        a,b,k=map(int, input().split())
        hasil+=filling_jars(a,b,k)
    
    print(akhir(hasil,n))
