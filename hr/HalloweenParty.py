def halloween_party(K):
    return (K//2)*(K-(K//2))
    
if __name__=='__main__':
    T=int(input())
    
    for _ in range(T): #d
        K=int(input())
        print(halloween_party(K))
