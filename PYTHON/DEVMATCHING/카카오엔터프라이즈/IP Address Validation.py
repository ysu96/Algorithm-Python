def validateAddresses(addresses):
    answer = []
    for address in addresses:
        check = True
        # : or .

        if '.' in address:
            # .이 많거나 :도 같이 있으면 아님
            if address.count('.') != 3 or ':' in address:
                answer.append("Neither")
                check = False
                continue

            groups = address.split('.')
            if len(groups) != 4:
                answer.append("Neither")
                check = False
                continue

            for group in groups:
                #255보다 크면 or 길이가 3보다 크면
                try:
                    if int(group) > 255 or len(group) > 3:
                        answer.append("Neither")
                        check = False
                        break
                except ValueError:
                    answer.append("Neither")
                    check = False
                    break

                # 맨 앞이 0이면

                if group[0] == '0' and int(group) != 0:
                    # 8진수가 8보다 크면
                    if int(group[1:]) >= 8:
                        answer.append("Neither")
                        check = False
                        break
            if check:
                answer.append("IPv4")


        elif ':' in address:
            # .도 같이 있으면 아님
            if '.' in address:
                answer.append("Neither")
                print(1)
                check = False
                continue

            # ::이 한번 이상 있으면
            if address.count("::") > 1:
                answer.append("Neither")
                print(2)
                check = False
                continue

            if "::" in address:
                groups = address.split(':')
                groups = [group for group in groups if group != '']

                print(groups)
                if len(groups) >= 6:
                    answer.append("Neither")
                    print(3)
                    check = False
                    continue

                for group in groups:
                    if len(group) > 4:
                        answer.append("Neither")
                        print(4)
                        check = False
                        break

                    try:
                        intNum = int(group, 16)
                    except ValueError:
                        answer.append("Neither")
                        print(5)
                        check = False
                        break

            else:
                groups = address.split(':')
                print(groups)
                if len(groups) != 8:
                    answer.append("Neither")
                    print(6)
                    check = False
                    continue

                for group in groups:
                    if len(group) > 4:
                        answer.append("Neither")
                        print(7)
                        check = False
                        break

                    try:
                        intNum = int(group, 16)
                    except ValueError:
                        answer.append("Neither")
                        print(8)
                        check = False
                        break
            if check:
                answer.append("IPv6")
        else:
            answer.append("Neither")

    return answer

print(validateAddresses(["::1"]))
# test = "2001:db8::ff00:42:8329"
# groups = test.split(':')
# groups.remove('')
# print(groups)
# print(int('262g', 16))
# print(int('4', 16))