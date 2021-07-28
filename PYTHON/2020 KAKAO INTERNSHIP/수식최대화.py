def calc(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b


def solution(expression):
    answer = 0

    # +, -, * 에 대한 연산 우선 순위
    priors = [[0, 1, 2], [0, 2, 1],[1, 0, 2], [1, 2, 0],[2, 0, 1],[2, 1, 0]]
    operands = ['*', '+', '-']

    # 문자열 에서 숫자들만 split 하여 추출
    nums_split = expression
    nums_split = nums_split.replace('+', ' ')
    nums_split = nums_split.replace('*', ' ')
    nums_split = nums_split.replace('-', ' ')
    nums_split = nums_split.split(' ')
    nums = [int(num) for num in nums_split]

    # 문자열에서 +, -, * 만 추출
    operands_split = [op for op in expression if not op.isdecimal()]

    # +, -, * 에 대한 모든 우선순위 조합에 대해서
    for prior in priors:

        _nums = nums
        _operands = operands_split

        # 정해진 우선순위 대로 계산 실행
        for i in range(3):
            stack_num = []
            stack_op = []

            stack_num.append(_nums[0])

            # 스택에 숫자와 연산자를 넣다가, 현재 계산해야 하는 연산자 일 시
            # 숫자 스택에 위의 2개, 연산자 스택의 위의 1개가 현재 계산해야 하는 식 이다
            for j in range(len(_operands)):
                stack_num.append(_nums[j+1])
                stack_op.append(_operands[j])

                # 현재 연산자가 계산해야 하는 경우
                if stack_op[-1] == operands[prior[i]]:
                    num1 = stack_num.pop(-1)
                    num2 = stack_num.pop(-1)
                    op = stack_op.pop(-1)

                    # 계산 결과를 다시 숫자 스택에 넣어줌
                    stack_num.append(calc(num2, num1, op))

            # 계산 결과 저장
            _nums = stack_num
            _operands = stack_op

        # _nums 배열에는 정상적인 계산 결과 1개의 숫자만이, _operands 는 비어있어야 한다
        assert(len(_nums) == 1)
        assert(len(_operands) == 0)
        answer = max(answer, abs(_nums[0]))

    return answer

expression = "100-200*300-500+20"	#60420
print(solution(expression))