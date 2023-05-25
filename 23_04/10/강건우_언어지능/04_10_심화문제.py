#주차 요금 계산 https://school.programmers.co.kr/learn/courses/30/lessons/92341?language=python3

#메인 함수
def solution(fees, records):
    answer, data, c_time, last_time = [],{},{},get_time("23:59")
    for record in records:
        time, num, inout = record.split(" ")
        if num not in data.keys(): data[num] = [last_time, last_time]
        if inout == "IN":
            data[num][0] = get_time(time)
        elif inout == "OUT":
            data[num], data[num][1],c_time[num] = [last_time, last_time], get_time(time), (c_time.get(num, 0) + data[num][1] - data[num][0])
    for key in data.keys():
        c_time[key] = c_time.get(key, 0) + data[key][1] - data[key][0]
    for item in sorted(c_time.items()):
        key, value = item
        answer.append((key, get_charge(fees, value)))
    answer = [x[1] for x in answer]
    return answer
#시간 합하는 함수
def get_time(time):
    s_h, s_m = time.split(":")
    return int(s_h)*60+int(s_m)
#요금 구하는 함수
def get_charge(fees, diff):
    b_time, b_charge, u_time, u_charge = fees
    diff -= b_time
    if diff <= 0:
        return b_charge
    return b_charge + ((diff - 1) // u_time + 1) * u_charge
