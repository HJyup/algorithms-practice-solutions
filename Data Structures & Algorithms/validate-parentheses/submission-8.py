class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        match = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for ch in s:
            if stack and ch in match and stack[-1] == match[ch]:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0
