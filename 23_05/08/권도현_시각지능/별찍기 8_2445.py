# https://solved.ac/profile/playdev7
# 2445 - 별찍기 8

# 문제 - 입력된 숫자 * 2 - 1 개의 행을 가진 나비모양 출력.
row = int(input())

# 입력된 숫자부터 row 행까지 출력.
for i in range(1, row+1):
    # i만큼 별 문자를 곱해서 출력
    print("*" * i, end ="")
    # row - i 만큼 공백 문자를 곱해서 출력
    print(" " * (row - i), end ="")
    # row - i 만큼 공백 문자를 곱해서 출력
    print(" " * (row - i), end ="")
    # i만큼 별 문자를 곱해서 출력
    print("*" * i, end ="")
    # 이후 개행
    print()

# row+1번째 행부터는 역으로
for j in range(1, row):
    # row - j 만큼의 별 문자를 곱해서 출력
    print("*" * (row - j), end="")
    # j 만큼의 공백 출력
    print(" " * j, end ="")
    # j 만큼의 공백 출력
    print(" " * j, end ="")
    # row - j 만큼의 별 문자를 곱해서 출력
    print("*" * (row - j), end="")
    # 개행
    print()