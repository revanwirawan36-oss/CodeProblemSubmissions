def keKata(digit):
    if digit == 1:
        return "one"
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    elif digit == 9:
        return "nine"
    elif digit == 10:
        return "ten"
    elif digit == 11:
        return "eleven"
    elif digit == 12:
        return "twelve"
    elif digit == 13:
        return "thirteen"
    elif digit == 14:
        return "fourteen"
    elif digit == 15:
        return "quarter"
    elif digit == 16:
        return "sixteen"
    elif digit == 17:
        return "seventeen"
    elif digit == 18:
        return "eighteen"
    elif digit == 19:
        return "nineteen"
    elif digit == 20:
        return "twenty"
    elif digit == 30:
        return "half"
        
def keYap(h,m):
    tengah=""
    final=""
    minute=" minutes"
    #ganti menit
    if(m==1):
        minute=" minute"
    #tengah
    if 1 <= m <= 30:
        tengah=" past "
    elif 30 < m <= 59:
        tengah=" to "
        h+=1
    else:
        tengah=" o' clock "
    #kecilin m    
    if m>30:
        m=60-m
    #final    
    if 20<m<30:
        final=keKata(20)+" "+keKata(m-20)+minute+tengah+keKata(h)
    elif m == 0:
        final=keKata(h)+tengah
    elif m==15 or m==30:
        final=keKata(m) +tengah+keKata(h)
    else:
        final=keKata(m)+minute+tengah+keKata(h)
        
    return final    
 
def utama():
    h=int(input())
    m=int(input())
    print(keYap(h,m))
    
if __name__ == '__main__':
    utama()
