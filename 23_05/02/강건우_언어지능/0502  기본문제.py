#!/usr/bin/env python
# coding: utf-8

# # [ 밥 알 갯수]
# https://www.acmicpc.net/problem/27294
# 
# 
# # [ 한타 ]
# https://www.acmicpc.net/problem/20499
# 
# 
# # [평균은 넘겠지]
# https://www.acmicpc.net/problem/4344
# 

# In[56]:


# 밥알개수 문제
t, s = input().split()
# 술하고 같이 먹을 경우
if int(s) == 1:
    print(280)
# 술없이 초밥만 먹을 경우 점심만 320개
else:
    if int(t) <= 11 : print(280) #아침
    elif int(t) >= 12 and int(t) <= 16 : print(320) #점심
    else : print(280) #저녁


# In[55]:


# 한타 문제
k,d,a = map(int, input().split("/"))
# 계산식(true가 뜨면 hasu false가 뜨면 gosu)
if k+a<d or d == 0 : print("hasu")
else : print("gosu")


# In[43]:


#평균은 넘겠지 문제
c = int(input()) #테스트 케이스의 수
for i in range(c):
    lst = list(map(int, input().split())) #학생의 수와 성적값
    avg, cnt = sum(lst[1:])/lst[0], 0 #평균값 구하는 식과 평균 이상의 학생 수를 세는 변수
    for i in lst[1:] : 
        if avg < i: cnt += 1 #평균을 넘는 학생수를 cnt변수에 저장
    print(f"{cnt/lst[0]*100:.3f}%") #소수점 세째자리까지 출력

