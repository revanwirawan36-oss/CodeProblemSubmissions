def count_substring(string, sub_string):
    hitung=0
    pSub=len(sub_string)
    
    for i in range(len(string)-pSub+1):
        
        if sub_string==string[0+i:pSub+i]:
            hitung+=1
    return hitung

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
