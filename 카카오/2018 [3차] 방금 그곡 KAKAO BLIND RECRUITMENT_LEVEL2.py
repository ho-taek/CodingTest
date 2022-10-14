def solution(m, musicinfos):
    dic = {}
    dic_time = {}
    m = change(m)
    for i in range(len(musicinfos)):
        start,end,song,code = musicinfos[i].split(",")
        # 코드 #부분 변경
        code = change(code)
        
        cal = calculate(start,end)
        dic_time[song] = cal
        plus = cal % len(code)
        division = cal // len(code)
        value = code*division + code[:plus]
        
        if m in value:
            dic[song] = len(value)
    if len(dic) == 0:
        return "(None)"
    
    sort = sorted(dic.items(), key=lambda x : x[1] ,reverse = True)
    max = sort[0][1]
    
    answer = ""
    answer_count = 0
    for i in sort:
        if i[1] == max and dic_time[i[0]] > answer_count:
            answer_count = dic_time[i[0]]
            answer = i[0]
            
    return answer

def calculate(start, end):
    start_hour, start_minute = map(int, start.split(":"))
    start = start_hour*60 + start_minute
        
    end_hour, end_minute = map(int, end.split(":"))
    end = end_hour*60+end_minute
    return end - start

def change(eng):
    eng = eng.replace("C#","-")
    eng = eng.replace("D#","+")
    eng = eng.replace("F#","=")
    eng = eng.replace("G#",")")
    eng = eng.replace("A#","*")
    return eng