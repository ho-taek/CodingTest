def solution(dirs):
    answer = 0
    road = []
    tmp = (0,0)
    for i in dirs:
        move_result = move(i,tmp[0],tmp[1])
        move_list = [tmp,move_result]
        converse_list = [move_result,tmp]
        if [tmp, move_result] not in road and tmp != move_result:
            answer += 1
            road.append(move_list)
            road.append(converse_list)
        tmp = move_result

    return answer

def move(value,x,y):
    if value == "U":
        if y == 5:
            return (x,5)
        return (x,y+1)
    elif value == "L":
        if x == -5:
            return (-5,y)
        return (x-1,y)
    elif value == "R":
        if x == 5:
            return (5,y)
        return (x+1,y)
    else:
        if y == -5:
            return(x,-5)
        return (x,y-1)