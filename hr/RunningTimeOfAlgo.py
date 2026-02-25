def runningTime(arr):
    shifts=0
    
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j] > key:
            arr[j+1]=arr[j]
            arr[j]=key
            j-=1
            shifts+=1
            
            
    return shifts
