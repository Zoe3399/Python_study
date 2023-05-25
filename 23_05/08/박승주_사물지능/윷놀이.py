# list에 1이 몇개 존재하는지 확인하기
for i in range(3):
    # 공백으로 입력 받기
    a = list(map(int, input().split()))
    back_count = 0
    for i in a:
        if i == 1:
            back_count +=1
    if back_count == 3: print("A")
    elif back_count == 2 : print("B")
    elif back_count == 1 : print("C")
    elif back_count == 0 : print("D")
    elif back_count == 4 : print("E")

    
