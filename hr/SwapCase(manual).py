def swap_case(s):
    tempS=list(s)
    for i in range(len(tempS)):
        upCase= 64 < ord(tempS[i]) <= 90
        lowCase= 97 <= ord(tempS[i]) <124
        
        if lowCase:
            idx= ord(tempS[i])-97
            tempS[i]=chr(65+idx)
        elif upCase:
            idx=ord(tempS[i])-65
            tempS[i]=chr(97+idx)
    
    s="".join(tempS)    
    return s
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
