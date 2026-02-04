def reverse_game(N,K):
    N-=1
    
    if K<N//2:
        return (K*2)+1
    return (N-K)*2
    
if __name__ =='__main__':
    T=int(input())
    
    for _ in range(T):
        N,K=map(int, input().split())
        print(reverse_game(N,K))
