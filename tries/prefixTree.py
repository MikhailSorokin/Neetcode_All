class TrieNode:
    
    # Array version O(26) memory per node so n * 26 memory, not as efficient as map
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        increment = ""
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]

        return curr.endOfWord == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True

class TrieNode:

    # Map version (more efficient memory) - O(1) per map
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.endOfWord == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        