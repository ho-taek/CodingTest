def solution(n, arr1, arr2):
    answer = [0]*n
    array_one = bin_str(n,arr1)
    array_two = bin_str(n,arr2)
    
    for i in range(n):
        string = ""
        for j in range(n):
            if array_one[i][j] == "1" or array_two[i][j] == "1":
                string += "#"
            else:
                string += " "
        answer[i] = string
    
    return answer

def bin_str_zero(n,string):
    count = len(string)
    zero = str(0)*(n-count)
    return zero+string

def bin_str(n,arr):
    for idx,i in enumerate(arr):
        binary = bin(i)[2:]
        arr[idx] = bin_str_zero(n,binary)
    return arr