def cutting_paper_squares(n,m):
    return (n*m)-1
        
if __name__=='__main__':
    n,m=map(int, input().split())
    print(cutting_paper_squares(n,m))
