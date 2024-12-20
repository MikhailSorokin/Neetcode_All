class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1=> 1, 2=> 2, 3 => 3

        # 1, 2, 3, 4, 5, 6
        # 1  2  3  0  0  0

        # Go from 6 to 1 and then get the top k non-0

        buckets = {}
        # For each digit, create a bucket to end up with a list
        for i in range(1, len(nums) + 1):
            buckets[i] = []
        
        frequentMap = {}
        for i in range(0, len(nums)):
            if nums[i] not in frequentMap:
                frequentMap[nums[i]] = 1
            frequentMap[nums[i]] += 1

        for key,value in frequentMap.items():
            buckets[value - 1].append(key)

        print(buckets)

        results = []
        ind = len(nums)
        while k > 0:
            print(buckets[ind])
            if len(buckets[ind]) > 0:
                results.append(buckets[ind])
                k -= len(buckets[ind])

            ind -= 1

        # Flatten using Nested Loops
        flattened_list = []
        for sublist in results:
            for item in sublist:
                flattened_list.append(item)


        return flattened_list


            
            