class Solution:
    #Rodrigo - Capital One
    #https://leetcode.com/problems/block-placement-queries/?envType=company&envId=capital-one&favoriteSlug=capital-one-thirty-days
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Create a SortedList to maintain sorted order of numbers dynamically
        sl = SortedList()
        n = min(5 * 10 ** 4, len(queries) * 3)  # Define an upper limit based on query size
        sl.add(0)  # Add initial boundary
        sl.add(n)  # Add upper boundary
        
        ans = []  # List to store results of queries
        
        # Process the queries
        for q in queries:
            if q[0] == 1:  # If query is of type 1, add the number to the SortedList
                x = q[1]
                sl.add(x)
        
        # Create another SortedList to track gaps between elements
        gap = SortedList()
        gap.add((0, 0))  # Add a placeholder initial gap
        curr = 0  # Variable to track the largest gap seen so far
        
        # Calculate gaps between consecutive elements in the SortedList
        for x, y in pairwise(sl):
            if (g := y - x) > curr:  # Update gaps if the new gap is larger
                gap.add((y, g))
                curr = g
        
        # Process queries in reverse order to handle removal
        for q in reversed(queries):
            if q[0] == 1:  # If query is of type 1, remove the number from the SortedList
                x = q[1]
                index = sl.index(x)  # Find index of the number
                after = sl[index + 1]  # Get the next element
                before = sl[index - 1]  # Get the previous element
                sl.remove(x)  # Remove the number from the list
                g = after - before  # Calculate the new gap
                index = gap.bisect_left((x, 0))  # Find position in the gap list
                
                # Remove gaps smaller than the new gap
                while index < len(gap) and gap[index][1] <= g:
                    gap.pop(index)
                
                # Add the new gap if it's larger
                if gap[index - 1][1] < g:
                    gap.add((after, g))
            else:
                # If query is of type 2, perform the range and size check
                _, x, sz = q
                index = sl.bisect_right(x)  # Find the insertion point for x
                before = sl[index - 1]  # Get the previous element
                
                # Find the largest gap before x and check if it meets the size requirement
                index = gap.bisect_right((before, math.inf)) - 1
                ans.append((x - before) >= sz or gap[index][1] >= sz)
        
        ans.reverse()  # Reverse the results to match query order
        return ans
