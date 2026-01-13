def min_palindromes(s):
    isEven= len(s)%2==0
    midPoint=len(s)//2
    kiri=s[0:midPoint]
    kanan = s[midPoint:] if isEven else s[midPoint+1:]
    #print(kiri)
    #print(kanan)
    minDiff=0
    for i in range(len(kanan)):
        minDiff+=abs(ord(kanan[i])-ord(kiri[len(kiri)-i-1]))
    return minDiff
          
if __name__=='__main__':
    t=int(input())
    
    for _ in range(t):
        s=input()
        print(min_palindromes(s))
        
