# https://solved.ac/profile/playdev7
# 인공지능사관학교 Python Study
# 4344 - 평균은 넘겠지

# 문제 - 학생의 수와 학생들의 점수가 입력되면, 평균을 초과하는 학생들의 비율을 소수점 셋 째자리 까지 반올림하여 출력하는 프로그램.
# 입력 - 테스트 케이스의 개수가 주어진다
# 다음 입력부터 자연수 집합이 공백으로 입력된다.
    # - 첫 숫자는 학생의 수 n이고, 그 다음 숫자들은 n명의 학생들의 점수 n개를 의미한다.
# 출력은 모든 케이스가 종료되고 한 번에 출력한다. 각 케이스마다 한 줄 씩 개행한다.

cases = int(input())
results = []

for case in range(cases):
    # 공백을 기준으로 입력받아 scores 리스트에 저장한다.
    scores = list(map(int, input().split()))

    # 첫 번째 요소는 학생의 수이므로 scores에서 빼서 별도로 저장한다.
    student = scores.pop(0)

    # Python 답게 sum() 메소드를 통해 평균을 간단하게 구한다.
    # mean() 은 NumPy의 메소드이므로 여기서는 사용하지 못한다.
    avg = sum(scores) / student
    # 평균을 초과할 학생의 수를 세어줄 cnt 변수 선언
    cnt = 0

    # 이후 scores를 대입하며 평균을 초과하면 cnt 1 증가.
    for i in scores:
        if avg < i:
            cnt += 1
        else:
            pass
    
    # 비율 구하기 - 평균을넘는학생수 / 전체학생수 * 100 %
    rate = round(cnt / student * 100, 3)   # round 메소드를 통해서 소수점 셋제자리수까지 표현 (넷째자리에서 반올림)

    # 예시출력에서 "%" 를 요구하므로 공백없는문자열로 만든다.
    # 소수점 세자리를 전부 채우기 위해 format() 메소드 사용
    results.append(format(rate, ".3f") + "%")


# 실제 답안 출력
for i in results:
    print(i)