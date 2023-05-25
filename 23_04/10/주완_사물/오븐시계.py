# t = 시, m = 분, n = 입력값
t, m = map(int, input().split())
n = int(input())
timer = m+n

# timer >= 60 일 경우 m은 나머지만큼 증가
# timer >= 60 일 경우 t는 (t + 몫)만큼 증가
# t가 무한히 증가할 수는 없으므로 24이상일 경우 24로 나눠준 나머지 값을 할당
if timer >= 60 :
    t = t + timer // 60
    m = timer % 60
    if t >= 24: 
        t = t % 24

# timer가 60이하일 경우 m에 할당
elif timer < 60 :
    m = m + n
    
print(t, m)