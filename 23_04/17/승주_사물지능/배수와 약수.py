while True:
    a, b = map(int, input().split()) #a, b 값 공백으로 입력 받기
    
    if a == 0 or b == 0: # a 또는 b 가 0일때 종료
        break
    
    #첫 번째 숫자가 두 번째 숫자의 배수일때
    if a % b == 0:
        print("multiple")
    # 첫 번째 숫자가 두 번째 숫자의 약수일때
    elif b % a == 0:
        print("factor")
    # 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아닐때
    else:
        print("neither")