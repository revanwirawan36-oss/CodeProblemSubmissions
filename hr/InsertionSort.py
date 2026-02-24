def perin(arr):
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    print(" ".join(arr))
    
    for i in range(len(arr)):
        arr[i]=int(arr[i])
        
def insertionSort2(n, arr):
    for i in range(1,n):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
        perin(arr)
