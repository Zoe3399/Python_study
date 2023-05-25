# 3. 평균은 넘겠지 (https://www.acmicpc.net/problem/4344)

Test_c = int(input()) # N번 케이스를 입력하겠다는 뜻.
# Stu = list(map(int,input().split())) -> 인덱스 첫번째는 학생 수, 뒤에는 다 점수
for i in range(Test_c) : #케이스 수 만큼 반복하시오
    Student = list(map(int,input().split()))
    Avg = sum(Student[1:]) / Student[0]

    # 승주님 풀이 참고
    count = 0
    for i in Student[1:]: # 점수들을 반복 체크
        if i > Avg:
            count += 1 # 해당 학생 카운트
    
    up_avg = count / Student[0] * 100  # 평균 이상 학생 수 / 해당 시험 본 총 학생 수 * 100
    #조건은 완성.
    #print(round(up_avg, 3)) -> "40.0" 으로 출력 됨

    
    print("{:.3f}%".format(up_avg))
    # {}.format(up_avg) -> up_avg의 값을 "{}"에 맞게 출력
    # "{:.3f}%" 는 {소숫점 셋째자리까지} % 랑 같이 (up_avg) 출력.
