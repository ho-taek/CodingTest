import sys

read = sys.stdin.readline

n = int(read().rstrip())


switch = list(map(int, read().split()))

switch.insert(0,-1)
m = int(read().rstrip())

def change(n):
    if n == 0:
        return 1
    else:
        return 0

for _ in range(m):
    a, b = map(int,read().split())
    j = k = b
    if a == 1:
        for idx, i in enumerate(switch):
            if idx > 0 and idx % b == 0:
                switch[idx] = change(switch[idx])
                
    else:
        switch[b] = change(switch[b])
        while j > 1 and k < n:
            j -= 1
            k += 1
            if switch[j] == switch[k]:
                switch[j] = switch[k] = change(switch[j])
            else:
                break

for i in range(1, n+1):
    print(switch[i], end= " ")
    if i %20 == 0:
        print()
            
            




    

