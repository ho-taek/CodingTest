
num = set(range(1,10001))
minus_num = set()
for i in num:
    for j in str(i):
        i += int(j)
    minus_num.add(i)

answer_num = sorted(num-minus_num)
for i in answer_num:
    print(i)



        




        
