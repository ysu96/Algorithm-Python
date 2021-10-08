def solution(phone_number):
    phone_number = phone_number.replace(phone_number[:-4], '*'*len(phone_number[:-4]))
    return phone_number

solution("01033334444")