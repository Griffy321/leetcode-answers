class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False

        stack = []
        for val in s:
            # print(stack)
            stack.append(val)
            if val in [")", "]", "}"] and len(stack) > 1:
                lastVal = stack[-2] 
                # print(lastVal)
                if lastVal == "(" and val == ")":
                    stack.pop(-1)
                    stack.pop(-1)
                elif lastVal == "[" and val == "]":
                    stack.pop(-1)
                    stack.pop(-1)
                elif lastVal == "{" and val == "}":
                    stack.pop(-1)
                    stack.pop(-1)
                else:
                    return False
            else:
                continue
        if len(stack) > 0:
            return False
        return True
