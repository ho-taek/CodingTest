def solution(numbers, target):
    sol = [0]
    for i in numbers:
        solve = []
        for j in sol:
            solve.append(j+i)
            solve.append(j-i)
        sol = solve
    return sol.count(target)
