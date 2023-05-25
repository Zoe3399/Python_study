# Dohyeon Kwon (playdev7)
# 2023-04-18

# 올림 연산을 위해 math 라이브러리 추가
import math

def solution(fees, records):
    
    # 주차요금을 담는 정답 리스트.
    answer = []
    
    # 입차 기록을 담을 리스트 선언
    in_list = []
    # 출차 기록을 담을 리스트 선언
    out_list = []
    # 차량 번호를 담을 리스트 선언
    car_list = []
    
    # 입차 기록과 출차 기록을 담는 반복문
    for i in records:
        if i[11:] == "IN":
            in_list.append(i)
        else:
            out_list.append(i)
    
    # 챠랑 번호를 car_list에 담는 반복문
    for i in records:
        # 이미 들어있으면 pass
        if car_list.count(i[6:10]) >= 1:
            pass
        # 아니면 car_list에 추가.
        else:
            car_list.append(i[6:10])
            
    # 이후 car_list 오름차순 정렬
    car_list.sort()
        
    # 차량 번호가 작은 순서대로 주차 시간과 요금을 구하고 answer에 추가되도록 다중 for문 선언
    for i in car_list:
        # 누적 주차 시간을 담을 변수 timer 선언
        timer = 0
        
        # 해당 차량에 해당하는 입차 리스트만 추린 this_in 선언
        this_in = []
        for j in in_list:
            if i in j:
                this_in.append(j)
        
        # 해당 차량에 해당하는 출차 리스트만 추린 this_out 선언
        this_out = []
        for k in out_list:
            if i in k:
                this_out.append(k)
        
        
        # this_out 보다 this_in의 길이가 더 길면 입차가 마지막임.
        # 따라서 마지막 입차에 대해 23:59 와의 시간 차이 또한 누산 필요.
        if len(this_in) > len(this_out):
            for i in range(len(this_in) - 1):
                timer += (int(this_out[i][:2]) * 60 + int(this_out[i][3:5])) - (int(this_in[i][:2]) * 60 + int(this_in[i][3:5]))
            # 마지막 입차에 대한 23:59 와의 시간 차이 누산.
            timer += (23 * 60 + 59) - (int(this_in[-1][:2]) * 60 + int(this_in[-1][3:5]))
        else:
            for i in range(len(this_in)):
                timer += (int(this_out[i][:2]) * 60 + int(this_out[i][3:5])) - (int(this_in[i][:2]) * 60 + int(this_in[i][3:5]))
            print(timer)
        
     
        # 다음 차량으로 가기 전 answer에 정산된 요금 추가
        # 공식 - 기본요금 + {(누적시간 - 기본시간) / 단위시간} * 단위요금
        
        # 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
        if timer < fees[0]:
            answer.append(fees[1])
        
        # 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다. - math.ceil
        else:
            answer.append(fees[1] + math.ceil((timer - fees[0]) / fees[2]) * fees[3])            
            
    return answer