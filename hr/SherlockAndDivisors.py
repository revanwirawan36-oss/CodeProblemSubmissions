import math
'''
    jadi ini pake metode pair
    1. cari divisornya, cek bisa dibagi 2 ngga
    2. terus kalo bisa dibagi 2, cek pairnya (N//i), bisa dibagi 2 juga ngga
    3. kalo bisa, increment
    4. stop di sqrt(N) karna if we go pass that bakal ke repeat + ngelama lamain+ ngedouble
'''
def sherlock_and_divisors(N):
    hasil=0
    if N % 2 !=0:
        return hasil
    
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            if i % 2 ==0:
                hasil+=1
            if N // i % 2 == 0 and N // i != i:
                hasil+=1
        
    return hasil
    
if __name__=='__main__':
    T=int(input())
    
    for _ in range(T):
        N=int(input())
        print(sherlock_and_divisors(N))
