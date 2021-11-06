def solution(time, plans):
    answer = ''
    for plan in plans:
        place, start, end = plan
        startTime = int(start[:-2])
        #24시간으로 변경
        if startTime == 12:
            if start[-2:] == "AM": startTime = 0
            else: startTime = 12
        else:
            if start[-2:] == "PM":
                startTime += 12

        #금요일 출근시간 전 출발
        if startTime < 9.5:
            startTime = 9.5

        #금요일 퇴근시간
        need = 18 - startTime
        if need > 0:
            if time-need < 0:
                return answer
            else:
                time -= need

        endTime = int(end[:-2])
        if endTime == 12:
            if end[-2:] == "AM":
                endTime = 0
            else:
                endTime = 12
        else:
            if end[-2:] == "PM":
                endTime += 12

        #월요일 퇴근 시간 후 도착
        if endTime > 18:
            endTime = 18

        #월요일 출근시간
        need = endTime - 13
        if need > 0:
            if time-need < 0:
                return answer
            else:
                time -= need
        
        answer = place

    return answer

print(solution(6, [ ["홍콩", "12PM", "12PM"], ["엘에이", "12AM", "12PM"] ]))
