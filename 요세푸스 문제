#백준 1158 요세푸스 문제

N, K = map(int,input().split())# N:사람 수 K:제거할 사람 번호
people = list((range(1,N+1)))#사람 리스트
yosepuse = []#요세푸스 리스트

num = 0

while people:
    num = (num + K -1) % len(people)
    deleted = people.pop(num)  # 제거될 사람을 리스트에서 삭제
    yosepuse.append(deleted)  # 요세푸스 순열 리스트에 추가

print('<'+', '.join(map(str,yosepuse))+'>')
