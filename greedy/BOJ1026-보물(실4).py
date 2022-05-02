n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

while a:
    maxa = max(a)
    aindex = a.index(maxa)
    a.pop(aindex)

    minb = min(b)
    bindex = b.index(minb)
    b.pop(bindex)

    result += maxa*minb    

print(result)
