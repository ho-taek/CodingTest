from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        stack = deque(skill)
        pointer = 0
        for j in i:
            if j in skill:
                if stack.popleft() != j:
                    pointer = -1
                    break
        if pointer != -1:
            answer += 1
                
    return answer