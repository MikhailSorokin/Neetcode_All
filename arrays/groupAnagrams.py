class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Go through each string and generate a code based on alphabet
        alphabetCodeMap = {defaultdict(list)}
        for string in strs:
            alphabetCode = [0] * 26
            # Generate code from str
            for c in string:
                alphabetCode[ord(c) - ord('a')] += 1

            alphabetCodeMap[tuple(alphabetCode)].append(string)

        return list(alphabetCodeMap.values())
