def quickSort(arr):
    p=arr[0]
    l=[]
    r=[]
    for el in arr:
        if el<p:
            l.append(el)
        elif el>p:
            r.append(el)
    l.append(p)
    return l+r
