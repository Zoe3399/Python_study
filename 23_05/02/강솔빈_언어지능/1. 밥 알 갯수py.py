# 1. 밥 알 갯수 (https://www.acmicpc.net/problem/27294)

#주어진 시간이 술과 같이 먹거나 OR 점심식사가 아닐때(not 점심 ->아침,저녁식사)280개. 점심 식사 이면서 and 술과 같이 먹지 않을때. 320개.

#첫째줄에 T 시간 정보, 술의 유무.

meal_t , with_a = map(int,input().split())

if not(12 <= meal_t <= 16) or (with_a == 1) :
    print(280)
else :
    print(320)