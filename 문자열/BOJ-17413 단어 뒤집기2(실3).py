import sys

read = sys.stdin.readline

sentence = read().rstrip()

stack = []
answer = []
str = ""
for idx, i in enumerate(sentence):
    if idx == len(sentence)-1 and i != ">":
        str += i
        answer.append(str[::-1])
    # <일경우 스택에 넣기
    if i == "<":
        stack.append(i)
        if str != "":
            answer.append(str[::-1])
            str = ""
    
    if len(stack) > 0:
        str += i
        if i == ">":
            stack.pop(0)
            answer.append(str)
            str = ""
    else:
        if i == " ":
            answer.append(str[::-1])
            answer.append(i)
            str = ""
        else:
            str += i

print(''.join(answer))