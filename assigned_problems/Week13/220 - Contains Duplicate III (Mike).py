class Solution:
    # Palantir
    # https://leetcode.com/problems/contains-duplicate-iii/description/?envType=company&envId=palantir-technologies&favoriteSlug=palantir-technologies-all

    # Get the ID of the bucket from element value x and bucket width w
    # Division '/' in Python with '//' performs floor division, which is necessary for correct bucketing.
    def getID(self, x, w):
        return (
            x // w
        )  # Floor division to handle both positive and negative integers correctly

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        buckets = {}
        w = t + 1  # Increment by 1 to handle the range correctly
        for i in range(len(nums)):
            bucket = self.getID(nums[i], w)
            # Check if current bucket is empty, each bucket may contain at most one element
            if bucket in buckets:
                return True
            # Check the neighbor buckets for almost duplicates
            if bucket - 1 in buckets and abs(nums[i] - buckets[bucket - 1]) < w:
                return True
            if bucket + 1 in buckets and abs(nums[i] - buckets[bucket + 1]) < w:
                return True
            # Now bucket is empty and no almost duplicates in neighbor buckets
            buckets[bucket] = nums[i]
            if i >= k:
                del buckets[self.getID(nums[i - k], w)]
        return False