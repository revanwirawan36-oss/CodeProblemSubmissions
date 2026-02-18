def perin(arr):
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    print(" ".join(arr))
    
    for i in range(len(arr)):
        arr[i]=int(arr[i])
    
def insertionSort1(n, arr):
    angkanya=arr[n-1]
    for i in range(n-1,-1,-1):
        if i==0:
            arr[i]=angkanya
            perin(arr)
            break
        elif arr[i-1]>angkanya:
            arr[i]=arr[i-1]
        else:
            arr[i]=angkanya
            perin(arr)
            break
        perin(arr)
