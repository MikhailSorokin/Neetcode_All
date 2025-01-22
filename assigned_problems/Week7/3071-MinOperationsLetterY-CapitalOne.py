class Solution:
    # Rodrigo - https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/?envType=company&envId=capital-one&favoriteSlug=capital-one-six-months
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        # O(N^2) Time | O(1) Space
        def get_operation_count(grid, y, not_y):
            n = len(grid)
            operations = 0
            for i in range(n):
                for j in range(n):
                    # Check if the cell belongs to the "Y"
                    if (i <= n // 2 and (i == j or i + j == n - 1)) \
                    or (i > n // 2 and j == n // 2):
                        if grid[i][j] != y:
                            operations += 1
                    else:
                        if grid[i][j] != not_y:
                            operations += 1
            return operations
            
        n = len(grid)
        min_operations = float('inf')
        
        # Iterate through all possible Y and non-Y values
        for y in range(3):
            for not_y in range(3):
                if y != not_y:
                    min_operations = min(min_operations, get_operation_count(grid, y, not_y))
        
        return min_operations

class Solution2:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        # O(N^2) Time | O(1) Space
        n  = len(grid)   
        n2 = n//2

        y = ((grid[i][i], grid[n-i-1][n2],          #  <-- 1)
                grid[i][n-i-1]) for i in range(n2)) # 

        ctr1 = Counter(chain(*y))                   #  <-- 2)
        ctr1[grid[n2][n2]]+= 1                      #

        ctr2 = Counter(chain(*grid)) - ctr1         #  <-- 3)

        return n*n - max(                           #  <-- 4)
                ctr1[0]+ctr2[1], ctr1[1]+ctr2[0],
                ctr1[0]+ctr2[2], ctr1[2]+ctr2[0], 
                ctr1[1]+ctr2[2], ctr1[2]+ctr2[1])
