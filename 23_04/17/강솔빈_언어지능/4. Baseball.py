# 4.Baseball (https://www.acmicpc.net/problem/10214)
# 케이스의 수를 의미하는 자연수 T. T개의 테스트 케이스.
#9줄에 걸쳐서 입력,
#매 줄마다 해당 회의 연세대 득점 Y와 고려대 득점 K가 공백으로 구분되어 주어진다. 이 두 수는 0이상 9이하이다
#승주님 답안 참고

R = int(input())

for i in range(R): #자연수 T 개의 테스트 케이스 -> 반복
    Yonsei = Korea = 0 #점수 0으로시작
    
    for i in range(9): # 9줄 입력받기
        Y, K = map(int, input().split()) # 점수입력받기 #공백으로 구분
        Yonsei = Yonsei + Y # (Yonsei += Y 로 표시가능)
        Korea += K
    #요기까지 해당 게임 점수 합계 담김


    if Yonsei > Korea: 
        print('Yonsei') 
    elif Yonsei < Korea: 
        print('Korea') 
    else: 
        print("Draw")
