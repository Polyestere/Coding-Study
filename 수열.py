#백준 2599 수열

N,K = map(int,input().split())#온도 측정 전체 날짜수, 연속적인 날짜 수
temp = list(map(int,input().split()))# 전체 온도 리스트
ans_list = []
ans = sum(temp[:K])
ans_list.append(ans)
for i in range(N-K):
   ans += temp[i+K] - temp[i]
   ans_list.append(ans)

print(max(ans_list))
