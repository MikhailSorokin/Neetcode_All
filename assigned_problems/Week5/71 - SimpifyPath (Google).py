class Solution:
    # Daniel - Google 
    # https://leetcode.com/problems/simplify-path/description/
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr_dir = ""

        for c in path + "/": # iterate through each char in path
            if c == "/": # evaluate if we hit a slash 
                if curr_dir == "..": 
                    if stack: stack.pop() # go up one level to parent directory
                elif curr_dir != "" and curr_dir != ".": # if current directory non-trivial
                    stack.append(curr_dir) # record current folder or file
                curr_dir = "" # will eat up repetitive slashes and single periods in curr_dir
            else: 
                curr_dir += c # build the path

        return "/" + "/".join(stack) # we want the path to start with "/"

        # # example 5
        # stack = []
        # curr_dir = "..."

        # stack = ["..."]
        # curr_dir = "a"

        # stack = ["...", "a"]
        # curr_dir = ".."

        # stack = ["..."]
        # curr_dir = "b"

        # stack = ["...", "b"]
        # curr_dir = "c"

        # stack = ["...", "b", "c"]
        # curr_dir = ".."

        # stack = ["...", "b"]
        # curr_dir = "d"

        # stack = ["...", "b", "d"]
        # curr_dir = "."

        # # join
        # "/.../b/d/"
