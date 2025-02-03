# Rodrigo (Capital One) - 
#https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=company&envId=capital-one&favoriteSlug=capital-one-six-months
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, num):
        node = self.root
        for digit in str(num):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]

    def find_longest_prefix(self, num):
        node = self.root
        prefix_length = 0

        for digit in str(num):
            if digit in node.children:
                prefix_length += 1
                node = node.children[digit]
            else:
                break
        return prefix_length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num in arr1:
            trie.add(num)
        
        #Find longest prefix of arr1 and arr2
        res = 0
        for num in arr2:
            res = max(res,trie.find_longest_prefix(num))
        
        return res
