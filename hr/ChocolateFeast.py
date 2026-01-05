def chocolate_feast(n,c,m):
    heCanBuy=n//c
    tot=heCanBuy
    while heCanBuy >= m:
       # print(f"he can buy: {heCanBuy}")
        sisa=heCanBuy%m
        heCanBuy=heCanBuy//m
        tot+=heCanBuy
        heCanBuy+=sisa
    return tot
    
    
if __name__=='__main__':
    t= int(input())
    
    for _ in range(t):
        n,c,m=map(int, input().split())
        print(chocolate_feast(n,c,m))
        
