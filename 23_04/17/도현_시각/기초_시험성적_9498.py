# https://solved.ac/profile/playdev7
# 문제 - 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램

# 정수로 입력받는다.
score = int(input())

# 90점 이상이면 "A"를 출력한다.
if score >= 90:
    print("A")

# 위에 해당하지 않고 80점 이상이면 "B"를 출력한다. - elif.
elif score >= 80:
    print("B")
    
# 위에 해당하지 않고 70점 이상이면 "C"를 출력한다.
elif score >= 70:
    print("C")
    
# 여전히 위에 해당하지 않고 60점 이상이면 "D"를 출력한다.
elif score >= 60:
    print("D")
    
# 이렇게 열심히 적었는데도 조건에 해당하지 않으면 "F"를 출력한다. - else.
else:
    print("F")