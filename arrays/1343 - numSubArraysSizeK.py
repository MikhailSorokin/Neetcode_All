class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        i = 0
        n = len(arr)

        runningSum = sum(arr[:k])

        while i < n:
            # Get average through k elements
            averageElems = 0
            stepSize = i + k
            if stepSize <= n:
                averageElems = runningSum // k
                # Check average >= threshold
                res += 1 if averageElems >= threshold else 0
            runningSum -= arr[i]
            i += 1
            if i + k <= n:
                runningSum += arr[i + k - 1]

        return res