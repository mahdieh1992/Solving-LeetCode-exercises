class Solution(object):
    def removeDuplicates(self,nums):
        index_of_nums = []
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[j] != nums[i]:
                    break
                else:
                    index_of_nums.append(j)
        for _ in sorted(set(index_of_nums),reverse=True):
              nums.pop(_)
        return len(nums)
    
nums = [0,0,1,1,1,2,2,3,3,4]    
n = 3 * (10 ** 4) 
len_nums = len(nums) 
class_Sol = Solution()
result = class_Sol.removeDuplicates(nums)
if 1 <= len_nums <= n:
    print(result)
else:
    print("Numbers is not valid it must in range")    