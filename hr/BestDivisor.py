def check_sum(el):
    word=str(el)
    tot=0
    for i in range(len(word)):
        tot+=int(word[i])
    return tot
    
def best_divisor(n):
    maxi=-1
    ans=-2
    for el in range(1, n+1):
        if n/el == n//el:
            temp=maxi
            maxi=max(maxi, check_sum(el))
            if maxi != temp:
                ans=el
    return ans
      
if __name__=='__main__':
    n=int(input())
    print(best_divisor(n))
