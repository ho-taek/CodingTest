def solution(p):
    answer = ''
    if isCorrect(p): return p
    
    answer = rec(p)
    
    return answer

def sepUV(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:] if i+1 < len(p) else ""
            break
    return u, v
    
def isCorrect(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if not len(stack):
                return False
            elif stack[-1] == '(':
                stack.pop()
    return False if len(stack) else True

def rec(p):
    result = ""
    if not len(p): return ""
    u,v = sepUV(p)
    if isCorrect(u):
        result = u + rec(v)
    else:
        tmp = "("
        tmp += rec(v)
        tmp += ")"
        u = u[1:-1]
        for c in u:
            if c == '(':
                tmp+=')'
            else:
                tmp+='('
        result += tmp
    return result