def manasa_and_stones(n,a,b):
    if n==1 :
        return list(str(0))
        
    ans=set()
    for i in range(n):
        inNow=(a*(n-1-i))+(b*(i))
        ans.add(inNow)
    
    return sorted(ans)
        
if __name__ =='__main__':
    T=int(input())
    
    for _ in range(T):
        n=int(input())
        a=int(input())
        b=int(input())
        print(" ".join(map(str, manasa_and_stones(n,a,b))))
    
