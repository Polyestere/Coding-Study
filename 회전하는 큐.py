#백준 1021 회전하는 큐

#원형 큐?
from collections import deque

N,M = map(int,input().split())# N:큐의크기, M:뽑아내려고 하는 수의 개수
numbers = list(map(int,input().split()))#뽑아내려하는 숫자

queue = deque((range(1,N+1)))#큐
total = 0 #필요한 2, 3번 연산의 횟수 중 최솟값 저장

for target in numbers:
    idx = queue.index(target)# 뽑아내려하는 숫자의 큐에서의 위치

    left = idx #왼쪽으로 움직였을 때 횟수(2번)
    right = len(queue)- idx #오른쪽으로 움직였을 때 횟수 (3번)
    total += min(left, right)# 2,3번연산 중 최솟값 

    queue.rotate(-left)#왼쪽으로 이동
                      #target으로 향하는 연산 횟수는 이미 계산 되었으므로 어떤 방향으로 회전하든 상관 없음
    queue.popleft()#target 제거

print(total)
