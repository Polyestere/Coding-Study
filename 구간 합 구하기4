#백준11659 구간 합 구하기4

N,M = map(int,input().split())
nums = list(map(int,input().split()))

acc = [0]
for num in nums:
    acc.append(acc[-1] + num)

for times in range(M):
    i,j = map(int,input().split())
    print(acc[j]-acc[i-1])

