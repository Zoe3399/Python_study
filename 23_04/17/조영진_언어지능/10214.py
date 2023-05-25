for _ in range(int(input())):
    ko = yon = 0
    for _ in range(9):
        a, b = map(int, input().split())
        ko += b
        yon += a
    if yon < ko:
        print("Korea")
    elif yon > ko:
        print("Yonsei")
    else:
        print("Draw")