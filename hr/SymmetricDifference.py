if __name__=='__main__':
    N=int(input())
    a=set(map(int, input().split()))
    M=int(input())
    b=set(map(int, input().split()))
    
    aInB=a.difference(b)
    bInA=b.difference(a)
    innit=aInB.union(bInA)
    for combo in sorted(innit):
        print(combo)
    
