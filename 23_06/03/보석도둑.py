#https://www.acmicpc.net/problem/1202
import sys
import heapq

n, k = map(int,sys.stdin.readline().split())
heap = []

# n만큼 반복 / 원소를 추가할 heap 리스트에 , 공백을 기준으로 입력받은 리스트를 넘긴다
for _ in range(n): heapq.heappush(heap, list(map(int, sys.stdin.readline().split())))
    #print(heap)
    # 1 65 >> [[1, 65]]
    # 5 23 >> [[1, 65], [5, 23]]
    # 2 99 >> [[1, 65], [5, 23], [2, 99]]
    
c = [int(sys.stdin.readline()) for x in range(k)]
# 무게가 작은 가방부터 보석을 넣기위해 오름차순 정렬
c.sort() # [2, 10]

# 현재 가방보다 작은 모든 보석들을 넣을 곳
bag = []

# 최대 가격
max_value = 0

for i in c:
    # 가방의 무게보다 작거나 같은 보석이 있는지 확인
    # heap[0][0]보다 크거나 같은 i 사이에 값이 heap 안에 있으면 true
    # 이때, heap[0][0]보다 크거나 같은 i 사이에 값중 heap 안에 있는 값을 하나씩 꺼내어 확인한다.
    while heap and i >= heap[0][0]: 
        heapq.heappush(bag, -heapq.heappop(heap)[1]) # 최대힙
        # 가방에 담을 수 있는 보석중 최대 가격순으로 bag에 넣는다.
        '''
        print(bag)
        [-65]
        [-99, -65]
        [-65, -23]
    
        '''

    # bag에 넣을 수 있는 보석이 있는 경우
    if bag: 
        # print(bag) >> [-99, -65] [-65, -23] << 최대힙의 부호는 음수이기에 -로 연산하여 양수를 만든다.
        max_value -= heapq.heappop(bag) #리스트 bag의 가장 작은 원소를 삭제 후 값 리턴
        # 현재 최대 가격인 보석을 카운트
    elif not heap: break  # 남은 보석이 없는 경우 끝낸다.

print(max_value) # 164 (99 + 65)

'''
        heappush
    heapq 모듈의 heappush() 함수를 이용하여, 힙의 원소를 추가 할 수있다.
    첫번째 인자는 원소를 추가할 대상 list 이며, 두번째 인자는 추가할 원소를 넘긴다.
    heappush(원소를 추가할 대상 list , 추가할 원소)
    내부적으로 이진 트리에 원소를 추가하는 heapush() 함수는 0(log(n))의 시간복잡도를 가짐
    

        heappop
    원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후 그 값을 리턴

'''
