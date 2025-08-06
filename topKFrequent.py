class Solution(object):
    def topKFrequent(self, nums, k):
        count_nums = {}
        for num in nums:
            if num in count_nums:
                count_nums[num] += 1
            else:
                count_nums[num] = 1

        # مرتب‌سازی با در نظر گرفتن کلید در صورت مساوی بودن مقدار
        sorted_items = sorted(count_nums.items(), key=lambda x: (-x[1], x[0]))
        output = [key for key, val in sorted_items[:k]]
        return output

# تست:
nums = [4,1,-1,2,-1,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))  # خروجی: [-1, 2]
