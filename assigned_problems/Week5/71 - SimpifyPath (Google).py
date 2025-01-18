class Solution:
    # Daniel - Google 
    # https://leetcode.com/problems/simplify-path/description/
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/": # iterate through each char in path
            if c == "/": # evaluate if we hit a slash 
                if cur == "..": 
                    if stack: stack.pop() # go up one level
                elif cur != "" and cur != ".":
                    stack.append(cur) # record current folder or file
                cur = "" # will eat up repetitive slashes and "."
            else: 
                cur += c # build the path

        return "/" + "/".join(stack) # we want the path to start with "/"
