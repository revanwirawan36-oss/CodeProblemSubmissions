def closestNumbers(arr):
    mini=100000000
    #lmao
    arr.sort()
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) < mini:
            mini=abs(arr[i]-arr[i+1])
                
    empAdd=[]
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1]) == mini:
            liste=[arr[i],arr[i+1]]
            empAdd+=liste
    return empAdd
