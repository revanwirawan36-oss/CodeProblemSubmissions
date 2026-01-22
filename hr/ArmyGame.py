def army_game(n,m):
    if n %2==0 and m%2==0 and n*m%4==0:
        return (n*m)//4
    sisaN= n%2
    sisaM= m%2
    
    fullEmpat= (n-sisaN)*(m-sisaM)
    productFullEmpat=fullEmpat//4
    akhir=productFullEmpat+((n*sisaM)//2)+((m*sisaN)//2)#lm12
   
    if (n==1 and m%2!=0) or (m==1 and n%2!=0) or (n%2!=0 and m%2!=0):
        akhir+=1
    return akhir
         

if __name__=='__main__':
    n,m=map(int, input().split())
    print(army_game(n,m))
