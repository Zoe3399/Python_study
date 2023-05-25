# 시, 분, 입력값 입력 받기
A, B = map(int, input().split())
C = int(input())

# 시
Hour = (B+C) // 60
t_min = (B+C)%60
if(B+C >= 60):
    if(A+Hour >= 24):
        A = A-24
    A=A+Hour
    print(A, t_min)
else:
    if(A>=24):
        A = A - 24
    print(A, B+C)