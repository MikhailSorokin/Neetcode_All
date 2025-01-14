class Codec:
    def encode(self, strs: List[str]) -> str:
        # ["neet", "code", "love", "you"] -> "4#neet4#code4#love3#you"
        strBuilder = ""
        for string in strs:
            strBuilder += str(len(string)) + "#" + string
        return strBuilder
        

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        # ["4#neet4#code4#love3#you"] -> ["neet", "code", "love", "you"]
        lst = []
        numStr = ""
        j = 0
        num = -1
        for idx, char in enumerate(s):
            # Extract number until #
            if num == -1:
                if char != "#":
                    numStr += char
                    continue
                elif char == "#":
                    num = int(numStr)
                    if num == 0:
                        lst.append("")
                        num = -1
                    numStr = ""
                    continue

            if j == 0:
                #Do this one time only
                lst.append(s[idx:idx+num])
                j = idx
            if idx >= j + num - 1:
                print(idx)
                num = -1
                j = 0

        return lst if lst else [""]
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))