# 2. 한타 안 함? (https://www.acmicpc.net/problem/20499)

# K D A "/"를 기준으로 입력. K + A < D Or D ==0 이면 가짜, 나머지 진짜.

K, D, A = map(int,input().split("/"))

if (K + A < D) or D == 0 :
    print("hasu")
else:
    print("gosu")
