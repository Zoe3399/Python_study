# https://solved.ac/profile/playdev7
# 10995 - 별찍기 12

# 규칙 - n개의 행을 가진 5시방향 직각인 삼각형과
# 첫 줄 빠진 n-1개 행을 가진 2시방향 직각삼각형 출력.

n = int(input())

# n개의 행을 가진 5시방향이 직각인 직각삼각형 구현
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * i)

# n-1개의 행을 가진 첫 줄 빠진 2시방향 직각삼각형 구현 
for j in range(1, n):
    print(" " * j, end="")
    print("*" * (n-j))