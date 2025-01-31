class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(count, node):
            if count == len(word):
                return node.endOfWord

            c = word[count]
            if c == '.':
                for i in range(0, 26):
                    if node.children[i] != None:
                        if dfs(count + 1, node.children[i]):
                            return True
            else:
                idx = ord(c) - ord('a')
                if node and node.children[idx] != None:
                    return dfs(count + 1, node.children[idx])
            return False

        return dfs(0, self.root)

