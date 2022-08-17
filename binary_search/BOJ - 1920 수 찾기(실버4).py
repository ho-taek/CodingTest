import sys

read = sys.stdin.readline
n = int(read())

num = list(map(int, read().split(" ")))

m = int(read())
differ = list(map(int, read().split(" ")))

for i in differ:
    print(1) if i in num else print(0)