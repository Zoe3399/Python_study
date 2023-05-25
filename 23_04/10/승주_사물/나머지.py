A,B = map(int, input().split()) # 공백을 기준으로 입력 받기
C = int(input())
print((A+B)%C,((A%C) + (B%C))%C ,(A*B)%C,((A%C) * (B%C))%C  ,sep='\n')
# 줄바꿈으로 출력
