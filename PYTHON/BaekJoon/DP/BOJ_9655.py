
# 탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개 또는 3개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.
# 두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.

# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)
# 상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.
import sys
input = sys.stdin.readline
N = int(input())
player = 1
while N != 0:
    if N-3 == 1:
        N-=1
        player *= -1

    elif N-3 == 2:
        N-=3
        player *= -1

    elif N-3 == 3:
        N-=1
        player *= -1

    elif N == 3:
        N-=3

    elif N == 1:
        N-=1

    elif N == 2:
        N-=1
        player *= -1

    else:
        N-=3
        player *= -1

if player == 1:
    print('SK')
else:
    print('CY')



