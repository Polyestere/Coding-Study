#백준 2805 나무 자르기

def check_length(h):
    return sum([i - h for i in height if i > h])
def cutting_tree(low, high, target):
    tmp = check_length(target)

    if low > high:
        return target
    if M == tmp:
        return target
    if tmp >= M:
        low = target+1
    else:
        high = target -1
    target = (low+high)//2
    return cutting_tree(low,high,target)

N, M = map(int, input().split())
height = list(map(int,input().split()))
print(cutting_tree(0,max(height),max(height)//2))
