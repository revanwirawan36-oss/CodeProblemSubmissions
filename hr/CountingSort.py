def countingSort(arr):
    
    liste=[0]*100 #create list kosong
   
    for i in range(len(arr)):
        liste[arr[i]]+=1
    
    return liste
