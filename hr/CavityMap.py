def cavity_map(N, mat):
    n=len(mat)
    print(mat[0])
    if n>2:
        for i in range(1, n-1): #hm
            liste=list(mat[i])
            for j in range(1,len(liste)-1):
                if (liste[j-1]!='X' and int(liste[j])>int(liste[j-1])) and (liste[j+1]!='X' and int(liste[j])>int(liste[j+1])) and (mat[i-1][j]!='X' and int(liste[j])>int(mat[i-1][j])) and ( mat[i+1][j]!='X' and int(liste[j])>int(mat[i+1][j])):
                    liste[j]='X'
            mat[i]="".join(liste)
            print(mat[i])
    if n>1:
        print(mat[-1])
    
if __name__=='__main__':
    N=int(input())
    mat=[]
    for _ in range(N):
        mat.append(input())
    cavity_map(N, mat)
    
