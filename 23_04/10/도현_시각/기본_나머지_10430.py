# https://solved.ac/profile/playdev7

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# a, b, c 입력받기 - split() 메소드는 두 개 "이상" 입력받을 수 있다.
a, b, c = input().split()

# 연산을 위해 a, b, c 변수를 정수형으로 변환.
a, b, c = int(a), int(b), int(c)

# 첫째 줄에 (A+B)%C 출력
print((a+b)%c)

# 둘째 줄에 ((A%C) + (B%C))%C 출력
print(((a%c) + (b%c))%c)

# 셋째 줄에 (A×B)%C 출력
print((a*b)%c)

# 넷째 줄에 ((A%C) × (B%C))%C를 출력
print(((a%c) * (b%c))%c)