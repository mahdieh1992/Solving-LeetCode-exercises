class Solution(object):
    def moveZeroes(self, nums):   
        index_zero = []     
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                index_zero.append(i)
        for _ in sorted(index_zero,reverse=True):
            nums.pop(_)
        return nums

nums = [0,0,1]    
instance = Solution()
result = instance.moveZeroes(nums)
print(result)




