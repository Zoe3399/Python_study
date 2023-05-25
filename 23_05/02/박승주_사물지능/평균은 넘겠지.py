# 테스트 케이스 개수 C
# 학생 수가 첫수로 주어지고, 이어 학생들의 점수가 주어짐

# C만큼 반복한다
C = int(input())

for i in range(C):
    # nums[0] = 학생수 / nums[1:] = 점수들 /list 공백으로 입력받음
    nums = list(map(int,input().split()))
    score_avg = sum(nums[1:]) / nums[0] # 평균 구하기
    count = 0
    for i in nums[1:]: # 학생들의 점수들 반복
        if i > score_avg: # 평균 점수 이상인지 확인하기
            count += 1 #평균 이상인 학생 수 count 하기
    #평균이 넘는 학생 비율 = 평균이상인 학생 / 학생 수  * 100        
    top_avg = count/nums[0] * 100
    print("{:.3f}%".format(round(top_avg, 3)))
    
    '''
    round()함수를 사용해서 3번째까지만 반올림 후
    40.0% 로 출력되는 문제를 없애기 위해
    서식을 지정할 수 있는 format 메소드로
    소수점 이하 3 번째 자리까지 출력  
    '''
    
    # -------------------------------------
    
    '''
    [ round() 함수만 사용될 수 없는 이유 ]
    반올림하기 위해서 round함수를 사용하긴 하는데
    문제는, round 함수를 사용해도, 
    40.000% 가 아니라 40.0% 로 출력되기 때문에 
    round함수의 문제점 = 끝자리가 0이면 출력하지 않음
    
    
    그래서 사용한 방법이 
    서식 지정할 수 있는 format 메소드
    < 참고한 서적 > 
    https://dojang.io/mod/page/view.php?id=2300 
    
    print("{}%".format(round(원하는 수, 원하는 자릿수)))
    
    '''

'''
 다른 분들의 포맷팅 코드

    print(f'{rate:.3f}%')
    print(f'{cnt/case[0] * 100:.3f}%')
    print('%.3f' %per + '%')
    print('%.3f' % (cnt / num[0] * 100) + '%')
    print("{:.3f}%".format(ratio))
    print("%.3f"%(res/arr[0] * 100) + "%)
'''