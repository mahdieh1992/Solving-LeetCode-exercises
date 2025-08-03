class Solution(object):
    def twoSum(self, nums, target):
        indics = []
        for i in range(len(nums) -1):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    indics.append(i)
                    indics.append(j)
        return indics


nums = [3,2,3]
target = 6
solution = Solution()
result = solution.twoSum(nums,target)
print(result)