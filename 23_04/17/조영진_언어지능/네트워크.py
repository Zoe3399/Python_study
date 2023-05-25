def dfs(n, computer, com, visited):# 깊이 우선 탐색
    visited[com] = True # 방문처리
    for connect in range(n): #컴퓨터 개수만큼 진행
        if connect != com and computer[com][connect] == 1:#연결여부 확인
            if visited[connect] == False:#방문 했는지 확인 -> 안 했으면 진행
                dfs(n, computer, connect, visited)# 재귀함수로 붙어있는 '1'에 대한 방문처리


def solution(n, computers):
    answer = 0
    visited = [False] * n #컴퓨터 개수
    for num in range(n):
        if visited[num] == False:#방문 안한 컴퓨터일 시 방문 진행
            dfs(n, computers, num, visited)#깊이 우선 탐색 진행 -> 재귀함수 호출로 붙어있는 '1'에 대한 모든 곳에 방문처리
            answer += 1 #붙어있는 '1'에 방문처리 후 더 갈 곳이 없을 때 정답에 +1
    return answer