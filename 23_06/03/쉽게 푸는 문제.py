# https://www.acmicpc.net/problem/1292
# 숫자 수열을 만들고
# 어느 일정 구간을 주면
# 그 구간의 합을 구하기

# 수열은 2 ** 2, 3 ** 3, 4 ** 4 이런식임.
# 구간의 시작과 끝을 나타태는 정수 A, B
A, B = map(int, input().split())

# 수열을 담을 list
arr = []    
num_sum  = 0

# 임의로 B+1까지 숫자 수열 만들기
for i in range(1, B+1):
    for j in range(i):
        arr.append(i)
# arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5 ...]

print(sum(arr[A-1:B]))
