import sys

read = sys.stdin.readline

n,m = map(int,read().split())

answer = []
def back_tracking():
    for i in range(1,n+1):
        if len(answer) == m:
            print(' '.join(map(str,answer)))
            return
        else:
            if i not in answer:
                answer.append(i)
                back_tracking()
                answer.pop()
    
back_tracking()
