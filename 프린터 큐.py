#백준 1966 프린터 큐

from collections import deque


for i in range(int(input())):#테스트 케이스만큼 반복
    N, M = map(int,input().split())# 문서의 개수(큐의 길이), 궁금한 문서의 인덱스
    importance = list(map(int,input().split()))#모든 문서의 중요도
    queue = deque([(idx, note) for idx, note in enumerate(importance)])#문서의 위치와 중요도를 큐로 생성
    #enumertate 함수는 리스트의 요소의 인덱스를 추출함. 
    #idx는 인덱스 note는 문서의 중요도로 이차원 배열로서 큐에 기록됨 
    count = 0# 문서의 순서

    while queue:# 큐가 빌 때까지 반복
        current = queue.popleft()
        
        if any(current[1] < high[1] for high in queue): # 현문서보다 중요도가 높은 문서가 있는지 탐색
            queue.append(current)# 있다면 맨 뒤로 옮기기
        else:
            count += 1 #중요도가 제일 높거나 높은 것과 같다면 인쇄
            if current[0] == M: #만약 문서의 인덱스가 궁금한 문서와 같다면 문서의 순서 기록
                print(count)
                break
