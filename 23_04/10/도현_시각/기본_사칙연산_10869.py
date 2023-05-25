# https://solved.ac/profile/playdev7

# 두 자연수 A와 B가 주어진다.
# 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

# input() 하위 메소드인 split() 메소드 통한 a, b 입력받기
a, b = input().split()

# 문자열로 받아지므로 정수로 변환.
a, b = int(a), int(b)

# 연산 결과 각각 출력
print(a+b)
print(a-b)
print(a*b)
# Python에서는 몫만 나눌 경우 슬래시 두 개.
print(a//b)
print(a%b)