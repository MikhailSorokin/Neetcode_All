class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        total = m + n
        half = (m + n) // 2

        if n > m:
            nums1, nums2 = nums2, nums1
          
        n = len(nums1)
        m = len(nums2)
        total = m + n
        half = (m + n) // 2


        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            print("i: ", i, " and j: ", j)

            Aleft = nums1[i] if i >= 0 else float("-infinity")
            Aright = nums1[i + 1] if (i + 1) < n else float("infinity")
            Bleft = nums2[j] if j >= 0 else float("-infinity")
            Bright = nums2[j + 1] if (j + 1) < m else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1