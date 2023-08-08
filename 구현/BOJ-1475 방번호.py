n = input()

num_list = [0]*9
six_nine = 0


for i in n:

    if i != "6" and i != "9":
        num_list[int(i)] += 1
    else:
        six_nine += 1

six_nine = six_nine//2 + six_nine%2
max_num_list = max(num_list)
answer = max(max_num_list, six_nine)

print(answer)
