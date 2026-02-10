def is_pali(s):
    stgh=len(s)//2
    
    return s[:stgh]==s[::-1][:stgh]


def palindrome_index(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            pali=s[:i]+s[i+1:]
            if is_pali(pali):
                return i
            pali=s[:n-1-i]+s[n-i:]
            if is_pali(pali):
                return n-1-i
            return -1
    return -1
    
if __name__=='__main__':
    q= int(input())
    
    for _ in range(q):
        s=input()
        print(palindrome_index(s))
