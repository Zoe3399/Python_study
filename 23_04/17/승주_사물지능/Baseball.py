T = int(input()) #테스트 케이스 수 T
for i in range(T): # T만큼 반복
    y_score = k_score = 0 #점수 0으로시작
    
    for i in range(9): # 9줄 입력받기
        y, k = map(int, input().split()) # 점수입력받기
        y_score += y # 연세대 점수 입력받아서 추가
        k_score += k # 고려대 점수 입력받아서 추가
    
    if y_score > k_score: #만약 연세대 점수가 높을 때
        print('Yonsei') #연세대 출력
    elif y_score < k_score: #만약 고려대 점수가 높을 때
        print('Korea') #고려대 출력
    else: # 이외에 경우 == 비긴경우 동점 Draw 출력
        print("Draw") 