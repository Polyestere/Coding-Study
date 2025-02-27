#백준 3273 두수의 합

n = int(input())# 수열의 크기
nums = list(map(int,input().split())) #수열
x= int(input())#자연수 x
nums.sort()

point_i, point_j = 0,n-1
ans = 0

while point_i < point_j:
    tmp = nums[point_i] + nums[point_j]
    if tmp == x:
        ans+=1
        point_j-=1
        point_i+=1
    elif tmp > x:
        point_j -=1
    else:
        point_i +=1



print(ans)
