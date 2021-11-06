def solution(log):

    cnt = 0
    startHour = int(log[0][:2])
    startMinute = startHour*60 + int(log[0][3:])

    for i in range(1, len(log)):
        #start time
        if i%2 == 0:
            startHour = int(log[i][:2])
            startMinute = startHour * 60 + int(log[i][3:])

        #end time
        else:
            endHour = int(log[i][:2])
            endMinute = endHour*60 + int(log[i][3:])
            studyTime = endMinute - startMinute
            if studyTime < 5:
                continue

            if studyTime >= 105:
                studyTime = 105

            cnt+=studyTime


    hour = cnt // 60
    minute = cnt % 60

    answer = str(hour).zfill(2) + ':' + str(minute).zfill(2)

    return answer

print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))