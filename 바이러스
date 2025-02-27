#백준 2606 바이러스

#인접 리스트 (바이러스 문제)
V = int(input())
E = int(input())

adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    x,y = map(int,input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

locate = [1]#스택
#복잡한 문제는 방문지를 집합구조로 설정해야함(이 문제는 간단한 문제라 리스트)
visited = set([1])
while locate:
    current = locate.pop()
    for next in adj_list[current]:
        if next not in visited:
            locate.append(next)
            visited.add(next)
        
print(len(visited)-1)

