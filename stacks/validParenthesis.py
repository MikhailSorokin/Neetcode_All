class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' or char == ']' or char == '}':
                if len(stack) > 0:
                    leftParen = stack.pop()
                    if leftParen == '(' and char != ')':
                        return False
                    elif leftParen == '[' and char != ']':
                        return False
                    elif leftParen == '{' and char != '}':
                        return False
                else:
                    return False
                
        return len(stack) == 0
