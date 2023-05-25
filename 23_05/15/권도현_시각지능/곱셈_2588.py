# https://solved.ac/profile/playdev7
# 2588 / 곱셈

# 문제
# 세 자리수 곱셈에 대하여 첫째자리수, 둘째자리수, 셋째자리수 곱셈 결과를 순차출력 및 이후 최종 연산결과 출력

# 입력
# 세 자리수 두 개가 개행되어 입력된다.

# 출력
# 네 줄에 거쳐 a * b 첫째자리수, 둘째자리수, 셋쩨자리수 곱셈결과, 마지막줄에 최종 곱셈결과 출력

a = int(input())
b = input()

print(a * int(b[2:]))
print(a * int(b[1:2]))
print(a * int(b[:1]))
print(a * int(b))