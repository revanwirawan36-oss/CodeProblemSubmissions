def print_formatted(n):
    spc=len(format(n, 'b'))
    spc+=1
    for i in range(n):
        liste=[]
        fin=""
        
        norm=str(i+1)
        okta=format(i+1, 'o')
        hexa=format(i+1, 'X')
        bina=format(i+1, 'b')
        
        liste.extend(" "*(spc-len(norm)-1))
        liste.append(norm)
        liste.extend(" "*(spc-len(okta)))
        liste.append(okta)
        liste.extend(" "*(spc-len(hexa)))
        liste.append(hexa)
        liste.extend(" "*(spc-len(bina)))
        liste.append(bina)
        fin="".join(liste)
        print(fin)
        
        
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
