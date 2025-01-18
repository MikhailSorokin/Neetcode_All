class Solution:
    # Rodrigo - Capital One
    # https://leetcode.com/problems/count-alternating-subarrays/?envType=company&envId=capital-one&favoriteSlug=capital-one-six-months
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
	    #O(n^3) time | O(1) space
        n = len(nums)
        count = 0
        
        # Iterate through all possible subarrays
        for i in range(n):
            for j in range(i, n):
                # Check if the subarray nums[i:j+1] is alternating
                is_alternating = True
                for k in range(i, j):
                    if nums[k] == nums[k + 1]:
                        is_alternating = False
                        break
                if is_alternating:
                    count += 1  # Increment if alternating
        
        return count

# Optimal
class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        # O(n) time | O(1) space
        n = len(nums)
        count = 0
        #valid_subarrays = []  # List to store all valid subarrays
        length = 0  # Length of the current alternating subarray

        #valid_subarrays.append([nums[0]])
        for i in range(1, n):
            #valid_subarrays.append([nums[i]])
            if nums[i] != nums[i - 1]:  # Check if the current pair alternates
                length += 1  # Extend the alternating sequence
                count += length  # Add all subarrays ending at the current index
                
                # Add all subarrays ending at the current index to valid_subarrays
                #for start in range(i - length, i):
                #    valid_subarrays.append(nums[start:i + 1])
            
            else:
                length = 0  # Reset the length for non-alternating pair
            
        # Print all valid subarrays
        #print("Valid subarrays:", valid_subarrays)
        
        # Return count plus the number of individual elements (n)
        return count + n

