# 인공지능사관학교 Python 스터디
# 신고 결과 받기 - 2022 KAKAO BLIND RECRUITMENT

# id_list 에는 사용자 리스트가 입력됨
# report 는 공백을 기준으로 "신고자 불량유저" 문자열을 원소로 담는 1차원 배열임
# k는 이용 정지 기준임. - 신고 누적수가 k 이상이 되면 해당 이용자는 정지됨.

# 동일 유저가 여러번 신고 해도 1회로 처리 됨 => 다른 유저가 신고했을 때에 대한 BFS 필요
# 정지된 유저에 대해 한 번 이상 신고했던 유저는 신고 결과 메일을 받아보게 됨.

def solution(id_list, report, k):
    # 정답 배열을 사용자 수 만큼 0이 담긴 배열로 초기화.
    answer = [0] * len(id_list)

    # 사용자에게 가입 순서대로 가입 번호를 부여하는 딕셔너리 생성.
    # 키가 문자열, 값이 숫자.
    user_dict = {}
    for id in range(len(id_list)):
        user_dict[id_list[id]] = id
    

    # 딕셔너리로 불량유저를 키로 하는 신고 리스트 생성
    reporting_dict = {}
    for report in report:
        # 공백을 기준으로 신고자와 불량유저를 담음
        reporter, fault = report.split(" ")
        
        # 이후 불량유저를 키로 하고 신고자를 값으로 추가함
        # value를 리스트화 하여 여러 신고자를 담을 수 있도록 딕셔너리 구성.
        if fault in reporting_dict:
            # 신고자가 동일 할 경우 pass - 동일 신고자가 누적 신고해도 1회로 간주함.
            if reporter in reporting_dict[fault]:
                pass
            else:
                reporting_dict[fault].append(reporter)
        else:
            reporting_dict[fault] = [reporter]
    

    # 신고 딕셔너리를 순회하며 value가 k 이상이면 user_dict를 참고하여 정답 배열에 1 추가
    # 단순히 딕셔너리를 대입하면 키가 대입 됨.
    for key in reporting_dict:
        # 해당 딕셔너리의 value가 k 이상이면 이용 정지 대상임.
        if len(reporting_dict[key]) >= k:
            # 신고자의 문자열 id가 순회됨.
            for result in reporting_dict[key]:
                # user_dict의 해당 문자열을 키로 대입하면 가입 번호가 나옴
                i = user_dict[result]
                # answer의 해당 가입번호 원소에 1 추가.
                answer[i] += 1

    return answer


# 메인 함수를 통해 신고 결과 예시.
def main():
    # 사용자 아이디 리스트
    id_list = ["muzi", "frodo", "apeach", "neo"]
    
    # 신고 목록 - "신고자, 불량유저" 를 원소로 하는 1차원 배열.
    # 신고목록 테스트 1
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    # 신고목록 테스트 2 - 하나의 이용자가 여러 번 신고해도 하나의 신고로 간주함.
    # report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    
    # 이용 정지 기준 - k 이상 신고가 누적되면 해당 유저는 이용 정지.
    k = 2

    solution(id_list, report, k)


if __name__ == "__main__":
    main()