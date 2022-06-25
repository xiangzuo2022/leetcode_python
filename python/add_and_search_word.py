
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

"""
# 解题思路：字典树（Trie），通配符.可以用枚举实现 dfs。
"""

class TrieNode:
    def __init__(self):        
        self.childs = dict()
        self.isWord = False


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()
        


    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child == None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.find(self.root,word)

    def find(self,node,word):
        if word == '':
            return node.isWord
        if word[0] == '.':
            for i in node.childs:
                if self.find(node.childs[i],word[1:]):
                    return True
        else:
            child = node.childs.get(word[0])
            if child:
                return self.find(child,word[1:])
        return False





        
























