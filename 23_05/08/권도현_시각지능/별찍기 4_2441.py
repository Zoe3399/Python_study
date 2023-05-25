# https://solved.ac/profile/playdev7
# 2441 - 별찍기 4

# 문제 - 입력된 숫자만큼 첫 행에 별을 찍고 이후 2시방향이 직각인 직각삼각형 찍어주기.

row = int(input())

for i in range(row):
    # i만큼 공백 문자를 곱해서 출력
    print(" " * i, end ="")
    # row - i 만큼 별 문자를 곱해서 출력
    print("*" * (row - i), end ="")
    # 한줄이 끝났으니 개행
    print()