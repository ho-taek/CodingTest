def solution(str1, str2):
    list_str1 = []
    list_str2 = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha() == True:
            list_str1.append(str1[i:i+2].upper())
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha() == True:
            list_str2.append(str2[i:i+2].upper())
            
    if len(list_str1)==0 and len(list_str2)==0:
        return 65536
    print(list_str1, list_str2)
    solution = intersection(list_str1, list_str2)/union(list_str1, list_str2) 
    return int(solution*65536)
#합집합
def union(list_str1,list_str2):
    check = []
    count = 0
    for i in set(list_str1):
        A_count,B_count  = list_str1.count(i),list_str2.count(i)
        count += max(A_count,B_count)
        
    for j in set(list_str2):
        if j not in list_str1:
            count += list_str2.count(j)
    print(count)
    return count

def intersection(list_str1, list_str2):
    count = 0
    for i in set(list_str1):
        if i in list_str2:
            A_count,B_count  = list_str1.count(i),list_str2.count(i)
            count += min(A_count,B_count)
            
    print(count)
    return count