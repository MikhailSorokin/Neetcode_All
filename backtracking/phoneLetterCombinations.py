class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def dfs(i, part):
            if i == len(digits):
                res.append(part)
                return

            for j in range(0, len(lists[i])):
                dfs(i + 1, part + lists[i][j])

        # Map a digit to a range EX: ['a' - 'c']
        lists = []
        base_chars = ord('a')
        for digit in digits:
            num = int(digit)
            if num == 7:  # Special case: 'pqrs' (4 letters)
                start_idx = (num - 2) * 3
                cList = [chr(base_chars + start_idx + j) for j in range(4)]
            elif num == 8:  # Special case: 'tuv' (3 letters, after 'pqrs')
                start_idx = (num - 2) * 3 + 1  # Adjusted due to 'pqrs'
                cList = [chr(base_chars + start_idx + j) for j in range(3)]
            elif num == 9:  # Special case: 'wxyz' (4 letters, after 'tuv')
                start_idx = (num - 2) * 3 + 1  # Adjusted due to 'pqrs' and 'tuv'
                cList = [chr(base_chars + start_idx + j) for j in range(4)]
            else:  # Digits 2-6 (normal 3-letter mapping)
                start_idx = (num - 2) * 3
                cList = [chr(base_chars + start_idx + j) for j in range(3)]

            lists.append(cList)

        res = []
        dfs(0, "")
        return res
                
