from collections import defaultdict
def nested_list(liste,score_board):
    liste.sort()
    for i in range(len(liste)):
        if liste[i]!=liste[i+1]:
            sec=liste[i+1]
            break
    liste2=score_board[sec]
    liste2.sort()
    for name in liste2:
        print(name)

def utama():
    liste=[]
    score_board = defaultdict(list)
    for _ in range(int(input())):
        name=input()
        score=float(input())
        liste.append(score)
        score_board[score].append(name)
        
    nested_list(liste,score_board)
         
if __name__ == '__main__':
    utama()

            
        
