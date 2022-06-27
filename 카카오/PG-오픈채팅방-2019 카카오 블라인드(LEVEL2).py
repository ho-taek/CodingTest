from collections import defaultdict
def solution(record):

    answer=[]
    nickname = defaultdict(str)
    for i in record:
        if "Leave" not in i:
            a,b,c = i.split(" ")
            if nickname[b] != c:
                nickname[b] = c

    for i in record:
        if "Enter" in i:
            a,b,c = i.split(" ")
            answer.append(str(nickname[b])+"님이 들어왔습니다.")
        elif "Leave" in i:
            a,b = i.split(" ")
            answer.append(str(nickname[b])+"님이 나갔습니다.")


    
    return answer
