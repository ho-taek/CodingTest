def solution(sizes):
    
    for i in sizes:
        if i[1] > i[0]:
            i[0],i[1] = i[1],i[0]
    width, height = 0,0
    
    for i in sizes:
        if i[0] > width:
            width = i[0]
        if i[1] > height:
            height = i[1]
            
    return height*width