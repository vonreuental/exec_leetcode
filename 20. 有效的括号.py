class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        if s == '':
            return True
        dict = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in dict.values():
                left.append(i)
            if i in dict:
                if len(left) == 0:
                    return False
                if left.pop() != dict[i]:
                    return False
        return True if len(left) == 0 else False


a = Solution()
print(a.isValid(']'))