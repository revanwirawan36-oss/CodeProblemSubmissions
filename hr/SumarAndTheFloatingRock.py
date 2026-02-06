import math
def sumar_and_points(x1,y1,x2,y3):
    return math.gcd(abs(x2-x1), abs(y2-y1))-1
        
    
if __name__=='__main__':
    T=int(input())
    
    for _ in range(T):
        x1,y1,x2,y2=map(int, input().split())
        print(sumar_and_points(x1,y1,x2,y2))
