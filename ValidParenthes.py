class Solution(object):
    def isValid(self, s):
        listString = {'(' : ')', '{' : '}' , '[':']'}
        s = s.strip()
        result = []
        for char in s:
            result.append(char)
            if len(result) >= 2 and result[-2] in listString and listString[result[-2]] == result[-1]:
                result.pop()
                result.pop()
        if result:
            return False
        return True
      
s = input().strip()
sol = Solution()
result = sol.isValid(s)
print(result)