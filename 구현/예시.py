s = input()
numRows = int(input())

answer = ""
index = -1
index_check = 0
tmp = False
for i in s :
    if tmp == False :
        index += 1
    else:
        index -= 1

    if index_check == index :
        answer += i
            
    
    if index == numRows - 1:
         tmp == True

    if index == 0:
         tmp = False
print(answer)

    
    

    