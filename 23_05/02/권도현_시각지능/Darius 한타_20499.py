# https://solved.ac/profile/playdev7
# 인공지능사관학교 Python Study 기본문제
# 20499 - Darius 님 한타 안 함?

# 문제 - K + A < D 또는 D가 0이면 "가짜" 아니면 "진짜" 를 출력하는 프로그램 작성.
# 입력 - 슬래시 기호를 기준으로 K/D/A 가 입력된다.
# 출력 - 진짜 이면 "gosu" 아니면 "hasu" 를 출력한다.

# 풀이 시작

# 슬래시 기호를 기준으로 입력받아 K, D, A 변수에 매핑
K, D, A = map(int, input().split("/"))

# 연산 수행
if K + A < D or D == 0:
    print("hasu")
else:
    print("gosu")

# 참 쉽죠?