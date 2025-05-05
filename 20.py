class Solution(object):
    def isValid(self, s):
        stack = []

        closeCh = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack[-1] != closeCh[c]:
                    return False
                stack.pop()

        return not stack
