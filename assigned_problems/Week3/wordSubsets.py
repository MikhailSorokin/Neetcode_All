class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count2Map = defaultdict(int)
        for word in words2:
            frequencies = Counter(word)
            for char, count in frequencies.items():
                count2Map[char] = max(count2Map[char], count)

        res = []

        for word in words1:
            flag = True
            frequencies = Counter(word)
            for char, count in count2Map.items():
                if frequencies[char] < count:
                    flag = False
                    break

            if flag:
                res.append(word)

        return res
                


        