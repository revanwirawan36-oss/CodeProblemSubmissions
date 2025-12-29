def ngeprin(grades):
    for grade in grades:
        if grade >= 38:
            hitung=0
            while grade % 5 !=0:
                grade+=1
                hitung+=1
                if(hitung==3):
                    grade-=3
                    break
        print(grade)

        
if __name__ == '__main__':
    grades=[]
    n=int(input())
    for i in range(n):
        grades.append(int(input()))
        
    ngeprin(grades)
    
