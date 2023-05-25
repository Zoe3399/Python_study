# https://solved.ac/profile/playdev7
# 5598 / 카이사르 암호

# 문제
# a-z 까지의 문자에서 3칸씩 뒤로 밀어낸 암호를 카이사르 암호라고 한다. 매우 단순한 암호체계이다.
# 카이사르 암호가 주어지면, 평문으로 해독해서 출력하라.

p_key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

pw = input()

for p in pw:
    print(p_key[p_key.index(p) - 3], end="")
