class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                for i in tmp:
                    stack.append(i)
        return "".join(e for e in stack)

test = Solution()
print(test.reverseParentheses("(ed(et(oc))el)"))