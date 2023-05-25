n = int(input())
# n줄만큼 반복
for i in range(n):
    for j in range(i):
        print(' ', end= "")
    for j in range(n-i):
        print("*", end="")
    print("")
