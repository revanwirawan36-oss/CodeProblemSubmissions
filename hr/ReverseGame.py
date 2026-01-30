def reverse_game(N,K):
    cpyN=N-1
    hasil=N-1
    
    if K==N-1:
        return 0
        
    for i in range(1, N):
        if i%2==0:
            hasil+=cpyN
          #  print(f"hasilnya segini: {hasil}, copyN= {cpyN}")
        else:
            hasil-=cpyN
           # print(f"hasilnya segini: {hasil}, copyN= {cpyN}")
        
        if hasil==K:
            break
        cpyN-=1
    return i
    
if __name__ =='__main__':
    T=int(input())
    
    for _ in range(T):
        N,K=map(int, input().split())
        print(reverse_game(N,K))
