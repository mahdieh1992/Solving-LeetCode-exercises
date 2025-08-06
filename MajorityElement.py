class Solution(object):
    def majorityElement(self, nums):
        numbers = {}
        for num in nums:
            if num in numbers:
                numbers[num] = numbers[num] +  1
            else:
                numbers[num] = 1
        get_key = max(numbers,key=numbers.get)
        return get_key

nums = [3,2,3]        
solution = Solution()
result = solution.majorityElement(nums)
print(result)
