def solution(code, day, data):
    answer = []
    for d in data:
        p,c,t = d.split()
        p=p[6:]
        c=c[5:]
        td=t[5:13]
        th=t[13:15]
        if td == day and c==code:
            answer.append((int(th),int(p)))
        answer.sort()
        answer2 = []
        for h,p in answer:
            answer2.append(p)

    return answer2



company_code = "012345"
day="20190620"
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
#[110, 90]
print(solution(company_code,day,data))