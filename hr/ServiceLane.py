if __name__=='__main__':
    n,t=map(int, input().split())
    width=list(map(int, input().split()))
    for _ in range(t):
        start,end=map(int, input().split())
        print(min(width[start:end+1]))
