def strange_grid_again(r,c):
    rPuluhan=r+1 if r%2!=0 else r
    
    puluhan=((rPuluhan//2)-1)*10
    
    digitDigit=0 if r%2!=0 else 1
    
    digitSatuan=digitDigit+(2*(c-1))
    
    return puluhan+digitSatuan
    
if __name__=='__main__':
    r,c=map(int, input().split())
    print(strange_grid_again(r,c))
