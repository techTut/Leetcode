class Solution:
    def generateParenthesis(self, n: int):
            result = []
            self.generateHelper(0, 0, "", n , result)
            return result
        
    def generateHelper(self, openBrackets, closedBrackets, parens, n, result):
            if openBrackets == n and closedBrackets == n:
                result.append(parens)
            else:
                if openBrackets < n:
                    self.generateHelper(openBrackets + 1, closedBrackets, parens + "(", n , result)
                if closedBrackets < openBrackets:
                    self.generateHelper(openBrackets, closedBrackets + 1, parens + ")", n , result)
         
        # queue = deque()
        # queue.append((0, 0, ""))
        # valids = []
        # while queue:
        #     openBrackets, closedBrackets, parens = queue.popleft()
        #     if openBrackets == n and closedBrackets == n:
        #         valids.append(parens)
        #     else:
        #         if openBrackets < n:
        #             queue.append((openBrackets + 1, closedBrackets, parens + "("))
        #         if closedBrackets < openBrackets:
        #             queue.append((openBrackets , closedBrackets + 1, parens + ")"))
        # return valids

if __name__ == "__main__":
    s = Solution()
    for testCase in [1, 3, 4, 5]:
        print('Output for input "{0}" is : "{1}"'.format(testCase, s.generateParenthesis(testCase)))
