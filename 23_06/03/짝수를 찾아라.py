# https://www.acmicpc.net/problem/3058

# 7개의 자연수가 주어질 때, 
# 이들 중 짝수인 자연수들만 골라서 합을 구하고
# 고른 짝수들 중 최솟값을 찾는 프로그램

# T = 테스트 데이터
# 각 테스트 데이터는 한줄로 구성
# 7개의 자연수가 공백으로 구분
# 입력으로 주어지는 자연수 >= 1
# 7개 중 적어도 하나는 짝수

# 테스트 데이터
T = int(input())

# T만큼 반복
for i in range(T):
    
    # 짝수 담을 list
    even_list = []

    # 짝수 합
    even_num = 0
    
    # list를 공백으로 입력받기(한줄로 구성)
    test_data = list(map(int, input().split())) 

    # 짝수인 자연수만 고르기
    for i in test_data:
        if i % 2 == 0: # 2로 나눴을 때 나머지 0
            # 짝수 리스트에 담기
            even_list.append(i)
            even_num += i # 짝수 값 다 더하기

    # 짝수 합, 최솟값
    print(even_num, min(even_list)) # 최솟값 구하는 min함수 사용
    
    


