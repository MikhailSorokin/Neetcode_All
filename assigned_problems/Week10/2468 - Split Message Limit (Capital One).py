class Solution:
    # Rodrigo
    # https://leetcode.com/problems/split-message-based-on-limit/?envType=company&envId=capital-one&favoriteSlug=capital-one-all
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def mysum(parts):
            if parts < 10: return parts
            if parts < 100: return 2*(parts-9) + mysum(9)
            if parts < 1000: return 3*(parts-99) + mysum(99)
            if parts < 10000: return 4*(parts-999)+mysum(999)
            return 5 + mysum(9999)
        for parts in range(1, len(message)+1):
            #O(n) - bad
            # totalLen = len(message) + sum(len('<{}/{}>'.format(i,parts)) for i in range(1,parts+1))
            #O(1) - good
            totalLen = len(message) + 3*parts + mysum(parts) + parts * len(str(parts))
            if ceil(totalLen / limit) == parts:
                #Run simulation
                ret = []
                ind = 0
                for i in range(1, parts+1):
                    counter = '<{}/{}>'.format(i,parts)
                    j = ind + limit - len(counter)
                    ret.append(message[ind:j]+counter)
                    ind = j
                return ret
        return []
