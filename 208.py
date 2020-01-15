# Implement Trie (Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class TrieNode(object):
    def __init__(self, char=None):
        self.val = char
        self.iskey = False
        self.counter = 0
        self.children = collections.defaultdict(TrieNode)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode('w')
            current.counter += 1
            current = current.children.get(w)
        current.iskey = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.iskey


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True


    def delete(self, word):
        current = self.root
        for w in word:
            current.counter -= 1
            current = current.children.get(w)
        current.iskey = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
