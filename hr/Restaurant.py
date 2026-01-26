def restaurant(l,b):
    res=-1
    i=1
    while(i*i <= l*b):
        #print(f"iterasi: {i*i}")
        if ((l*b) / (i*i) == (l*b) // (i*i)) and (l % i*i==0 and b % i*i == 0):
            res= (l*b) // (i*i)
            #print(f"res : {res}")
        i+=1
    return res

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        l,b=map(int, input().split())
        print(restaurant(l,b))
