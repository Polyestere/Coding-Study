#### 백준 1715 카드 정렬하기

import heapq

# 카드 묶음의 개수
N = int(input())

# 각 카드 묶음의 크기를 입력받아 최소 힙에 추가
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

total = 0

# 카드 묶음이 하나 남을 때까지 반복
while len(heap) > 1:
    # 가장 작은 두 묶음을 꺼내어 합침
    hap = heapq.heappop(heap) + heapq.heappop(heap)
    total += hap
    # 합친 묶음을 다시 힙에 삽입
    heapq.heappush(heap, hap)

# 최소 비교 횟수 출력
print(total)
