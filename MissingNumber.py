#Missing Number
def missingNumber(nums):
    n = len(nums)
    outPut = 0
    for _ in range(0,n + 1):
        if not _ in nums:
            outPut = _
    return outPut

nums = [0,1,2,3,4,6]
print(missingNumber(nums))