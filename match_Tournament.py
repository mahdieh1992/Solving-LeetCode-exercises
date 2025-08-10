class Solution(object):
    def numberOfMatches(self, n):
        total = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                total += n
            else:
                total += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return total            

n = int(input())
solution = Solution()
result = solution.numberOfMatches(n)        
print(result)