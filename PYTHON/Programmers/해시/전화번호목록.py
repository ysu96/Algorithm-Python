# def solution(phone_book):
#     phone_book.sort(key=len)
#     shortest = phone_book[0]
#     phone_book = phone_book[1:]
#     l = len(phone_book)
#     while l != 0:
#         for i in range(l):
#             if phone_book[i].startswith(shortest):
#                 return False
#         shortest = phone_book[0]
#         phone_book = phone_book[1:]
#         l -= 1
#     return True

#해시 풀이법
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


phone_book = ["119","123", "12", "1195524421", "97674223" ]
aaa = {"111":"bbb", "222":"aaa"}
print("11" in aaa)
# print(solution(phone_book))