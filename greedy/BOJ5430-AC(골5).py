import sys
import re
from collections import deque
read = sys.stdin.readline

t = int(read())

for _ in range(t):
    func = list(map(str, read().rstrip()))
    m = int(read().rstrip())
    array = read().rstrip()[1:-1].split(",")
    reverse = 0
    flag = 0
    queue = deque(array)
    
    if m == 0:
        queue = deque()
        
    for i in range(len(func)):
        if func[i] == "R":
            reverse += 1
        else:
            if len(queue) == 0:
                flag = 1
                print("error")
                break
            else:
                if reverse % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if reverse %2== 0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")
    
    


    
 

