- 푼 문제

- 9655번 - 돌 게임
```
점화식으로 풀 수 있다. 1개 혹은 3개만 가져갈 수 있으므로 상대방의 선택지는 n-1 혹은 n-3이 될 것이다.
따라서 자신이 가져갈 수 있는 다음 경우의 수는 n-2, n-4, n-6 총 3가지가 될 것이다.
이렇게 쭉 내려가다 보면 결국 SK는 n이 홀 수 일 때 이길 수 있고, 짝수 일 때는 방법이 없이 CY가 우승을 차지하게 된다.
```

- 1010번 - 다리 놓기
```
이차원 DP 배열 생성
서쪽에 1개, 동쪽에 n개 있을 때 다리는 n개 지을 수 있음
서쪽의 개수와 동쪽의 개수가 똑같으면 경우의 수는 1이다
서쪽 n, 동쪽 m이면 : (서쪽 n 동쪽 m-1 일떄의 경우의 수) + (서쪽 n-1, 동쪽 m-1 일 때의 경우의 수)
```
