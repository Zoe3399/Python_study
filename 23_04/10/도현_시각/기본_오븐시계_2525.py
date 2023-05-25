# https://solved.ac/profile/playdev7

# 첫째 줄에 현재 시각의 시와 분을 입력받는다.
# 둘째 줄에는 요리에 필요한 시간을 입력받는다.
# 첫째 줄의 시각에서 둘째 줄의 시간이 흐른 데이터를 출력한다.

# 시게 입력받기
hour, minute = input().split()
cooking_time = input()

# 연산을 위해 모두 정수로 변환.
hour, minute, cooking_time = int(hour), int(minute), int(cooking_time)

# 1000분까지 대응해야 하므로 반복문 사용
for i in range(cooking_time):
    minute += 1

    # 60분이 되면 1시간 증가, 24시가 되면 0시로 변경.
    if minute == 60:
        hour += 1
        minute = 0
    
    # 0시 0분이 출력되어야 하므로 if문 2개 사용 필요.
    # elif로 하면 24시 0분 -> 0시 1분이 됨. - 조건문 만족 후 바로 빠져나가므로.
    if hour == 24:
        hour = 0

# for문을 마치고 연산 결과를 출력.
print(hour, minute)