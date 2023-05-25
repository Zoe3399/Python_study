# 3. 팰린드롬인지 확인하기 (https://www.acmicpc.net/problem/10988)
# 앞으로나 뒤로나 똑같은 단어 level, noon, etc....
# 강건우님 식 참고 -> #문자열 뒤집기 = y=x[::-1]

Check_w = input()
Check_w_b = Check_w[::-1]

if Check_w == Check_w_b:
   print("1")
else:
   print("0")