# Word Search

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution(object):
    def wordsearch(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word[1:]):
                        return True
        return False

    def dfs(self, board, x, y, word):
        if len(word) == 0:
            return True
        # up
        if x > 0 and board[x-1][y] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(board, x-1, y, word[1:]):
                return True
            board[x][y] = tmp
        # down
        if x < len(board) - 1 and board[x+1][y] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(board, x+1, y, word[1:]):
                return True
            board[x][y] = tmp
        # left
        if y > 0 and board[x][y-1] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(board, x, y-1, word[1:]):
                return True
            board[x][y] = tmp
        # right
        if y < len(board[0]) - 1 and board[x][y+1] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(board, x, y+1, word[1:]):
                return True
            board[x][y] = tmp
        return False


# II

# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example:

# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]

# Output: ["eat","oath"]

class Solution(object):
    def findWords(self, board, words):
        w, h = len(board[0]), len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)

        visited = [[False] * w for x in range(h)]
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        res = []

        def dfs(word, node, x, y):
            node = node.childrens.get(board[x][y])
            if node is None:
                return
            visited[x][y] = True
            for d in direction:
                nx, ny = x + d[0], y + d[1]
                if nx >= 0 and nx <= h and ny >= 0 and ny <= w and not visited[nx][ny]:
                    dfs(word + board[nx][ny], node, nx, ny)
            if node.isWord:
                res.append(word)
                trie.delete(word)
            visited[x][y] = False

        for x in range(h):
            for y in range(w):
                dfs(board[x][y], trie.root, x, y)

        return sorted(res)

class TrieNode:
    def __init__(self):
        self.childrens = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            child = node.childrens.get(c, None)
            if child is None:
                child = TrieNode
                node.childrens[c] = child
            node = child
        node.isWord = True

    def delete(self, word):
        node = self.root
        queue = []
        for c in word:
            queue.append((c, node))
            child = node.childrens.get(c, None)
            if child is None:
                return False
            node = child
        if not node.isWord:
            return False
        if len(node.childrens):
            node.isWord = False
        else:
            for c, node in reversed(queue):
                del node.childrens[c]
                if len(node.childrens) or node.isWord:
                    break
        return True


sol = Solution()
print(sol.wordsearch(board=[['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], word='SEE'))
