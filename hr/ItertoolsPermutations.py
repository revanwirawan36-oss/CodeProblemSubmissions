from itertools import permutations
if __name__=='__main__':
    s,num=input().split()
    num=int(num)

    liste=list(permutations(s,num))
    liste.sort()
    
    for combo in liste:
        print("".join(combo))
    #print(liste)
    
