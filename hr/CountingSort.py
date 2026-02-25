def countingSort(arr):
    
    liste=[0]*100
   
    for i in range(len(arr)):
        liste[arr[i]]+=1
    
    return liste
