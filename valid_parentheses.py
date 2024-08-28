class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c in '({[':  # if c is an opening bracket
                stack.append(c)  # push to end of stack
            else:  # if not an opening bracket and stack is not empty
                if not stack or \
                   (c == ')' and stack[-1] != '(') or \
                   (c == '}' and stack[-1] != '{') or \
                   (c == ']' and stack[-1] != '['):  # checks if most recent opening bracket matches closing
                    return False  # return false if stack is empty or brackets don't match
                stack.pop()  # otherwise, pop or remove the last bracket from stack

        return not stack  # if stack is empty, all opening brackets match
