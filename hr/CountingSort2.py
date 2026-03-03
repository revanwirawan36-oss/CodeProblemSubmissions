def countingSort(arr):
    liste=[0]*100
   
    for i in range(len(arr)):
        liste[arr[i]]+=1
        
    kosong=[]
    
    for i in range(len(liste)):
        for j in range(liste[i]):
            kosong.append(i)
    
        
    return kosong
