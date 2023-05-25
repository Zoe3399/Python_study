# 점수입력받기
score = int(input())
# 100~ 90  = A
if 100 >= score >= 90:
    print("A")
# 89 ~ 80 = B
elif 90 > score >= 80:
    print("B")
# 79 ~ 70 = C
elif 80 > score >= 70:
    print("C")
# 69 ~ 60 = D
elif 70 > score >= 60:
    print("D")
# 나머지 F
else: print("F")