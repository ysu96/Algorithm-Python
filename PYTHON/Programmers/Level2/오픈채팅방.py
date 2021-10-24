def solution(record):
    answer = []
    users = {}
    for r in record:
        array = list(r.split())
        if len(array) == 2:
            type, uid = array[0], array[1]
        else:
            type, uid, nickname = array[0], array[1], array[2]
            users[uid] = nickname

        if type == "Enter":
            msg = uid + "E"
            answer.append(msg)
        elif type == "Leave":
            msg = uid + "L"
            answer.append(msg)

    for i in range(len(answer)):
        type = answer[i][-1]
        uid = answer[i][:-1]
        if type == "E":
            answer[i] = users[uid] + "님이 들어왔습니다."
        else:
            answer[i] = users[uid] + "님이 나갔습니다."

    return answer


record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
solution(record)
