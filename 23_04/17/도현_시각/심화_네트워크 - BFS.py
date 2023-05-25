# 현재 computers 는 인접 행렬로 주어지는 상태.
# 인접 행렬 - i번 노드에 i번 노드를 포함한 전체 노드의 연결상태를 연결이면 1, 아니면 0 으로 표현하는 정방행렬.
# 이번 문제 풀이는 BFS로 풀어보고자 함.


# BFS로 문제를 풀기 위해 인접 리스트로 변환
# 인접리스트 - i번 노드에 연결된 노드 a,b,c / j번 노드에 연결된 노드 e, d 와 같이 표현하는 자료구조 표현 방식
# adjacency_list 가 기므로 보통 adj_list 로 표현함.
def matrix_to_list(adj_matrix):
    # 인접행렬의 길이를 n에 부여
    n = len(adj_matrix)

    # 인접리스트는 딕셔너리로 구현하는 것이 효율적임.
    adj_list = {}

    # 반복문을 통해 i번 노드에 연결되어 있는 j들이 담긴 딕셔너리 구조로 매핑.
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] == 1:
                if i not in adj_list:
                    adj_list[i] = [j]
                else:
                    adj_list[i] += [j]

    # 입력받은 adj_matrix를 adj_list로 반환.
    return adj_list



# BFS 알고리즘 구현
# 인자 - 인접리스트, 시작점, 방문리스트(Visited)
# 방문리스트는 노드의 길이만큼 방문하였으면 True, 아니면 False로 기록하는 전광판 같은 리스트임.
def BFS(adj_list, start, visited):

    # python은 insert와 pop으로 바로 큐 구현이 가능함.
    queue = [start]

    # 시작 지점은 당연히 방문하므로 True
    visited[start] = True

    # BFS 사이클
    # 준비물 - 인접리스트, 시작노드번호, 방문리스트
    # 시작노드를 일단 큐에 담고, 방문리스트에 시작노드는 방문하였다고 표시한다.
    # 아래 내용을 큐가 완전히 사라 질 때까지 반복한다.
    # 1. 큐에 들어있는 노드번호를 빼서 임의의 변수 v에 할당한다.
    # 2. 인접리스트의 v번 노드를 확인한다.
    # 3. 만약에 방문리스트에 False인 노드라면 큐에 노드번호를 삽입한다
    # 결과적으로 해당 시작점으로부터 트리의 BFS 탐색 결과가 visited에 담긴다.

    # 큐가 완전히 사라질 동안
    while queue:
        # 큐의 내용을 빼서 v에 대입.
        v = queue.pop()
        
        # 한 줄로 확인하기 쉽도록 end 를 활용하여 v를 출력.
        # print(v, end=' ')

        # 인접리스트의 v번 노드에 대해 탐색
        for i in adj_list[v]:
            # 만약 방문하지 않은 노드라면 큐에 해당 노드 삽입 후 visited에 해당 노드 방문하였다고 True를 표시.
            if not visited[i]:
                queue.insert(0, i)
                visited[i] = True
    
    return visited
 

def solution(n, computers):
    # matrix_to_list 를 통해 computers 인접행렬을 인접 리스트로 변환.
    # 반환된 인접리스트를 adj_list에 대입
    adj_list = matrix_to_list(computers)

    # 네트워크의 개수를 새야하므로 networks 리스트 선언.
    networks = []
    
    # n개의 컴퓨터가 있으므로 시작노드를 0부터 n까지 순차적으로 BFS 탐색.
    for i in range(n):

        # 방문리스트는 매 시작 때 마다 초기화 되어야 i에 대한 정확한 탐색 결과가 도출됨.
        visited = [False] * n
        
        # BFS 실행 결과를 network 에 대입
        network = BFS(adj_list, i, visited)
        
        # 중복값은 networks에 들어가지 않도록 적절히 추가.
        # 만약에 networks에 들어있다면 pass, 들어있지 않다면 append.
        if network in networks:
            pass
        else:
            networks.append(network)

    # 네트워크의 개수는 networks 2차원 배열의 길이가 됨.
    return len(networks)


# 실행 테스트용 main 함수
def main():
    # 1개가 나와야 맞는 경우
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

    # 2개가 나와야 맞는 경우
    # print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    
    # 3개의 네트워크가 되는 경우 - 0과 2간 구축된 네트워크, 1-0-2 네트워크, 3-2-0-1 네트워크.
    # print(solution(4, [[1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1]]))

    # 각자 두 개의 네트워크를 구축한 5개의 쌍
    # print(solution(5, [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))

    # 4개가 나와야 맞는 경우
    # print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
    
    # 5개가 나와야 하는 경우
    # print(solution(10, [[1, 1, 1, 0, 0, 0, 1, 0, 1, 0],[1, 1, 1, 0, 0, 0, 1, 0, 0, 0],[1, 1, 1, 0, 0, 0, 1, 0, 0, 0],[1, 1, 1, 0, 0, 0, 1, 0, 0, 0],[1, 1, 1, 0, 1, 1, 1, 0, 0, 0],[1, 1, 1, 0, 1, 1, 1, 1, 1, 0],[1, 1, 1, 0, 0, 0, 1, 0, 0, 0],[1, 1, 1, 0, 0, 0, 1, 0, 0, 0],[1, 1, 1, 0, 0, 0, 1, 0, 0, 0],[1, 1, 1, 0, 1, 1, 1, 1, 1, 0]]))


if __name__ == "__main__":
    main()