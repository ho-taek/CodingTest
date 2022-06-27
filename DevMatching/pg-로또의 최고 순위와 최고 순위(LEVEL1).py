def solution(lottos, win_nums):
    win = {6:1,5:2,4:3,3:4,2:5}
    win_cnt = 0
    loss_cnt = 0
    answer = []
    for i in lottos:
        if i == 0:
            win_cnt += 1
        elif i in win_nums:
            win_cnt += 1
            loss_cnt +=1

    answer.append(win.get(win_cnt,6))
    answer.append(win.get(loss_cnt,6))
    return answer
