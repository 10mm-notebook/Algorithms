import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
target=int(sys.stdin.readline())

numbers.sort()
cnt=0

def two_pointer(nums,target):
    global cnt
    left,right=0,len(nums)-1
    
    while left<right:
        numbers_sum=nums[left]+nums[right]
        if numbers_sum==target:
            cnt+=1
            left+=1
        elif numbers_sum<target:
            left+=1
        elif numbers_sum>target:
            right-=1
    return None

two_pointer(numbers,target)

print(cnt)