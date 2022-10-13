import sys
read = sys.stdin.readline
eng = read()
stack = [eng[0]]
one, zero = 0, 0
if eng[0] == "0":
    zero += 1
else:
    one += 1

if len(eng)-1 == eng.count("1") or len(eng)-1 == eng.count("0"):
    print(0)
else:
    for i in range(1,len(eng)):
        if eng[i] == "1":
            if stack[0] == "0":
                stack.pop()
                one += 1
                stack.append("1")
        if eng[i] == "0":
            if stack[0] == "1":
                stack.pop()
                zero += 1
                stack.append("0")
    print(min(one,zero))

    
