import sys

read = sys.stdin.readline


n = int(read())
len_n = len(str(n))

count = 0
for i in range(len_n - 1):
    count += 9 * 10 ** i*(i+1)


answer = count + (n-10**(len_n-1)+1)*len_n
print(answer)
    
