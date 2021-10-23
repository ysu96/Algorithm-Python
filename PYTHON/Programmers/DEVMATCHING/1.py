
def solution(registered_list, new_id):
    if new_id not in registered_list: return new_id

    if new_id[-1].isalpha():
        S = new_id
        N = 0
    else:
        for i in range(len(new_id)):
            if new_id[i].isdigit():
                S = new_id[:i]
                N = int(new_id[i:])
                break

    ll = len(S)
    new_registered_list = [int(i[ll:]) if i[ll:].isdigit() else 0 for i in registered_list if S in i]
    #
    # for z in range(len(new_registered_list)):
    #     if new_registered_list[z] == '':
    #         new_registered_list[z] = 0
    #     else:
    #         new_registered_list[z] = int(new_registered_list[z])

    nrl = new_registered_list

    while 1:
        if N in nrl:
            N = N+1
        else:
            answer = S + str(N)
            return answer


    #
    # while 1:
    #     if new_id not in registered_list: return new_id
    #     else:
    #         if new_id[-1].isalpha():
    #             S = new_id
    #             new_id = new_id + '1'
    #             continue
    #
    #         for i in range(len(new_id)):
    #             if new_id[i].isdigit():
    #                 S = new_id[:i]
    #                 N = new_id[i:]
    #                 break
    #         # if len(N) == 0: N = '0'
    #         intN = int(N)+1
    #         new_id = S+ str(intN)

solution(["cow", "cow11", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"],	"cow1")