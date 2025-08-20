class Solution(object):
    def isValid(self, s):
        listString = ['()','[]','{}']
        listS = list(s)
        ls = len(listS)
        i = 0
        while i < ls - 1:
            m = listS[i] + listS[i + 1]
            if m in listString:
                del listS[i:i + 2]
                i = 0 
                ls = len(listS)
            else:
                i += 1
        if not listS:
            return True
        else:
            return False

s = input().strip()
sol = Solution()
result = sol.isValid(s)
print(result)