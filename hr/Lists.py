def hapus(e,arr):
    for i in range(len(arr)):
        if arr[i]==e:
            del arr[i]
            break
            
def lists(tipe,lNum,arr):
        if(tipe=='insert'):
            arr.insert(lNum[0],lNum[1])
           # print(f"{lNum[0]}, {lNum[1]}")
        elif(tipe=='print'):
            print(arr)
        elif(tipe=='remove'):
            hapus(lNum[0],arr)
        elif(tipe=='append'):
            arr.append(lNum[0])
        elif(tipe=='sort'):
            arr.sort()
        elif(tipe=='pop'):
            arr.pop()
        elif(tipe=='reverse'):
            arr.reverse()

def utama():
    N = int(input())
    arr=[]
    for i in range(N):
        tipe, *num=input().split()
        lNum=list(map(int, num))
        lists(tipe,lNum,arr)
        
if __name__ == '__main__':
    utama()

            
            
            
        
