import sys

read = sys.stdin.readline

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = read().rstrip()

for i in cro:
    word = word.replace(i, ".")

print(len(word))
