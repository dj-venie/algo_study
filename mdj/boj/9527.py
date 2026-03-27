# 1의 개수 세기 다국어
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	13027	5229	4166	42.667%
# 문제
# 두 자연수 A, B가 주어졌을 때, A ≤ x ≤ B를 만족하는 모든 x에 대해 x를 이진수로 표현했을 때 
# 1의 개수의 합을 구하는 프로그램을 작성하시오.

# 즉, f(x) = x를 이진수로 표현 했을 때 1의 개수라고 정의하고, 아래 식의 결과를 구하자.

#  
# \[\sum_{x=A}^{B}{f(x)}\] 

# 입력
# 첫 줄에 두 자연수 A, B가 주어진다. (1 ≤ A ≤ B ≤ 1016)

# 출력
# 1의 개수를 세어 출력한다.

a, b = map(int, input().split())

def bin_nth_count(n):
    if n<=0:
        return 0
    # 2진법 n자리 1의 자리 수 합
    now = 2**(n-1)
    return now + now//2 * (n-1)

def bin_nth_sum(n):
    
    if n<=0:
        return 0
    return n * 2**(n-1)

def get_sum(x):

    n = x.bit_length()
    if x <= 0:
        return 0
    elif x == 2**(n-1):
        return bin_nth_sum(n-1) + 1
    elif x == 2**(n) - 1:
        return bin_nth_sum(n)
    
    sum = bin_nth_sum(n-1) + 1

    left = x - 2**(n-1)
    sum += get_sum(left) + left
    
    return sum

la, lb = a.bit_length(),b.bit_length()

answer = 0

print(get_sum(b) - get_sum(a-1))

# 예제 입력 1 
# 2 12
# 예제 출력 1 
# 21
