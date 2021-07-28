def solution(s):
    answer = ''
    num_int = ''
    num_str = ''

    for i in range(len(s)):
        if s[i].isalpha():

            if len(num_int) != 0:
                answer += num_int
                num_int = ''
            num_str += s[i]

            if i == len(s)-1:
                while len(num_str) != 0:
                    if num_str.startswith("one"):
                        answer += '1'
                        num_str = num_str[3:]
                    elif num_str.startswith("two"):
                        answer += '2'
                        num_str = num_str[3:]
                    elif num_str.startswith("three"):
                        answer += '3'
                        num_str = num_str[5:]
                    elif num_str.startswith("four"):
                        answer += '4'
                        num_str = num_str[4:]
                    elif num_str.startswith("five"):
                        answer += '5'
                        num_str = num_str[4:]
                    elif num_str.startswith("six"):
                        answer += '6'
                        num_str = num_str[3:]
                    elif num_str.startswith("seven"):
                        answer += '7'
                        num_str = num_str[5:]
                    elif num_str.startswith("eight"):
                        answer += '8'
                        num_str = num_str[5:]
                    elif num_str.startswith("nine"):
                        answer += '9'
                        num_str = num_str[4:]
                    elif num_str.startswith("zero"):
                        answer += '0'
                        num_str = num_str[4:]

        else:
            # print(num_str)
            while len(num_str) != 0:
                if num_str.startswith("one"):
                    answer += '1'
                    num_str = num_str[3:]
                elif num_str.startswith("two"):
                    answer += '2'
                    num_str = num_str[3:]
                elif num_str.startswith("three"):
                    answer += '3'
                    num_str = num_str[5:]
                elif num_str.startswith("four"):
                    answer += '4'
                    num_str = num_str[4:]
                elif num_str.startswith("five"):
                    answer += '5'
                    num_str = num_str[4:]
                elif num_str.startswith("six"):
                    answer += '6'
                    num_str = num_str[3:]
                elif num_str.startswith("seven"):
                    answer += '7'
                    num_str = num_str[5:]
                elif num_str.startswith("eight"):
                    answer += '8'
                    num_str = num_str[5:]
                elif num_str.startswith("nine"):
                    answer += '9'
                    num_str = num_str[4:]
                elif num_str.startswith("zero"):
                    answer += '0'
                    num_str = num_str[4:]

            num_int += s[i]
            if i == len(s)-1:
                answer += num_int

    return int(answer)


# "one4seveneight"	1478
# "23four5six7"	234567
# "2three45sixseven"	234567
# "123"	123
s = "one4seveneight"
print(solution(s))