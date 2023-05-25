#시험 성적 / https://www.acmicpc.net/problem/9498
x = int(input()) 
    #입력
print("A") if x >= 90 else print("B") if x >= 80 else print("C") if x >= 70  else print("D") if x>= 60 else print("F")
    #조건문으로 출력

#배수와 약수 / https://www.acmicpc.net/problem/5086
while True:
    # 반복문을 돌려 두 개의 수를 입력
    a, b = map(int, input().split())
    # 입력이 끝난 경우 종료
    if a == 0 and b == 0 : break
    # 첫 번째 숫자가 두 번째 숫자의 약수factor나 배수multiple인지 판단 아니라면 neither출력
    print("factor") if b % a == 0 else print("multiple") if a % b == 0 else print("neither")

#팰린드롬인지 확인하기 / https://www.acmicpc.net/problem/10988
    #문자열 입력
x=input()
    #문자열 뒤집기
y=x[::-1]
    #x와 y 비교 동일시 1 아니면 0 출력
print(1) if x==y else print(0)

# Baseball / https://www.acmicpc.net/problem/10214
    #숫자 입력
x = int(input())
for i in range(x):
    # 9개의 줄에서 연세대와 고려대의 득점을 입력
    y_total = 0  # 연세대의 총 득점
    k_total = 0  # 고려대의 총 득점
    for j in range(9):
        y, k = map(int, input().split())
        y_total += y
        k_total += k
    # 두 팀의 득점을 비교하여 이긴 팀 출력
    print("Yonsei") if y_total > k_total else print("Korea") if y_total < k_total else print("Draw")