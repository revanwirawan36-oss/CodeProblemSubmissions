from itertools import combinations
def two_characters(n,s):
    b=set()
    alph=[0]*26
    maxLen=0
    es=list(s)

    for letter in s:
        alph[ord(letter)-97]+=1
        b.add(letter)
    
    #print(alph)
    permu=list(combinations(b,2))
    #print(permu)
    
    for pair in permu:
        es=list(s)
        hur1=ord(pair[0])-97
        hur2=ord(pair[1])-97
        #print(f"hur1: {hur1}")
        #print(f"hur2: {hur2}")
        disiniSama=False
        for i in range(len(alph)):
            if alph[i] > 0 and (i!=hur1 and i!= hur2):
                while chr(i+97) in es:
                    es.remove(chr(i+97))
        #print(f"es: {es}")
        for i in range(len(es)-1):
            if es[i]==es[i+1]:
                disiniSama=True
                break
        if disiniSama:
                continue
        #print(f"kurlen: {len(es)}")      
        currLen=len(es)
        maxLen=max(currLen,maxLen)
        #print(f"max: {maxLen}")
    return maxLen
 
 
if __name__=='__main__':
    n=int(input())
    s=input()
    
    print(two_characters(n,s))
