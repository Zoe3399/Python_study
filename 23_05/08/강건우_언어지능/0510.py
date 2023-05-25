#!/usr/bin/env python
# coding: utf-8

# 윷놀이
# 
# https://www.acmicpc.net/problem/2490
# 
# 별 찍기
# 
# 4 https://www.acmicpc.net/problem/2441
# 
# 8  https://www.acmicpc.net/problem/2445
# 
# 12  https://www.acmicpc.net/problem/2522
# 
# 20 https://www.acmicpc.net/problem/10995

# ## [윷놀이](https://www.acmicpc.net/problem/2490)

# In[9]:


#입력받을때 map함수를 사용. split함수로 띄어쓰기 구분
for i in range(3):
    lst, b, d = map(int, input().split()), 0, 0
    #for문을 돌려서 조건문을 통해 배(b:0)과 등(d:1)을 구분 후 증감
    for i in lst:
        if i==0 : b+=1
        else : d+=1
    #조건문으로 배와 등 개수를 세서 도개걸윷모(ABCDE) 출력
    print("A")if b==1 and d==3 else print("B") if b==2 and d==2 else print("C") if b==3 and d==1 else print("D") if b==4 and d==0 else print("E")


# ## [별찍기 4](https://www.acmicpc.net/problem/2441)

# In[43]:


# N을 입력받고 N의 횟수만큼 별을 출력하는 문제
n = int(input())
# for문을 돌려서 별 출력
[print(" "*i+"*"*(n-i))for i in range(n)]


# ## [별찍기 8](https://www.acmicpc.net/problem/2445)

# In[44]:


#N입력받기
n = int(input())
#상단 포문 , 하단 포문
[print("*"*i +" "*2*(n-i)+"*"*i) for i in range(1,n+1)], [print("*"*(n-j)+" "*2*j+"*"*(n-j)) for j in range(1,n)]


# ## [별찍기 12](https://www.acmicpc.net/problem/2522)

# In[45]:


#N입력받기
n = int(input())
#상하단 응용
[print(" "*(n-i)+"*"*i) for i in range(1,n+1)],[print(" "*j+"*"*(n-j)) for j in range(1,n)]


# ## [별찍기 20](https://www.acmicpc.net/problem/10995)

# In[46]:


n = int(input())
[print("* "*n if i%2==0 else " *"*n) for i in range(n)]

