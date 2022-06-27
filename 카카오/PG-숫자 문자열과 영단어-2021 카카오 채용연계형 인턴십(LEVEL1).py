def solution(s):
    number = {0:"zero",1:"one", 2:"two",3:"three",4:"four",
        5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    if s.isdigit() == True:
        return int(s)
    for i in range(0,10):
        if number[i] in s:
            s = s.replace(str(number[i]), str(i))
        
    return int(s)
