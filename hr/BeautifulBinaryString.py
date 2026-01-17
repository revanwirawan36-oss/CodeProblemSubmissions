def beautiful_binary_string(n,b):
    ada=0
    i=0
    while i < n-2:
        if b[i:i+3]=="010":
            ada+=1a
            i+=3
        else:
            i+=1
    return ada 
    
if __name__=='__main__':
    n=int(input())
    b=input()
    
    print(beautiful_binary_string(n,b))
#test
