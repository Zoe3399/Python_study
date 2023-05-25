#사칙연산 https://www.acmicpc.net/problem/10869
A, B = map(int, input().split()) #입력
print(A+B); print(A-B); print(A*B); print(int(A/B)); print(A%B)#출력

#나머지 https://www.acmicpc.net/problem/10430
A, B, C= map(int, input().split()); print((A+B)%C)#입력 
print(((A%C) + (B%C))%C); print((A*B)%C); print(((A%C)* (B%C))%C)#출력

#초콜릿 자르기https://www.acmicpc.net/problem/2163
N, M = map(int, input().split()) #입력
print(N*M-1)#출력

#인공지능 오븐 시계 https://www.acmicpc.net/problem/2525
a, b=map(int, input().split()); c=int(input()) #입력
while(c>=60): a+=1; c-=60; #while문
b=b+c
while(b>=60): a+=1; b-=60; #while문
if a >= 24: a-=24; #조건문 돌리기
print(str(a)+" "+str(b)) #출력