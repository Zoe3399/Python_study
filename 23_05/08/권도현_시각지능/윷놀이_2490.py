# https://solved.ac/profile/playdev7
# 2490 - 윷놀이

# 공백을 기준으로 4개의 숫자가 입력됨 0이 배, 1이 등
# 3줄에 거쳐서 입력됨.
# 도, 개, 걸, 윷, 모 순으로 A, B, C, D, E 출력

# 인덱싱 활용 - 윷, 걸, 개, 도 , 모.
yut_list = ["D", "C", "B", "A", "E"]
result = []

yut = [list(map(int, input().split())) for m in range(3)]

for i in yut:
    cnt = 0
    for j in range(len(i)):
        if i[j] == 1:
            cnt += 1
    
    result.append(yut_list[cnt])

for i in result:
    print(i)