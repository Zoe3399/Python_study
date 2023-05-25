#알파벳 소문자로만 이루어진 단어 받기
word = input()
r_word = word[::-1] # 단어 반대로 뒤집기

# 입력받은 단어와 뒤집은 단어 같은지 확인
if word == r_word: print("1")
else: print("0")