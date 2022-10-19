import math
def solution(n, k):
    notation = change(n,k)
    notation_str = str(notation).split("0")
    print(notation_str)
    answer = 0
    
    for i in notation_str:
        if i != '' and i != '1':
            notation_num = int(i)
            for j in range(2,int(math.sqrt(notation_num)+1)):
                if notation_num % 2 == 0:
                    break
                else:
                    if notation_num % j == 0:
                        break
            else:
                answer += 1
    return answer

#진법 구하기
def change(n,k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1] 