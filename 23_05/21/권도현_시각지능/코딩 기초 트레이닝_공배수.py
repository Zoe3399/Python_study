# https://school.programmers.co.kr/learn/courses/30/lessons/181936?language=python3

def solution(number, n, m):
    # 두 수 모두 나뉘어 떨어지면 공배수이다.
    if number % n == 0 and number % m == 0:
        answer = 1
    else:
        answer = 0
    
    return answer