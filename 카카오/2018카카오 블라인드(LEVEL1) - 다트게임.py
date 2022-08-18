def solution(dartResult):
    stack = []
    exp = {"S":1, "D":2, "T":3}
    dartResult = dartResult.replace("10", "a")
    
    for i in dartResult:
        if i.isdigit() or i == "a":
            stack.append(10 if i == 'a' else int(i))
        elif i in ("S","D","T"):
            num = stack.pop()
            stack.append(num ** exp[i])
        elif i == "#":
            num = stack.pop()
            stack.append(num *(-1))
        elif i == "*":
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(num*2)
    return sum(stack)
   