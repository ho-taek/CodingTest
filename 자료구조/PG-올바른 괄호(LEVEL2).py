from collections import deque
def solution(s):
    if s.count("(") != s.count(")"):
        return False
    dq = deque()
    for i in s:
        if i == "(":
            dq.append(i)
        else:
            if len(dq) == 0:
                return False
            else:
                dq.pop()
    if len(dq) != 0:
        return False
    return True