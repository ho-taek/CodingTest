def solution(board, moves):
    stack = [0]
    count = 0
    point = 1
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if stack[point-1] == board[j][i-1]:
                    stack.pop(point-1)
                    point -= 1
                    count += 2
                    board[j][i-1] = 0
                    break
                        

                point += 1
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break

    return count
