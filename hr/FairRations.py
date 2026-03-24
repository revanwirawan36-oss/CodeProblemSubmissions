def fairRations(B):
    kasih=0
    for i in range(len(B)-1):
        if B[i]%2!=0:
            B[i+1]+=1
            B[i]+=1
            kasih+=2
        #print(B) debug
    for el in B:
        if el%2!=0:
            return "NO" 
    return kasih

if __name__ == '__main__':
    n=int(input())
    B=list(map(int, input().split()))
    
    print(fairRations(B))
