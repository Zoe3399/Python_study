# 다리우스 K/D/A 형식으로 입력받기
K, D, A = map(int, input().split('/'))

# K + A < D 이거나, D = 0이면 가짜
if K + A < D or D == 0:
    print("hasu")
# 아니면 진짜
else: print("gosu")


