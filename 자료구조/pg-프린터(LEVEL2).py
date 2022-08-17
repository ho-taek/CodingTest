def solution(priorities, location):
    answer = 1
    while len(priorities) != 0:
        if location == 0:
            if priorities[0] == max(priorities):
                return answer
            else:
                num = priorities.pop(0)
                priorities.append(num)
                location = len(priorities)-1
        else:
            if priorities[0] == max(priorities):
                priorities.pop(0)
                answer += 1
            else:
                num = priorities.pop(0)
                priorities.append(num)
            location -= 1
            
                    