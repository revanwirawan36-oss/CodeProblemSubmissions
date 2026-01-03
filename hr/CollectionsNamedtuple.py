from collections import namedtuple

if __name__=='__main__':
    N, header_line=int(input()), input().split()
    StudentRecords= namedtuple("StudentRecords", header_line)
    tot=0
    for _ in range(N):
        data_values=input().split()
        student= StudentRecords(*data_values)
        tot+=int(student.MARKS)
    print(f"{tot/N:.2f}")
