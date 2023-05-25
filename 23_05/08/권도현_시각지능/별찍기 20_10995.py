# https://solved.ac/profile/playdev7
# 10995 - 별찍기 20

# 규칙 - n 만큼의 별과 공백을 n개의 행만큼 번갈아가며 출력
# 홀수 행은 공백이 먼저, 짝수 행은 별이 먼저.

n = int(input())

# 홀짝 구분을 위해 0부터가 아닌 1부터 n을 포함해서 반복.
for i in range(1, n+1):
    if i % 2 == 1:
        print("* " * n)
    else:
        print(" *" * n)