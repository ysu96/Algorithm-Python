def solution(s):
    answer = ""
    numstr = ""
    for i in range(0, len(s)):
        if s[i].isdigit() == False:
            numstr+=s[i]

            if numstr == "one":
                answer += '1'
                numstr = ""
            elif numstr == "two":
                answer += '2'
                numstr = ""
            elif numstr == 'three':
                answer += '3'
                numstr = ""
            elif numstr == 'four':
                answer += '4'
                numstr = ""
            elif numstr == 'five':
                answer += '5'
                numstr = ""
            elif numstr == 'six':
                answer += '6'
                numstr = ""
            elif numstr == 'seven':
                answer += '7'
                numstr = ""
            elif numstr == 'eight':
                answer += '8'
                numstr = ""
            elif numstr == 'nine':
                answer += '9'
                numstr = ""
            elif numstr =='zero':
                answer += '0'
                numstr = ""


        else:
            if numstr != "":
                if numstr == "one": answer += '1'
                elif numstr == "two": answer += '2'
                elif numstr == 'three': answer += '3'
                elif numstr == 'four': answer+='4'
                elif numstr == 'five': answer+='5'
                elif numstr == 'six': answer+='6'
                elif numstr == 'seven': answer+='7'
                elif numstr == 'eight': answer+='8'
                elif numstr == 'nine': answer +='9'
                else: answer +='0'
                numstr = ""
            answer += s[i]
    return int(answer)

print(solution("one4seveneight"))