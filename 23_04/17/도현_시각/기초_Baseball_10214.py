# https://solved.ac/profile/playdev7

# 문제 - 야구 경기의 결과를 출력하는 프로그램
# 1회부터 9회까지 득점수가 출력되는데, 이를 합산하여 승자 또는 비김을 결정한다.

# 게임 수를 입력받는다.
game = int(input())

# 게임 수 만큼 반복한다.
for i in range(game):
    # K, Y 변수를 0으로 초기화하여 선언한다.
    K, Y = 0, 0
    # 1회부터 9회까지 반복한다.
    for i in range(9):
        # 입력받는 득점 수를 y_score 와 k_score 에 대입한다.
        y_score, k_score = map(int, input().split())

        # K 와 Y에 각 score를 더해준다.
        K += k_score
        Y += y_score

    # 이번 게임의 승자를 확인하고, 출력하는 부분
    
    # 고대 승리
    if K > Y:
        print("Korea")
    
    # 비겼을 때
    elif K == Y:
        print("Draw")
    
    # 그 외
    else:
        print("Yonsei")

    # game의 값이 2이상이라면 그만큼 반복되고, 출력된다. 끝.