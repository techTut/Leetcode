class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, ch in enumerate(s):
            if ch == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        stack.append(len(s))
        longest = stack[0]
        for i in range(1, len(stack)):
            longest = max(longest, stack[i] - stack[i-1] -1) 
        return longest
    
#         0123456
#         )()())
#         ()()()
        
#         [6]