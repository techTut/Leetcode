class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(" : ")",
                  "[" : "]",
                  "{" : "}",
                  }
                  
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                if not stack or mapping[stack.pop()] != ch:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    for testCase in ["()", "(){}[]", "(]"]:
        print('Output for input "{0}" is : "{1}"'.format(testCase, s.isValid(testCase)))