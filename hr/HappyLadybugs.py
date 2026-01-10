def cekAdja(s):
    adja=False
    currEl=-1
    for i in range(len(s)):
        if s[i]!=currEl and s[i]!='_':
            if i<len(s)-1:
                if s[i]==s[i+1]:
                    adja=True
                    currEl=s[i]
                else:
                    adja=False
                    break
                    
            else:
                if s[i]==s[i-1]:
                    adja=True
                    currEl=s[i]
                else:
                    adja=False
                    break
                
        if s[i]==currEl:
            continue
    return adja
    
def happy_ladybugs(n,s):
    adja=cekAdja(s)
            
    alphabet=[0]*27
    for el in s:
        if el != '_':
            alphabet[ord(el)-65]+=1
        else:
            alphabet[26]+=1
    #print(alphabet)
    if 1 in alphabet[0:26] or (alphabet[26]==0 and not adja):
        return "NO"
    return "YES"

if __name__=='__main__':
    g=int(input())
    
    for _ in range(g):
        n=int(input())
        s=input()
        print(happy_ladybugs(n,s))
