# RGB거리 2
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.5 초 (추가 시간 없음)	128 MB	23168	14089	11682	61.034%
# 문제
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
r_min_costs = [[0,0,0] for i in range(n-1)]
g_min_costs = [[0,0,0] for i in range(n-1)]
b_min_costs = [[0,0,0] for i in range(n-1)]

r1,g1,b1 = map(int, input().split())
r2,g2,b2 = map(int, input().split())

r_min_costs[0] = [float('inf'), r1 + g2, r1 + b2]
g_min_costs[0] = [g1 + r2, float('inf'), g1 + b2]
b_min_costs[0] = [b1 + r2, b1 + g2, float('inf')]


for idx in range(1,n-1):
    r,g,b = map(int, input().split())
    
    before_r, before_g, before_b = r_min_costs[idx-1]
    r_min_costs[idx] = [min(before_b, before_g)+r, min(before_r, before_b)+g, min(before_r, before_g)+b]
    before_r, before_g, before_b = g_min_costs[idx-1]
    g_min_costs[idx] = [min(before_b, before_g)+r, min(before_r, before_b)+g, min(before_r, before_g)+b]
    before_r, before_g, before_b = b_min_costs[idx-1]
    b_min_costs[idx] = [min(before_b, before_g)+r, min(before_r, before_b)+g, min(before_r, before_g)+b]

r_min = min(r_min_costs[-1][1],r_min_costs[-1][2])
g_min = min(g_min_costs[-1][0],g_min_costs[-1][2])
b_min = min(b_min_costs[-1][0],b_min_costs[-1][1])

print(min(r_min, g_min, b_min))


# 예제 입력 1 
# 3
# 26 40 83
# 49 60 57
# 13 89 99
# 예제 출력 1 
# 110
# 예제 입력 2 
# 3
# 1 100 100
# 100 1 100
# 100 100 1
# 예제 출력 2 
# 3
# 예제 입력 3 
# 3
# 1 100 100
# 100 100 100
# 1 100 100
# 예제 출력 3 
# 201
# 예제 입력 4 
# 6
# 30 19 5
# 64 77 64
# 15 19 97
# 4 71 57
# 90 86 84
# 93 32 91
# 예제 출력 4 
# 208
# 예제 입력 5 
# 8
# 71 39 44
# 32 83 55
# 51 37 63
# 89 29 100
# 83 58 11
# 65 13 15
# 47 25 29
# 60 66 19
# 예제 출력 5 
# 253
