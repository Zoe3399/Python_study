# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

    #1. 첫 번째 숫자가 두 번째 숫자의 약수이다. = "factor"
    #2. 번째 숫자가 두 번째 숫자의 배수이다. = "multiple"
    #3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다. "neither"

# 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다.
# 마지막 줄에는 0이 2개 주어진다. ?????     -----> While break 로 마지막 00 입력 전까지 계속 입력받는다.
# 두 수가 같은 경우는 없다.

while True :
    a , b = map(int,input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0 :
        print("factor")
    elif a % b == 0 :
        print("multiple")
    else:
        print("neither")