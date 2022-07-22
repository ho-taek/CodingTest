from itertools import permutations
def solution(expression):
    sign = ["-","+","*"]
    express = list(permutations(sign, 3))
    answer = []
    for i in express:
        answer.append(result(expression, i))
        
    return max(answer)

def result(expressions, op):
    tmp = ""
    li = []
    for i in expressions:
        if i.isdigit() == True:
            tmp += i
        else:
            li.append(tmp)
            li.append(i)
            tmp = ""
    li.append(tmp)
    
    for i in op:
        stack = []
        while len(li) != 0:
            tmp = li.pop(0)
            if tmp == i:
                stack.append(operation(stack.pop(), li.pop(0), i))
            else:
                stack.append(tmp)
        li = stack
    return abs(int(li[0]))
    
    

def operation(num1,num2,op):
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '+':
        return str(int(num1) + int(num2))
    if op == "*":
        return str(int(num1) * int(num2))


