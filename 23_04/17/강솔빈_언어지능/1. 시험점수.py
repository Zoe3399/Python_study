#시험 점수 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F.
# 정수는 0 < S <= 100
#

Score = int(input())

if 90 <= Score <= 100:
    print("A")
elif 80 <= Score <= 89:
    print("B")
elif 70 <= Score <= 79:
    print("C")
elif 60 <= Score <= 69:
    pritn("D")
else:
    print("F")